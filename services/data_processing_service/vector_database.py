from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct
from qdrant_client.models import VectorParams, Distance


class VectorDatabase:
    def __init__(self) -> None:
        self.client = QdrantClient(host="localhost", port=6333)
        self.client.recreate_collection(
            collection_name="faces",
            vectors_config=VectorParams(size=768, distance=Distance.COSINE),
        )

    def insert(self, vectors, name, id):
        self.client.upsert(
            collection_name="faces",
            points=[
                PointStruct(
                    id=id,
                    vector=vector.tolist(),
                    payload={"person": name}
                )
                for idx, vector in enumerate(vectors)
            ]
        )

    def search(self, query_vector):
        search_result = self.client.search(
            collection_name="faces",
            query_vector=query_vector,
            limit=1
        )
        return search_result[0].score


if __name__ == "__main__":
    VectorDatabase()
