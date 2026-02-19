import json
import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
DATA_FILE = 'messages.json'

# Function to load messages from the JSON file
def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    except:
        return []

# Function to save messages to the JSON file
def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

@app.route('/', methods=['GET', 'POST'])
def index():
    messages = load_data()
    
    if request.method == 'POST':
        user_name = request.form.get('name')
        user_msg = request.form.get('message')
        
        if user_name and user_msg:
            # Create a new entry with a unique ID based on the timestamp or list length
            new_entry = {
                'id': len(messages) + 1,
                'name': user_name,
                'message': user_msg
            }
            messages.append(new_entry)
            save_data(messages)
            
        return redirect(url_for('index'))
    
    return render_template('index.html', messages=messages)

@app.route('/delete/<int:msg_id>')
def delete(msg_id):
    messages = load_data()
    # Keep only the messages that DON'T match the ID we want to delete
    updated_messages = [m for m in messages if m['id'] != msg_id]
    save_data(updated_messages)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)