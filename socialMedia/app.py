from flask import Flask
from artificial_intelligence import ModelType, utils
from huggingface_hub import login
from dotenv import load_dotenv
import os
load_dotenv()
app = Flask(__name__)
hf_token = os.getenv('HF_AUTH_TOKEN')
login(hf_token)
@app.route('/')
def hello_world():
    return 'Home'

@app.route('/sentiment_analysis_big_data')
def sentiment_analysis_bd():
    text_mock = "Had a great day at the beach, so relaxing. 🌊🏖 #vacation #chill"
    results ={}
    for ai_model in ModelType.SentimentAnalysis:
        pipeline_load = utils.import_model_from_hugging_face("sentiment-analysis", ai_model.value)
        result = utils.process_data(text_mock, pipeline_load)
        label, score =  utils.get_score(result)
        results[f"{ai_model.value}"] = [label,score]
    return results

@app.route('/sentiment_analysis')
def sentiment_analysis():
    text_mock = "Had a great day at the beach, so relaxing. 🌊🏖 #vacation #chill"
    ai_model = ModelType.SentimentAnalysis.BERT
    results = utils.get_model_results("sentiment-analysis", ai_model.value, text_mock)
    if results[ai_model.value][1] == "LABEL_0":
        sentiment = "POSITIVE"
    elif results[ai_model.value][1] == "LABEL_1":
        sentiment = "NEGATIVE"
    else:
        sentiment = "NEUTRAL"
    results[ai_model.value][0] = sentiment
    results["text"] = text_mock
    return results


if __name__ == '__main__':
    app.run(debug=True,port=5001)
