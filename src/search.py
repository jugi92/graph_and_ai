import os

from azure.identity import DefaultAzureCredential
from azure.search.documents import SearchClient
from azure.search.documents.models import VectorizableTextQuery

service_endpoint = os.getenv("AZURE_SEARCH_SERVICE_ENDPOINT")
# index_name = os.getenv("AZURE_SEARCH_INDEX_NAME")
index_name = "vector-1744205712204"
credential = DefaultAzureCredential() # require user to have role "Search Index Data Reader"

search_client = SearchClient(service_endpoint, index_name, credential)

query = "VENTILATION" # contained in docs
results = search_client.search(search_text=query, top=5)
for res in results:
    print(f"Document: {res['chunk']}, Score: {res['@search.score']}")

query = "BANG" # not contained in docs
results = search_client.search(search_text=query, top=5)
for res in results:
    print(f"Document: {res['chunk']}, Score: {res['@search.score']}")

# semantic query
vector_query = VectorizableTextQuery(text=query, k_nearest_neighbors=50, fields="text_vector")
results = search_client.search(
    search_text=query,
    vector_queries=[vector_query],
    top=5,
    # select=["chunk_id","parent_id","chunk","title","label","id"]
)

for res in results:
    print(f"Document: {res['chunk']}, Score: {res['@search.score']}")
