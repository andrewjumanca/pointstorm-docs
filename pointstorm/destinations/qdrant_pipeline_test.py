from qdrant_client import QdrantClient
from langchain.vectorstores import Qdrant



qdrant = QdrantClient(":memory:")


# (Re)Creating a collection, specifying the vector configuration and embedding details (in our case we have our own)
qdrant.recreate_collection(
    collection_name="development"#,
    # vectors_config=models.VectorParams(
    #     size=encoder.get_sentence_embedding_dimension(), # Vector size is defined by used model
    #     distance=models.Distance.COSINE
    # )
)

# Uploading a collection. 
qdrant.upload_records(
    collection_name="my_books",
    records=[]
)