#BW5M-M4IE-H1BZ-3WOA

#admin@admin.com
#admin
#admin123

#Bug
#Task
#Sub-task
#Improvement
#New Feature
#Epic

from jira.client import JIRA

jira_options={'server': 'http://35.225.152.39:8080/'}

jira=JIRA(options=jira_options,basic_auth=('admin','admin123'))

def assign_jira(id,act_item):
    #jira.add_user('Punyam', 'user1@admin.com', '12345', 'user1', False, True, False)
        
    for at in act_item:
        new_issue = jira.create_issue(project={'key': 'TP2'}, summary=str(id),   description=at['action'], issuetype={'name': 'Task'})
        new_issue.update(reporter={'name': 'Punyam'})
        

#text = [{'name':'n4','action_item':'a4'}]
#assign_jira(text)