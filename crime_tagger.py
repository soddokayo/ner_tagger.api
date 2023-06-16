import re

CRIME_VOCAB_PATH = "data/crime_vocab.txt"
word_list = []

def load_list():
    global CRIME_VOCAB_PATH, word_list
    fin = open(CRIME_VOCAB_PATH, "r", encoding='utf-8')
    lines = fin.readlines()

    word_list = []
    for line in lines:
        word, ner_tag, _ = line.split('\t')
        dict_ = {
            "entity_group": ner_tag,
            "word": word,
        }
        word_list.append(dict_)

    return

load_list()

def crime_tagger(sent:str) -> str:
    res = []
    for dict_ in word_list:
        mat_obj = re.finditer(pattern=dict_["word"], string=sent)
        for match in mat_obj:
            dict_["start"] = match.start()
            dict_["end"] = match.end()
            res.append(dict_)
    return res