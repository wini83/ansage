#!flask/bin/python
# -*- coding: utf-8 -*-
from flask import Flask, jsonify

app = Flask(__name__)

from flask_httpauth import HTTPBasicAuth
auth = HTTPBasicAuth()

@auth.get_password
def get_password(username):
    if username == 'miguel':
        return 'python'
    return None

@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)

from flask import url_for

from flask import make_response

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

def make_public_task(task):
    new_task = {}
    for field in task:
        if field == 'id':
            new_task['uri'] = url_for('get_announcement', task_id=task['id'], _external=True)
        else:
            new_task[field] = task[field]
    return new_task

tasks= [
    {
        'id': 1,
        'text': u'Pociąg osobowy do Grodziska Wielkopolskiego odjedzie z toru pierwszego przy peronie drugim',
        'lang': u'pl', 
        'fromTTS': True,
        'played': False
    }
]

from flask import abort

@app.route('/pa/api/v1.0/anouncements/<int:task_id>', methods=['GET'])
def get_announcement(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})


@app.route('/pa/api/v1.0/anouncements', methods=['GET'])
def get_announcements():
    return jsonify({'tasks': [make_public_task(task) for task in tasks]})

from flask import request




@auth.login_required
@app.route('/pa/api/v1.0/anouncements', methods=['POST'])
def create_anouncement():
    if not request.json or not 'text' in request.json:
        abort(400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'text': request.json['text'],
        'lang': request.json.get('lang', ""),
        'played': False,
        'fromTTS':True
    }
    import engine
    engine.downloadMP3(task['text'],'dupa.mp3')   
    tasks.append(task)

    return jsonify({'task': task}), 201

if __name__ == '__main__':
    app.run(debug=True)