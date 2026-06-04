'''
This code is responsible for handling user queries, generating embeddings for the queries, and retrieving relevant information from the ChromaDB collections based on the generated embeddings.
1. we used path liberary to get abd extract the path for the retrivel pipeline
2 working of chromadb
-> needs to connect to a client to access the database
-> we can create collections in the database to store different types of data
-> we can query the collections using the query method, which takes in the query embeddings and the number of results to return
-> we can also specify the collection name to query from, which allows us to retrieve relevant information from specific collections based on the type of query we have.
-> we gave an n value using wich it extracted top 5 vectors using cosine simalrity and returned the results in the form of a dictionary which contains the ids, metadatas and documents of the retrieved results.
'''
from sentence_transformers import SentenceTransformer
import chromadb
from pathlib import Path
print("imported sucessfuly")
class dataQuery:
    def get_query(self):
        data =  str(input("Enter your query: "))
        query = [data]
        return query

obj = dataQuery()
dataquery = obj.get_query()

model = SentenceTransformer('all-MiniLM-L6-v2')
class embeddings:
    def get_embeddings(self, dataquery):
        embeddings = model.encode(dataquery)
        return embeddings

obj1 = embeddings()
data_embeddings = obj1.get_embeddings(dataquery)
DB_path = Path(__file__).parent.parent
client = chromadb.PersistentClient(path=DB_path/"embedding_storage"/"chromadb")
print(client.list_collections())
class retrieval:
    def char_retrieval(self,data_embeddings):
        collection = client.get_collection(name= "char_collection")
        results = collection.query(
            query_embeddings= data_embeddings.tolist(),
            n_results=5
        )
        return results
    def space_retrieval(self,data_embeddings):
        collection = client.get_collection(name= "space_collection")
        results = collection.query(
            query_embeddings= data_embeddings.tolist(),
            n_results=5
        )
        return results
    def nltk_retrieval(self,data_embeddings):
        collection = client.get_collection(name= "nltk_collection")
        results = collection.query(
            query_embeddings= data_embeddings.tolist(),
            n_results=5
        )
        return results
    
obj2 = retrieval()
char_results = obj2.char_retrieval(data_embeddings)
space_results = obj2.space_retrieval(data_embeddings)
nltk_results = obj2.nltk_retrieval(data_embeddings)
print("Char Retrieval Results: ", char_results)
print("Space Retrieval Results: ", space_results)
print("NLTK Retrieval Results: ", nltk_results) 