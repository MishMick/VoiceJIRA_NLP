import os, json
from flask import Flask, session

#import sentiment

#java_path = "C:/Program Files/Java/jdk1.8.0_191/jre/bin/java.exe"
#os.environ['JAVAHOME'] = java_path

fl = "data2.txt"

from nltk import pos_tag
from nltk.tag.stanford import StanfordPOSTagger as POS_Tag

action_keywords = ['please','kindly']

from nltk import RegexpParser
from nltk.tree import Tree
'''
def is_imperative(tagged_sent):
    if tagged_sent[0][1] == "VB" or tagged_sent[0][1] == "MD":
        return True
    else:
        chunk = get_chunks(tagged_sent)
        if type(chunk[0]) is Tree and chunk[0].label() == "VB-Phrase":
            return True
    return False
'''
def return_task(tagged_sent):
    task = ""
    chunks = get_chunks(tagged_sent)
    for chunk in chunks:
        if type(chunk) is Tree and chunk.label() == "VB-Phrase":
            for word in chunk: 
                if word[1] == "FW" or word[1] == "NN":
                    task += word[0]

    task = task.replace(',',' ')
    return task

def return_user(tagged_sent):  
    user = "" 
    chunks = get_chunks(tagged_sent)
    if type(chunks) is Tree:
        for chunk in chunks: 
            if chunk[1] == "NNP" or chunk[1] == "NP":
                user = chunk[0]
    return user

def get_chunks(tagged_sent):
    chunkgram = r"""VB-Phrase: {<DT><,>*<VB>}
                    #VB-Phrase: {<VBP><TO>}
                    #VB-Phrase: {<RB><VB>}
                    #VB-Phrase: {<UH><,>*<VB>}
                    #VB-Phrase: {<UH><,><VBP>}
                    VB-Phrase: {<PRP><MD>*<VB><IN><NN>*<FW>*}
                    VB-Phrase: {<NN.?>+<,>*<MD>*<VB>}
                    VB-Phrase: {<PRP>*<NNP>*<CC><PRP>*<MD>*<VB>+<FW>*}
                    """
    chunkparser = RegexpParser(chunkgram)
    return chunkparser.parse(tagged_sent)

def get_action_items(id,text):
    print("Called S")
    with open(fl) as f:
        data = json.load(f)
    f.close()
    
    english_postagger = POS_Tag('models/english-bidirectional-distsim.tagger', 'stanford-postagger.jar')    
    action_item = []
    for t in text.split('.'):
        if t:
            user_result = return_user(english_postagger.tag(t.split()))
            task_result = return_task(english_postagger.tag(t.split()))
            action_item.append({'action':task_result, 'name':user_result}) 
    data[id]['act_pt'] = action_item    
    with open(fl,'w') as f:
        f.write(json.dumps(data, indent=3))
    f.close()
    return str(action_item)

def get_action_items_n(text):
    print("Called N")
    act_item = ''
    for t in text.split('.'):
        if is_imperative(pos_tag(t.split())):
            act_item = act_item + '.' + t
    return act_item
