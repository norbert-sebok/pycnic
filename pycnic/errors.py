from .data import STATUSES

class PycnicError(Exception):
    pass

class HTTPError(PycnicError):
    status_code = 0
    status = None
    message = None
    data = None

    def __init__(self, status_code, message, data=None):
        if self.status_code:
            status_code = self.status_code
        self.status_code = status_code
        self.status = STATUSES[status_code]
        self.message = message
        self.data = data

    def response(self):
        return { 
            "status": self.status,
            "status_code": self.status_code,
            "error":self.message,
            "data":self.data
        }

class HTTPNumeric(HTTPError):
    status_code = 0
    def __init__(self, message, data=None):
        super(HTTPError, self).__init__(self.status_code, message, data)
        self.status = STATUSES[self.status_code]
        self.message = message
        self.data = data

class HTTP_400(HTTPNumeric):
    status_code = 400

class HTTP_401(HTTPNumeric):
    status_code = 401

class HTTP_403(HTTPNumeric):
    status_code = 403

class HTTP_404(HTTPNumeric):
    status_code = 404
    
class HTTP_405(HTTPNumeric):
    status_code = 405

class HTTP_500(HTTPNumeric):
    status_code = 500
