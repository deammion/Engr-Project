import time

"""
.....
"""

class response:


    def __init__(self, flow):
        self.flow = flow
        self.time = str(time.time())

    def get_time(self):
        return self.time

    def get_response(self):
        return self.flow

    def get_response_content(self):
        return self.flow.response.text