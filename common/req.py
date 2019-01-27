from log.log import return_api_resp
import requests
import json
requests.packages.urllib3.disable_warnings()
import logging
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(levelname)s -- %(message)s")
LOG = logging.getLogger(__name__)

class Base(object):
    def __init__(self, project_id, url, port, token):
        self.project_id = project_id
        self.url = url
        self.port = port
        self.token = token
        self.headers = {"X-Auth-Token": token, "Content-Type": "application/json"}


@return_api_resp()
def _request(path, method, body=None, headers=None):
    if not headers:
        headers = {"Content-Type": "application/json"}
    ret = None
    if method == "post":
        ret = requests.post(path, headers=headers, verify=False, timeout=5, data=json.dumps(body))
    elif method == "get":
        ret = requests.get(path, headers=headers, verify=False, timeout=5)
    elif method == "put":
        ret = requests.put(path, headers=headers, verify=False, timeout=5, data=json.dumps(body))
    elif method == "delete":
        ret = requests.delete(path, headers=headers, verify=False, timeout=5, data=None)
    LOG.debug("Request response result : {}".format(json.dumps(ret.__dict__)))
    code, body = ret.status_code, ret.content
    LOG.info("Request resp code: {0}, body : {1}".format(code, body))    
    return ret


if __name__ == '__main__':
    print("hello")
