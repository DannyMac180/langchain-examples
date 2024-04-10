from langchain_exa import ExaSearchRetriever, ExaSearchResults, ExaFindSimilarResults


exa_api_key = "03ab2ac5-66d5-46c1-8f30-91585712609a"
exa_base_url = "https://api.exa.com"


# Create a new instance of the ExaSearchRetriever
exa = ExaSearchRetriever(exa_api_key=exa_api_key)

# Search for a query
results  = exa.get_relevant_documents(query="What is the capital of France?")

# Print the results
print(results)

