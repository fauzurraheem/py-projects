
document1 = "the fox jumped over the dog"
document2 = "this is for using inverted index"

token1 = document1.split()
token2 = document2.split()

terms = list(set(token1 + token2))

inverted_index = {}

for term in terms:
  documents = []
  if term in token1:
    documents.append("Document 1")
  if term in token2:
    documents.append("Document 2")
  inverted_index[term] = documents
  
  
for term, documents in inverted_index.items():
    print(term, "->", ", ".join(documents))