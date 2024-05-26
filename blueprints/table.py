from flask import Blueprint, request, jsonify
from datastructures import Table

table_bp = Blueprint('tables', __name__)

tables = {}

@table_bp.route('/tables', methods=['POST'])
def add_table():
    body = request.json
    table_number = body.get('table_number')
    
    table = Table(table_number)
    tables[table_number] = table
    
    return jsonify({"table_number": table.table_number, "id_client": table.id_client, "products": table._products}), 201

@table_bp.route('/tables', methods=['GET'])
def get_tables():
    all_tables = []
    for table in tables.values():
        all_tables.append({
            "table_number": table.table_number,
            "id_client": table.id_client,
            "products": table._products
        })
    return jsonify(all_tables), 200

@table_bp.route('/tables/<int:table_number>/client', methods=['POST'])
def assign_client_to_table(table_number):
    table = tables.get(table_number)
    if not table:
        return jsonify({"message": "Table not found"}), 404
    
    client_id = table.assign_client()
    return jsonify({"table_number": table.table_number, "id_client": client_id}), 200

@table_bp.route('/tables/<int:table_number>/products', methods=['POST'])
def add_product_to_table(table_number):
    table = tables.get(table_number)
    if not table:
        return jsonify({"message": "Table not found"}), 404
    
    body = request.json
    product = body.get('product')
    
    if not product:
        return jsonify({"message": "Product is missing"}), 400

    table.add_product(product)
    return jsonify({"table_number": table.table_number, "products": table._products}), 200

@table_bp.route('/tables/<int:table_number>', methods=['DELETE'])
def clear_table(table_number):
    table = tables.get(table_number)
    if not table:
        return jsonify({"message": "Table not found"}), 404
    
    table.clear_table()
    return jsonify({"message": "Table cleared"}), 200