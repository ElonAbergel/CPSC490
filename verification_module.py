import json

# Function to parse the adjacency list from the response
def parse_adjacency_list(adj_list_str):
    adj_list = {}
    
    # Split by commas or newlines to handle both formats
    entries = adj_list_str.replace('\n', ',').split(',')

    for entry in entries:
        if ':' in entry:
            try:
                node, neighbors = entry.split(':', 1)  # Split only on the first colon
                node = int(node.strip())  # Try converting node to an integer
            
                # Clean the neighbors part to remove brackets and extra spaces
                neighbors = neighbors.replace('[', '').replace(']', '').strip()
                if neighbors:
                    neighbors = [int(n.strip()) for n in neighbors.split() if n.isdigit()]
                else:
                    neighbors = []
                
                adj_list[node] = neighbors
            except ValueError:
                print(f"Skipping invalid entry: {entry}")
                return None  # Return None to indicate a parsing failure
    
    return adj_list

# Function to detect cycles in the graph using DFS
def has_cycle(adj_list):
    visited = set()
    rec_stack = set()

    def dfs(node):
        if node in rec_stack:
            return True  # Cycle detected
        if node in visited:
            return False
        
        visited.add(node)
        rec_stack.add(node)

        for neighbor in adj_list.get(node, []):
            if dfs(neighbor):
                return True

        rec_stack.remove(node)
        return False

    # Check for cycles from each node
    for node in adj_list:
        if node not in visited:
            if dfs(node):
                return True
    return False

# Function to check if all nodes are reachable from the root (node 0)
def all_nodes_reachable(adj_list):
    visited = set()

    def dfs(node):
        visited.add(node)
        for neighbor in adj_list.get(node, []):
            if neighbor not in visited:
                dfs(neighbor)

    # Start DFS from node 0
    dfs(0)

    # Check if all nodes in the adjacency list were visited
    return len(visited) == len(adj_list)

# Function to verify the graph based on structure, checking for unrealistic cycles and reachability
def verify_query_against_graph(query, adj_list):
    # Check if the graph has cycles (which shouldn't exist in a well-formed DAG)
    if has_cycle(adj_list):
        print(f"Failed: Cycle detected in the graph")
        return False
    
    # Check if all nodes are reachable from node 0 (assuming node 0 is the root)
    if not all_nodes_reachable(adj_list):
        print(f"Failed: Not all nodes are reachable from the root node 0")
        return False

    # If no issues were found, the graph is valid
    return True

# Main function to process queries, verify, and save correct results
def process_queries(file_path):
    # Load the queries from the JSON file
    with open(file_path, 'r') as file:
        queries = json.load(file)

    incorrect_counter = 0
    correct_results = []
    easy_incorrect = 0
    medium_incorrect = 0
    hard_incorrect = 0

    # Process each query and response
    for idx, query_data in enumerate(queries):
        query = query_data['query']
        response = query_data['response']
        
        # Parse the response adjacency list
        generated_adj_list = parse_adjacency_list(response)
        if generated_adj_list is None:
            # If parsing fails, categorize as incorrect and by difficulty level
            incorrect_counter += 1
            if idx < 500:
                easy_incorrect += 1
            elif idx < 1000:
                medium_incorrect += 1
            else:
                hard_incorrect += 1
            continue

        print(f"Generated Adjacency List: {generated_adj_list}")
        
        # Verify if the graph has no cycles and all nodes are reachable
        is_correct = verify_query_against_graph(query, generated_adj_list)
        if is_correct:
            # If correct, save the query and response to the correct results list
            correct_results.append({
                'query': query,
                'correct_response': response
            })
        else:
            # Increment incorrect counter if verification fails and categorize
            incorrect_counter += 1
            if idx < 500:
                easy_incorrect += 1
            elif idx < 1000:
                medium_incorrect += 1
            else:
                hard_incorrect += 1

    # Save all correct results into a new JSON file
    with open('correct_results.json', 'w') as output_file:
        json.dump(correct_results, output_file, indent=4)

    print(f"Verification completed. Incorrect results: {incorrect_counter}")
    print(f"Easy incorrect: {easy_incorrect}, Medium incorrect: {medium_incorrect}, Hard incorrect: {hard_incorrect}")
    print("Correct results saved to 'correct_results.json'.")


# Example usage: Process the queries
process_queries('query_results.json')
