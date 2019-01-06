import requests
from flask import request
from flask import Flask
from flask_cors import CORS
import os 
from os import path 
from flask import send_file 
from flask import json
import text_summ
import keywords as keyword_extract
app = Flask(__name__)


CORS(app)

'''
@app.route('/meeting/save', methods=['POST']) 
def save_meetings():    
    content = request.json
    
    id = content['id']
    name = content['meeting_name']
    MoM = content['MoM']
    action_points = content['actionItems']
    
    save_meeting.save_meet(id, MoM, action_points, name)
    jira_api.assign_jira(id,action_points)
    
    return 'True'
'''

@app.route('/nlp', methods = ['GET']) 
def transform_text():
    id = request.args.get('id')
    text = request.args.get('text')
    ratio = request.args.get('ratio', default = 0.4)
    flag = request.args.get('flag', default = 'True')
    length = request.args.get('length', default = 0)
    return text_summ.get_summary(id, text, float(ratio), flag, length)

if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.run(host="0.0.0.0", port=9000)