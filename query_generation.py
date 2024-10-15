import random

# Define variables, operations, and complexity levels
variables = ['x', 'y', 'A', 'B', 'C', 'D', 'E', 'F']
operations_easy = ['AND', 'OR', '>', '<', '==']
operations_moderate = ['+', '-', '*', '/', 'AND', 'OR', '>', '<', '==']
operations_hard = ['+', '-', '*', '/', 'AND', 'OR', '>', '<', '==', '!=']

# Function to generate an easy logical expression
def generate_easy_query():
    var1, var2 = random.sample(variables, 2)
    operation = random.choice(operations_easy)
    expression = f"{var1} {operation} {var2}"
    return f"Generate a graph for the expression: {expression}. Return only the adjacency list in the format: '0: [1, 2], 1: [2], 2: []', without additional text."

# Function to generate a more complex moderate logical expression
def generate_moderate_query():
    var1, var2, var3, var4 = random.sample(variables, 4)
    operation1, operation2, operation3 = random.choices(operations_moderate, k=3)
    nested_expr = f"({var1} {operation1} {var2}) {operation2} ({var3} {operation3} {var4})"
    return f"Generate a graph for the expression: {nested_expr}. Return only the adjacency list in the format: '0: [1, 2], 1: [2], 2: []', without additional text."

# Function to generate a highly complex hard logical expression with loops
def generate_hard_query():
    var1, var2, var3, var4, var5, var6, var7 = random.sample(variables, 7)
    operation1, operation2, operation3, operation4, operation5 = random.choices(operations_hard, k=5)
    
    # Construct a highly nested and complex expression
    nested_expr1 = f"({var1} {operation1} ({var2} {operation2} {var3}))"
    nested_expr2 = f"({var4} {operation3} ({var5} {operation4} {var6}))"
    
    # Final expression combining both nested expressions
    expression = f"(({nested_expr1}) {operation5} {var7}) {operation3} {nested_expr2}"
    
    return f"Generate a graph for the expression: {expression}. Return only the adjacency list in the format: '0: [1, 2], 1: [2], 2: []', without additional text."

# Generate queries of increasing difficulty
def generate_queries_by_difficulty(level='easy', num_queries=10):
    queries = []
    for _ in range(num_queries):
        if level == 'easy':
            query = generate_easy_query()
        elif level == 'moderate':
            query = generate_moderate_query()
        elif level == 'hard':
            query = generate_hard_query()
        queries.append(query)
    return queries

# Function to create all queries and write them into a full list in a text file
def create_all_queries_in_text_file(num_easy=10, num_moderate=10, num_hard=10):
    # Generate queries for each difficulty level
    easy_queries = generate_queries_by_difficulty('easy', num_easy)
    moderate_queries = generate_queries_by_difficulty('moderate', num_moderate)
    hard_queries = generate_queries_by_difficulty('hard', num_hard)
    
    # Combine all queries into one list
    all_queries = easy_queries + moderate_queries + hard_queries
    
    # Write all queries to a text file in a readable format
    with open('all_queries.txt', 'w') as f:
        for i, query in enumerate(all_queries, 1):
            f.write(f"Query {i}: {query}\n")
    
    print("All queries have been saved to 'all_queries.txt'")

# Example: Create a list of 5 easy, 5 moderate, and 5 hard queries and write them to a file
create_all_queries_in_text_file(num_easy=500, num_moderate=500, num_hard=500)
