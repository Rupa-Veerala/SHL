from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class AssessmentRecommender:
    def __init__(self, df):
        self.df = df
        self.vectorizer = TfidfVectorizer(stop_words="english")
        self.assessment_vectors = self.vectorizer.fit_transform(df["description"])

    def recommend(self, query, top_k=10):
        query_vector = self.vectorizer.transform([query])
        similarities = cosine_similarity(query_vector, self.assessment_vectors).flatten()
        top_indices = similarities.argsort()[-top_k:][::-1]
        return self.df.iloc[top_indices]
