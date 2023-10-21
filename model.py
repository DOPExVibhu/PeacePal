from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class SimpleChatbot:
    def __init__(self, questions, answers):
        self.vectorizer = TfidfVectorizer()
        self.questions = questions
        self.answers = answers
        self.tfidf = self.vectorizer.fit_transform(self.questions)

    def get_response(self, user_input):
        user_vec = self.vectorizer.transform([user_input])
        cosines = cosine_similarity(user_vec, self.tfidf)
        index = cosines.argmax()
        return self.answers[index]

