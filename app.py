from flask import Flask, request, jsonify

api = Flask(__name__)

products = []
users = []
departments = []
categories = []


def get_next_id(lista):
    if lista:
        return max(item['id'] for item in lista) + 1
    return 1


@api.route("/")
def index():
    return jsonify({'version': '1.0.0'}), 200


@api.route("/products/<int:id>", methods=['GET'])
def get_product_by_id(id):
    for product in products:
        if product['id'] == id:
            return jsonify(product), 200
    return jsonify({'error': 'Produto não encontrado'}), 404


@api.route('/products', methods=['GET', 'POST'])
def product_handle():
    if request.method == 'POST':
        json_data = request.get_json()
        json_product = {
            'id': get_next_id(products),
            'nome': json_data["nome"],
        }
        products.append(json_product)
        return jsonify(json_product), 201

    elif request.method == 'GET':
        return jsonify(products), 200


@api.route("/users/<int:id>", methods=['GET'])
def get_user_by_id(id):
    for user in users:
        if user['id'] == id:
            return jsonify(user), 200
    return jsonify({'error': 'Usuário não encontrado'}), 404


@api.route('/users', methods=['GET', 'POST'])
def user_handle():
    if request.method == 'POST':
        json_data = request.get_json()
        json_user = {
            'id': get_next_id(users),
            'nome': json_data["nome"],
        }
        users.append(json_user)
        return jsonify(json_user), 201

    elif request.method == 'GET':
        return jsonify(users), 200


@api.route('/categories/<int:id>', methods=['GET'])
def get_category_by_id(id):
    for category in categories:
        if category['id'] == id:
            return jsonify(category), 200
    return jsonify({'error': 'Categoria não encontrada'}), 404


@api.route('/categories', methods=['GET', 'POST'])
def category_handle():
    if request.method == 'POST':
        json_data = request.get_json()
        json_category = {
            'id': get_next_id(categories),
            'nome': json_data['nome']
        }
        categories.append(json_category)
        return jsonify(json_category), 201

    elif request.method == 'GET':
        return jsonify(categories), 200


@api.route('/departments/<int:id>', methods=['GET'])
def get_department_by_id(id):
    for department in departments:
        if department['id'] == id:
            return jsonify(department), 200
    return jsonify({'error': 'Departamento não encontrado'}), 404


@api.route('/departments', methods=['GET', 'POST'])
def department_handle():
    if request.method == 'POST':
        json_data = request.get_json()
        json_department = {
            'id': get_next_id(departments),
            'nome': json_data['nome']
        }
        departments.append(json_department)
        return jsonify(json_department), 201

    elif request.method == 'GET':
        return jsonify(departments), 200


if __name__ == "__main__":
    api.run(debug=True)
