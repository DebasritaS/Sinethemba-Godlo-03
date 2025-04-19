
from datetime import datetime
from access_request import AccessRequest
class User:
    def __init__(self, user_id, name, email, roles):
        self.__user_id = user_id
        self.__name = name
        self.__email = email
        self.__roles = roles  # List of roles (e.g., ['Reviewer', 'Manager'])

    def get_user_id(self):
        return self.__user_id

    def get_roles(self):
        return self.__roles

    def get_email(self):  
        return self.__email

    def assign_role(self, role):
        if role not in self.__roles:
            self.__roles.append(role)

    def remove_role(self, role):
        if role in self.__roles:
            self.__roles.remove(role)

    def request_access(self, request_id, resource):
        now = datetime.now()
        return AccessRequest(request_id=request_id, user=self, resource=resource, date_requested=now)

    def get_name(self):
        return self.__name