from log.log import return_api_resp
from module import tag, node


@return_api_resp()
def test_fun():
    return [i for i in xrange(100)]

from common.req import _request


if __name__ == '__main__':
    test_fun()
    import sys,getpass
    usr = sys.argv[1]

    pwd = getpass.getpass()
    # client = Base(project_id="", url="www.baidu.com", token="", port="")
    _request(method="get", path="http://www.baidu.com")
    client = node.Node(
            usr=usr, pwd=pwd, project_id="988a1af23ff942879d4844f233ba7b23",
            url="ief2.cn-north-1.myhuaweicloud.com", api_version="v2")
    client.list_nodes()

    client = tag.TAG(usr="", pwd="", project_id="", url="ief2.cn-north-1.myhuaweicloud.com", api_version="v2")
    client.query_ins(resource_type="edge_node", action="filter", tags=[{"key": "qwq", "values": []}])

