

class Base(object):
    def __init__(self, project_id, url, port, token):
        self.project_id = project_id
        self.url = url
        self.port = port
        self.token = token
        self.headers = {"X-Auth-Token": token, "Content-Type": "application/json"}

    def _request(self, path, method, body=None):
        global TEST_CASE_SEQ, TOTAL_TIME
        ret = None
        time_s = time.time()
        if method == "post":
            ret = requests.post(path, headers=self.headers, verify=False, timeout=5, data=json.dumps(body))
        elif method == "get":
            ret = requests.get(path, headers=self.headers, verify=False, timeout=5)
        elif method == "put":
            ret = requests.put(path, headers=self.headers, verify=False, timeout=5, data=json.dumps(body))
        elif method == "delete":
            ret = requests.delete(path, headers=self.headers, verify=False, timeout=5, data=None)
        time_cost = time.time() - time_s
        print "Cost time: {0}".format(time_cost)
        TEST_CASE_SEQ += 1
        TOTAL_TIME += time_cost
        return ret