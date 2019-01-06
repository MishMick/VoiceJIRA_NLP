import requests
import keywords as key
import json
import keywords as keyword_extract
import action_item

fl = "data2.txt"

def pre_process(text):
    print("adding punctuation ")
    url = "http://bark.phon.ioc.ee/punctuator"    
    payload = ""
    response = requests.request("POST", url, data=payload, params={"text":text})
    return(response.text)
    

def get_summary(id, text, ratio , flag, length):    
    text = pre_process(text)  + 'okay'  
    print("Params ",id,text.replace('%20',' '))
    if flag=='True': 
        with open(fl) as f:
            data = json.load(f)
        f.close()
        
        data[id] = {}
        data[id]['name'] = id
        data[id]['text'] = text
        #MoM =  summarize(text, ratio = ratio)
        #data[id]['MoM'] = MoM
        data[id]['length'] = length
        data[id]['edit'] = True
        #print(data)
        
        with open(fl,'w') as f:
            f.write(json.dumps(data, indent=3))
        f.close()
    
    keyword_extract.get_keywords(id, text)
    return action_item.get_action_items(id,text)
        
