from sentence_transformers import SentenceTransformer
import chromadb

model = SentenceTransformer("all-MiniLM-L6-v2")
db = chromadb.Client()

query = "Arjun aur Meera ne puzzle kaise solve kiya?"
query_emb = model.encode(query).tolist()

# Retrieve evidence
results = db.search(query_emb, top_k=5)

print("Top Retrieved Evidence:\n", results)
print("\nEvidence ready for LLM reasoning ✔️")
