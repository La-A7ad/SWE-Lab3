from flask import Flask, request, jsonify

app = Flask(__name__)

# Global list to store items
items = [
    {'id': 1, 'name': 'Item One', 'description': 'First item'},
    {'id': 2, 'name': 'Item Two', 'description': 'Second item'}
]

# GET all items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

# GET a specific item by ID
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item:
        return jsonify(item)
    return jsonify({'error': 'Item not found'}), 404

# POST: Create a new item
@app.route('/items', methods=['POST'])
def create_item():
    data = request.get_json()
    if not data or not 'name' in data:
        return jsonify({'error': 'Invalid input'}), 400
    new_item = {
        'id': len(items) + 1,
        'name': data['name'],
        'description': data.get('description', '')
    }
    items.append(new_item)
    return jsonify(new_item), 201

# PUT: Update an existing item by ID
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    data = request.get_json()
    # Find the item by id
    item = next((item for item in items if item['id'] == item_id), None)
    if not item:
        return jsonify({'error': 'Item not found'}), 404

    # Update the item's name and/or description
    if 'name' in data:
        item['name'] = data['name']
    if 'description' in data:
        item['description'] = data['description']
    
    return jsonify(item), 200

if __name__ == '__main__':
    app.run(debug=True)
