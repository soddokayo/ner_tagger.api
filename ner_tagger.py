
from transformers import pipeline

model_checkpoint = "soddokayo/klue-roberta-large-klue-ner"
ner = pipeline("ner", model=model_checkpoint, aggregation_strategy="simple")

def ner_tagger(sent:str):
    global ner
    ner_tags = ner(sent)

    for dict_ in ner_tags:
        dict_.pop('score')

    sent2 = list(sent)
    for dict_ in ner_tags[::-1]: # 인덱스 안깨지게 뒤에서부터
        sent2.insert(dict_['end'], "</span>")
        sent2.insert(
            dict_['start'], 
            '<span type="' + dict_['entity_group'] + '">'
        )
    return ner_tags #''.join(sent2)