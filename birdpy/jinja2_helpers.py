import re


class JinjaArgs(object):
    def __init__(self):
        self.user = None
        self.request_obj = None
        self.last_req = None

    def kwargs(self):
        return self.__dict__

    def add_all(self, kwargs, regex=None):
        for key, val in kwargs.items():
            if regex is None or re.search(regex, key) is not None:
                self.__dict__[key] = val

