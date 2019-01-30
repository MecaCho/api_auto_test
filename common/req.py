import requests
import json
import logging
from log.log import return_api_resp

requests.packages.urllib3.disable_warnings()
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s - %(name)s - %(message)s")
LOG = logging.getLogger(__name__)


class Base(object):
    def __init__(self, project_id, url, port, token):
        self.project_id = project_id
        self.url = url
        self.port = port
        self.token = token
        self.headers = {"X-Auth-Token": token, "Content-Type": "application/json"}


@return_api_resp()
def common_request(path, method, body=None, headers=None, portion=None):
    if not headers:
        headers = {"Content-Type": "application/json"}
    ret = None
#    LOG.info("Request method: {}, path: {}, body: {}".format(method, path, str(body)))
    import time
    time.sleep(0.5)
    if method == "post":
        ret = requests.post(path, headers=headers, verify=False, timeout=5, data=json.dumps(body))
    elif method == "get":
        ret = requests.get(path, headers=headers, verify=False, timeout=5)
    elif method == "put":
        ret = requests.put(path, headers=headers, verify=False, timeout=5, data=json.dumps(body))
    elif method == "delete":
        ret = requests.delete(path, headers=headers, verify=False, timeout=5, data=None)
    code, body = ret.status_code, json.loads(ret.content) if ret.content else None
    if portion:
        return code, body
 #   LOG.info("Request resp code: {0}, body : {1}".format(code, str(body)))
    return ret


if __name__ == '__main__':
    print("hello")
    body = '{"auth": {"scope": {"project": {"id": "988a1af23ff942879d4844f233ba7b23"}}, "identity": {"password": {"user": {"domain": {"name": "qiuwenqi"}, "password": "421521qwq~", "name": "qiuwenqi"}}, "methods": ["password"]}}}'
    path = "https://iam.cn-north-1.myhuaweicloud.com/v3/auth/tokens"
    common_request(path=path, method="post", body=json.loads(body))
    common_request(path="http://www.baidu.com", method="get")
