from enum import Enum

class AccessStatus(Enum):
    PENDING = "Pending"
    APPROVED = "Approved"
    REJECTED = "Rejected"
    REVOKED = "Revoked"

class AccessRequest:
    def __init__(self, request_id, user, resource, date_requested):
        self.__request_id = request_id
        self.__user = user  # Association to User
        self.__resource = resource
        self.__status = AccessStatus.PENDING
        self.__date_requested = date_requested

    def approve(self):
        self.__status = AccessStatus.APPROVED

    def reject(self):
        self.__status = AccessStatus.REJECTED

    def revoke(self):
        self.__status = AccessStatus.REVOKED

    def get_status(self):
        return self.__status.value
        
    def get_resource(self):
        return self.__resource

    def get_status(self):
        return self.__status.value 