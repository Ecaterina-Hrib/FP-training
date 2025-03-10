from enum import Enum

class SentimentAnalysis(Enum):
    BERT = "distilbert-base-uncased"
    ROBERTA_J = "j-hartmann/emotion-english-distilroberta-base"
    ROBERTA_C = "cardiffnlp/twitter-roberta-base-sentiment"
    XLNET = "xlnet-base-cased"
