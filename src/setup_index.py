import os

from azure.identity import DefaultAzureCredential
from azure.search.documents import SearchClient

# https://github.com/Azure/azure-search-vector-samples/blob/main/demo-python/code/basic-vector-workflow/azure-search-vector-python-sample.ipynb


# The following variables from your .env file are used in this notebook
search_endpoint = os.environ["AZURE_SEARCH_SERVICE_ENDPOINT"]
credential = DefaultAzureCredential()
index_name = os.getenv("AZURE_SEARCH_INDEX")
azure_openai_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"]
azure_openai_embedding_deployment = os.getenv("AZURE_OPENAI_EMBEDDING_DEPLOYMENT", "text-embedding-3-large")
azure_openai_embedding_dimensions = int(os.getenv("AZURE_OPENAI_EMBEDDING_DIMENSIONS", 1024))
embedding_model_name = os.getenv("AZURE_OPENAI_EMBEDDING_DEPLOYMENT", "text-embedding-3-large")
azure_openai_api_version = os.getenv("AZURE_OPENAI_API_VERSION", "2024-10-21") # https://learn.microsoft.com/en-us/azure/ai-services/openai/api-version-deprecation

search_client = SearchClient(search_endpoint, index_name, credential)

#TODO: continue
