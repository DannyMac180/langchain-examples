from langchain_exa import ExaFindSimilarResults

# Initialize the ExaFindSimilarResults tool
find_similar_tool = ExaFindSimilarResults(exa_api_key="03ab2ac5-66d5-46c1-8f30-91585712609a")

# Find similar results based on a URL
similar_results = find_similar_tool._run(
    url="http://espn.com",
    num_results=5,
    text_contents_options=True,
    highlights=True
)

print("Similar Results:", similar_results)