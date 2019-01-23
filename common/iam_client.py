#-*-coding=UTF-8-*-
import requests
from requests.exceptions import ReadTimeout

BASEURL = ""
URI = BASEURL+""

class Client_(object):

    def __init__(self):
        self.header = {'name': 'jack'}
        self.data = {'name': 'jack'}

    def get_service_t(self):
        url = URI
        header = self.header
        body = self
        return self.req_(url,header,data=body)

    def role_t(self):
        url = URI
        header = self.header
        body = {}
        return self.req_(url,header,data=body)

    def get_key(self):
        url = URI
        header = self.header
        body = {}
        return self.req_(url,header,data=body)

    def get_user_t(self):
        url = URI
        header = self.header
        body = {}
        return self.req_(url,header,data=body)

    def req_(self,url,header,method,data):
        if method == "post":
            response = requests.post(url, header, data=data)
            return response


def time_out():
    try:
        # 设置必须在500ms内收到响应，不然或抛出ReadTimeout异常
        response = requests.get("http://httpbin.org/get", timeout=0.5)
        print(response.status_code)
    except ReadTimeout:
        print('Timeout')

if __name__ == "__main__":
    test_client = Client_()
    print test_client.get_service_t()
