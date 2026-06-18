import re
import math
import numpy as np
from collections import Counter, defaultdict

def tokenize(text):
    text = str(text).lower()
    tokens = re.findall(r"[a-zA-ZÀ-ÿ0-9_]+", text)
    return tokens

class BM25:
    def __init__(self, documents, k1=1.5, b=0.75):
        self.k1 = k1
        self.b = b
        self.docs = [tokenize(doc) for doc in documents]
        self.N = len(self.docs)
        self.doc_len = np.array([len(doc) for doc in self.docs], dtype=np.float32)
        self.avgdl = self.doc_len.mean() if self.N > 0 else 1.0
        self.df = Counter()
        self.postings = defaultdict(list)
        for i, doc in enumerate(self.docs):
            tf = Counter(doc)
            for term, freq in tf.items():
                self.df[term] += 1
                self.postings[term].append((i, freq))
        self.idf = {term: math.log(1 + (self.N - df + 0.5) / (df + 0.5))
                    for term, df in self.df.items()}

    def get_scores(self, query):
        query_terms = tokenize(query)
        scores = np.zeros(self.N, dtype=np.float32)
        for term in query_terms:
            if term not in self.postings:
                continue
            idf = self.idf.get(term, 0.0)
            for doc_id, freq in self.postings[term]:
                dl = self.doc_len[doc_id]
                numerator = freq * (self.k1 + 1)
                denominator = freq + self.k1 * (1 - self.b + self.b * dl / self.avgdl)
                scores[doc_id] += idf * numerator / denominator
        return scores
