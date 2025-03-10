from transformers import pipeline

def import_model_from_hugging_face(category, model_name):
    return pipeline(category, model=model_name)

def process_data(text, pipeline_load):
    return pipeline_load(text)

def get_score(result):
    return result[0]['label'], result[0]['score']

def get_model_results(category,model_name,text):
    results = {}
    pipeline_load = import_model_from_hugging_face(category, model_name)
    result = process_data(text, pipeline_load)
    label, score =  get_score(result)
    results[f"{model_name}"] = [label,score]
    results["text"] = text
    return results