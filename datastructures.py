
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = []

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        if 'id' not in member:
            member['id'] = self._generateId()
        if 'last_name' not in member :
            member['last_name'] = self.last_name
        self._members.append(member)
        return member

    def delete_member(self, id):
        # fill this method and update the return
        for member in self._members:
            if member['id'] == id:
                self._members.remove(member)
        

    def get_member(self, id):
        # fill this method and update the return
        for member in self._members:
            if member['id'] == id:
                return member
            
    def update_member(self, id, updated_member):
        for index, member in enumerate(self._members):
            if member['id'] == id:
                self._members[index].update(updated_member)
                return self._members[index]
    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members

class Table: 
    def __init__(self, table_number):
        self.table_number = table_number
        self._products = []
        self.id_client = None
   
    def _generateId(self):
        return randint(0, 99999999)

    def add_product(self, product):
      self._products.append(product)
      return product

    def assign_client(self):
        self.id_client = self._generateId()
        return self.id_client
        
    def clear_table(self):
        self._products = []
        self.id_client = None