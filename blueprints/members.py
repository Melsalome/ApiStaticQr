from flask import Blueprint, request, jsonify
from datastructures import FamilyStructure

members_bp = Blueprint('members',__name__)
jackson_family = FamilyStructure("Jackson")



@members_bp.route('/members', methods=['POST'])
def new_member():
    body = request.json
    jackson_family.add_member(body)
    return jsonify(body), 200

@members_bp.route('/members', methods=['GET'])
def get_members_list():
    # this is how you can use the Family datastructure by calling its methods
    members = jackson_family.get_all_members()
    response_body = {
        "family": members
    }
    return response_body, 200

@members_bp.route('/members/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
   jackson_family.delete_member(member_id)
   return jsonify({"done":True}), 200

@members_bp.route('/members/<int:member_id>', methods=['GET'])
def get_member(member_id):
    member = jackson_family.get_member(member_id)
    return jsonify(member)

@members_bp.route('/members/<int:member_id>', methods=['PUT'])
def update_member(member_id):
    body = request.json
    member=jackson_family.update_member(member_id, body)
    return jsonify(member), 200