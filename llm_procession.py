import openai
import json

# Replace with your API key
api_key = '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'
# Set up the OpenAI API client
openai.api_key = api_key

# Initialize an empty list to store the results
results = []

# Open the text file and read each line (each query)
with open('all_queries.txt', 'r') as file:
    queries = file.readlines()

# Loop through each query, call the API, and store the results
for query in queries:
    query = query.strip()  # Remove leading/trailing spaces or newlines
    if not query:
        continue  # Skip empty lines
    
    try:
        # Call the OpenAI API with the query
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # You can use "gpt-4" if needed
            messages=[{"role": "user", "content": query}]
        )

        # Extract the API response text
        api_response = response['choices'][0]['message']['content'].strip()

        # Store the query and its response in a dictionary
        results.append({"query": query, "response": api_response})
        print(f"Query: {query}\n")

    except openai.error.AuthenticationError:
        print("API key is invalid. Please check your API key.")
        break
    except Exception as e:
        print(f"An error occurred with query '{query}': {e}")

# Save the results into a JSON file
with open('query_results.json', 'w') as json_file:
    json.dump(results, json_file, indent=4)