from flask import Flask, request, jsonify, render_template
import json

app = Flask(__name__)

# Load contacts from file
def load_contacts():
    try:
        with open("contacts.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save contacts to file
def save_contacts(contacts):
    with open("contacts.json", "w") as file:
        json.dump(contacts, file)

contacts = load_contacts()

@app.route('/')
def index():
    return render_template('index.html', contacts=contacts)

@app.route('/add', methods=['POST'])
def add_contact():
    new_contact = request.json
    if 'name' in new_contact and 'phone' in new_contact:
        contacts.append(new_contact)
        save_contacts(contacts)
        return jsonify(new_contact), 201
    else:
        return jsonify({'error': 'Name and Phone Number are required'}), 400

@app.route('/update/<int:index>', methods=['POST'])
def update_contact(index):
    updated_contact = request.json
    if 'name' in updated_contact and 'phone' in updated_contact:
        contacts[index] = updated_contact
        save_contacts(contacts)
        return jsonify(updated_contact)
    else:
        return jsonify({'error': 'Name and Phone Number are required'}), 400

@app.route('/delete/<int:index>', methods=['DELETE'])
def delete_contact(index):
    if 0 <= index < len(contacts):
        contacts.pop(index)
        save_contacts(contacts)
        return jsonify({'status': 'deleted'})
    else:
        return jsonify({'error': 'Index out of range'}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
