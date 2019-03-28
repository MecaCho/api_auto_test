# -*-coding=UTF-8-*-
import json
import time
import uuid
import logging
from base import BASE
from log.log import assert_resp

TEST_CASE_SEQ = 0
TOTAL_TIME = 0
logging.basicConfig(level=logging.INFO, filename="report.html",
                    format='<tr bordercolor="Blue" align="left"><td colspan="7">%(asctime)s-%(message)s</td></tr>')
LOG = logging.getLogger(__name__)


class NodeCert(BASE):
    def __init__(self, project_id, url, api_version, pwd, usr):
        super(NodeCert, self).__init__(project_id, url, api_version, pwd, usr)
        self.project_id = project_id
        self.url = url
        self.api_version = api_version
        self.pwd = pwd
        self.usr = usr

    def assert_result(code=None, expect_code=None, comment=""):
        if code and expect_code:
            assert code == expect_code
        LOG.info('<td colspan="7">{}</td>'.format(comment))

    def create_node_cert(self, node_id, name=None, description="edge_node_value0", type_cert="device", del_key=None):

        data_post = {
            "name": name,
            "description": description,
            "type": type_cert
        }
        if del_key:
            data_post.pop(del_key, None)
        path = self.node_certs.format(
                project_id=self.project_id, node_id=node_id)
        ret = self.req(method="post", path=path, body=data_post)
        return ret.status_code, json.loads(ret.content) if ret.content else None

    @assert_resp(True, expection_code=200, comment=u"# IEF_NODE_ListNodeCerts 查询节点证书列表")
    def get_node_certs(self, node_id):
        path = self.node_certs.format(
                project_id=self.project_id, node_id=node_id)
        ret = self.req(method="get", path=path, body=None)
        return ret.status_code, json.loads(ret.content) if ret.content else None

    def delete_node_cert(self, cert_id, node_id):
        path = self.url_del_tag.format(
                project_id=self.project_id, resource_id=node_id, cert_id=cert_id)
        ret = self.req(method="delete", path=path, body=None)
        return ret.status_code, json.loads(ret.content) if ret.content else None

    def test_create_node_cert(self):
        code, node = self.create_node(name="test_ode_cert")
        assert code == 201
        node_id = node.get("node").get("id")
        # #         Depth	特性_名称	测试用例_编号	测试用例_名称	测试预期结果（返回码保持一致）	测试结果
        # ..	创建节点证书	 IEF_NODE_CERT_CreateNodeCert	POST /{version}/{project_id}/edgemgr/nodes/{node_id}/certs
        # 	节点证书名称检验	 IEF_NODE_CERT_CreateNodeCertCount_001	创建一个节点证书，证书名称name为null，创建失败	201
        self.assert_result(comment="IEF_NODE_CERT_CreateNodeCertCount_001	创建一个节点证书，证书名称name为null，创建失败")
        code, response = self.create_node_cert(node_id=node_id, name=None)
        assert code == 400
        # 		IEF_NODE_CERT_CreateNodeCertCount_002	创建一个节点证书，证书名称name为"null"，创建成功	201
        self.assert_result(comment="IEF_NODE_CERT_CreateNodeCertCount_002	创建一个节点证书，证书名称name为'null'，创建成功")
        code, response = self.create_node_cert(node_id=node_id, name="null")
        assert code == 201

        self.assert_result(comment="IEF_NODE_CERT_CreateNodeCertCount_067	创建一个节点证书，证书名称name重名，创建失败")
        code, response = self.create_node_cert(node_id=node_id, name="null")
        assert code == 400

        node_cert_id = response.get("id")
        self.assert_result(comment="TC_NODE_CERT_DeleteNodeCerts_012, 删除一个节点证书，带正确id， 删除成功")
        code, response = self.delete_node_cert(cert_id=node_cert_id, node_id=node_id)
        assert code == 204

        self.assert_result(comment="IEF_NODE_CERT_CreateNodeCertCount_068	创建一个节点证书，证书名称与已经删除的证书name重名，创建成功")
        code, response = self.create_node_cert(node_id=node_id, name="null")
        assert code == 201

        # 		IEF_NODE_CERT_CreateNodeCertCount_003	创建一个节点证书，证书名称name为空，创建失败	400
        self.assert_result(comment="IEF_NODE_CERT_CreateNodeCertCount_003	创建一个节点证书，证书名称name为空，创建失败")
        code, response = self.create_node_cert(node_id=node_id, name="")
        assert code == 400
        # 		IEF_NODE_CERT_CreateNodeCertCount_004	创建一个节点证书，证书名称name为空格，创建失败	400
        self.assert_result(comment="IEF_NODE_CERT_CreateNodeCertCount_004	创建一个节点证书，证书名称name为空格，创建失败")
        code, response = self.create_node_cert(node_id=node_id, name=" ")
        assert code == 400
        # IEF_NODE_CERT_CreateNodeCertCount_005	创建一个节点证书，证书名称name长度为1，创建成功	201
        self.assert_result(comment="IEF_NODE_CERT_CreateNodeCertCount_005	创建一个节点证书，证书名称name长度为1，创建成功")
        code, response = self.create_node_cert(node_id=node_id, name="q")
        assert code == 201

        # IEF_NODE_CERT_CreateNodeCertCount_006	创建一个节点证书，证书名称name长度为64，创建成功	201
        self.assert_result(comment="IEF_NODE_CERT_CreateNodeCertCount_006	创建一个节点证书，证书名称name长度为64，创建成功")
        code, response = self.create_node_cert(node_id=node_id, name="q"*64)
        assert code == 201

        # IEF_NODE_CERT_CreateNodeCertCount_007	创建一个节点证书，证书名称name长度为64(前面含有空格)，创建成功	201
        self.assert_result(comment="IEF_NODE_CERT_CreateNodeCertCount_007	创建一个节点证书，证书名称name长度为64(前面含有空格)，创建成功")
        code, response = self.create_node_cert(node_id=node_id, name="  "+"q" * 64)
        assert code == 201

        # IEF_NODE_CERT_CreateNodeCertCount_008	创建一个节点证书，证书名称name长度为64(中间含有空格)，创建失败	400
        self.assert_result(comment="IEF_NODE_CERT_CreateNodeCertCount_008	创建一个节点证书，证书名称name长度为64(中间含有空格)，创建失败")
        code, response = self.create_node_cert(node_id=node_id, name="q" * 32+" "+"q"*31)
        assert code == 400

        # IEF_NODE_CERT_CreateNodeCertCount_009	创建一个节点证书，证书名称name长度为65，创建失败	400
        self.assert_result(comment="IEF_NODE_CERT_CreateNodeCertCount_009	创建一个节点证书，证书名称name长度为65，创建失败")
        code, response = self.create_node_cert(node_id=node_id, name="q" * 65)
        assert code == 400

        # IEF_NODE_CERT_CreateNodeCertCount_010	创建一个节点证书，证书名称name字段缺失，创建失败	400
        self.assert_result(comment="IEF_NODE_CERT_CreateNodeCertCount_010	创建一个节点证书，证书名称name字段缺失，创建失败")
        code, response = self.create_node_cert(node_id=node_id, del_key="name")
        assert code == 400

        # 		IEF_NODE_CERT_CreateNodeCertCount_011	创建一个节点证书，证书名称name为“AAaa00-99_中”字符，创建失败	400
        self.assert_result(comment="IEF_NODE_CERT_CreateNodeCertCount_011	创建一个节点证书，证书名称name为“AAaa00-99_中”字符，创建失败")
        code, response = self.create_node_cert(node_id=node_id, name="AAaa00-99_中")
        assert code == 400

        # # 		IEF_NODE_CERT_CreateNodeCertCount_012	创建一个节点证书，证书名称name字段包含非打印字符ASCII（0~31），创建失败	400
        #     self.assert_result(comment="IEF_NODE_CERT_CreateNodeCertCount_006	创建一个节点证书，证书名称name长度为64，创建成功")
        #     code, response = self.create_node_cert(node_id=node_id, name="q" * 64)
        #     assert code == 201
        # 		IEF_NODE_CERT_CreateNodeCertCount_013	创建一个节点证书，证书名称name字段包含特殊字符*，创建失败	400
        # 		IEF_NODE_CERT_CreateNodeCertCount_014	创建一个节点证书，证书名称name字段包含特殊字符<，创建失败	400
        # 		 IEF_NODE_CERT_CreateNodeCertCount_015	创建一个节点证书，证书名称name字段包含特殊字符>，创建失败	400
        # 		 IEF_NODE_CERT_CreateNodeCertCount_016	创建一个节点证书，证书名称name字段包含特殊字符\，创建失败	400
        # 		 IEF_NODE_CERT_CreateNodeCertCount_017	创建一个节点证书，证书名称name字段包含特殊字符=，创建失败	400
        # 		 IEF_NODE_CERT_CreateNodeCertCount_018	创建一个节点证书，证书名称name字段包含特殊字符/，创建失败	400
        # 		 IEF_NODE_CERT_CreateNodeCertCount_019	创建一个节点证书，证书名称name字段包含特殊字符|，创建失败	400
        # 		 IEF_NODE_CERT_CreateNodeCertCount_021	创建一个节点证书，证书名称name字段包含特殊字符$，创建失败	400
        # 		 IEF_NODE_CERT_CreateNodeCertCount_022	创建一个节点证书，证书名称name字段包含特殊字符&，创建失败	400
        # 		 IEF_NODE_CERT_CreateNodeCertCount_023	创建一个节点证书，证书名称name字段包含特殊字符%，创建失败	400
        for k in "*<>\=/|$&%":
            self.assert_result(comment="IEF_NODE_CERT_CreateNodeCertCount_023	创建一个节点证书，证书名称name字段包含特殊字符{}，创建失败".format(k))
            code, response = self.create_node_cert(node_id=node_id, name="test"+k)
            assert code == 400

        # 	节点证书类型检验	 IEF_NODE_CERT_CreateNodeCertCount_024	创建一个节点证书，证书类型type为null，创建失败	400
        fake_cert_name = str(uuid.uuid4())
        self.assert_result(comment="IEF_NODE_CERT_CreateNodeCertCount_024	创建一个节点证书，证书类型type为null，创建失败")
        code, response = self.create_node_cert(node_id=node_id, name="test-node-cert", type_cert=None)
        assert code == 400

        self.assert_result(comment="IEF_NODE_CERT_CreateNodeCertCount_025	创建一个节点证书，不带证书类型type，创建失败")
        code, response = self.create_node_cert(node_id=node_id, name="test-node-cert", del_key="type")
        assert code == 400
        # 		 IEF_NODE_CERT_CreateNodeCertCount_025	创建一个节点证书，证书证书类型type为"null"，创建失败	400
        # 		 IEF_NODE_CERT_CreateNodeCertCount_026	创建一个节点证书，证书证书类型type为空，创建失败	400
        # 		 IEF_NODE_CERT_CreateNodeCertCount_027	创建一个节点证书，证书证书类型type为空格，创建失败	400
        # 		 IEF_NODE_CERT_CreateNodeCertCount_028	创建一个节点证书，证书证书类型type为device，创建成功	201
        self.assert_result(comment="IEF_NODE_CERT_CreateNodeCertCount_028	创建一个节点证书，证书证书类型type为device，创建成功")
        code, response = self.create_node_cert(node_id=node_id, name="test-node-cert", type_cert="device")
        assert code == 201
        # 		 IEF_NODE_CERT_CreateNodeCertCount_029	创建一个节点证书，证书证书类型type为application，创建成功	201
        self.assert_result(comment="IEF_NODE_CERT_CreateNodeCertCount_029	创建一个节点证书，证书证书类型type为application，创建成功")
        code, response = self.create_node_cert(node_id=node_id, name="test-node-cert", type_cert="application")
        assert code == 201
        # 		 IEF_NODE_CERT_CreateNodeCertCount_030	创建节点证书，type值为DEVICE，创建失败	400
        # 		 IEF_NODE_CERT_CreateNodeCertCount_031	创建节点证书，type值为Device，创建失败	400
        # 		 IEF_NODE_CERT_CreateNodeCertCount_032	创建节点证书，type值为APPLICATION，创建失败	400
        # 		 IEF_NODE_CERT_CreateNodeCertCount_033	创建节点证书，type值为Application，创建失败	400
        # 		 IEF_NODE_CERT_CreateNodeCertCount_034	创建节点证书，type值为*，创建失败	400
        # 		 IEF_NODE_CERT_CreateNodeCertCount_035	创建节点证书，type值为0，创建失败	400
        # 		 IEF_NODE_CERT_CreateNodeCertCount_036	创建节点证书，type值为#，创建失败	400
        # 		 IEF_NODE_CERT_CreateNodeCertCount_037	创建节点证书，type值为node，创建失败	400
        for value in ["null", None, "", " ", "DEVICE", "Device", "APPLICATION", "Application", "*", 0, "#", "node"]:
            self.assert_result(comment="IEF_NODE_CERT_CreateNodeCertCount_024	创建一个节点证书，证书类型type为{}，创建失败".format(value))
            code, response = self.create_node_cert(node_id=node_id, name="test-node-cert", type_cert=value)
            assert code == 400

# 	节点证书描述校验	IEF_NODE_CERT_CreateNodeCertCount_038	创建一个节点证书，证书名称description字段包含特殊字符*，创建失败	400
# 		IEF_NODE_CERT_CreateNodeCertCount_039	创建一个节点证书，证书名称description字段包含特殊字符*，创建失败	400
# 		IEF_NODE_CERT_CreateNodeCertCount_040	创建一个节点证书，证书名称description字段包含特殊字符*，创建失败	400
# 		IEF_NODE_CERT_CreateNodeCertCount_041	创建一个节点证书，证书名称description字段包含特殊字符*，创建失败	400
# 		IEF_NODE_CERT_CreateNodeCertCount_042	创建一个节点证书，证书名称description字段包含特殊字符*，创建失败	400
# 		IEF_NODE_CERT_CreateNodeCertCount_043	创建一个节点证书，证书名称description字段包含特殊字符*，创建失败	400
# 		IEF_NODE_CERT_CreateNodeCertCount_044	创建一个节点证书，证书名称description字段包含特殊字符*，创建失败	400
# 		IEF_NODE_CERT_CreateNodeCertCount_045	创建一个节点证书，证书名称description字段包含特殊字符*，创建失败	400
# 		IEF_NODE_CERT_CreateNodeCertCount_046	创建一个节点证书，证书名称description字段包含特殊字符*，创建失败	400
# 		IEF_NODE_CERT_CreateNodeCertCount_047	创建一个节点证书，证书名称description字段包含中文字符，创建成功	400
# 		IEF_NODE_CERT_CreateNodeCertCount_048	创建一个节点证书，证书名称description字段包含英文字符，创建成功	400
        for value in "*<>\=/|$&%":
            self.assert_result(comment="IEF_NODE_CERT_CreateNodeCertCount_039	创建一个节点证书，证书名称description字段包含特殊字符{}，创建失败".format(value))
            code, response = self.create_node_cert(node_id=node_id, name="test-node-cert", type_cert="device", description="This is a node cert test."+value)
            assert code == 400

# 	节点证书配额校验	IEF_NODE_CERT_CreateNodeCertCount_049	创建1个节点证书，创建成功	201
# 		IEF_NODE_CERT_CreateNodeCertCount_050	创建9个节点证书，创建成功	201
# 		IEF_NODE_CERT_CreateNodeCertCount_051	创建10个节点证书，创建成功	201
# 		IEF_NODE_CERT_CreateNodeCertCount_052	创建11个节点证书，创建失败	400
# 		IEF_NODE_CERT_CreateNodeCertCount_053	创建10个节点证书，删除一个证书，再创建一个证书，创建成功	201
# 		IEF_NODE_CERT_CreateNodeCertCount_054	创建10个节点证书，删除39个证书，再创建39个证书（重复删除再创建），创建成功	201
# 		IEF_NODE_CERT_CreateNodeCertCount_055	创建10个节点证书，删除40个证书，再创建40个证书（重复删除再创建），创建成功	201
# 		IEF_NODE_CERT_CreateNodeCertCount_056	创建10个节点证书，删除41个证书，再创建41个证书（重复删除再创建），创建失败	400
# 		IEF_NODE_CERT_CreateNodeCertCount_057	创建4999个节点证书，创建成功（单租户）	201
# 		IEF_NODE_CERT_CreateNodeCertCount_058	创建5000个节点证书，创建成功（单租户）	201
# 		IEF_NODE_CERT_CreateNodeCertCount_059	创建5001个节点证书，创建失败（单租户）	400
# 	节点证书权限校验	IEF_NODE_CERT_CreateNodeCertCount_060	创建节点证书，请求中node_id不存在，创建失败	400
# 		IEF_NODE_CERT_CreateNodeCertCount_061	创建节点证书，请求中node_id为其他project节点id，创建失败	404
# 		IEF_NODE_CERT_CreateNodeCertCount_062	创建节点证书，请求中project_id缺失，创建失败	404
# 		IEF_NODE_CERT_CreateNodeCertCount_063	创建节点证书，请求中project_id为其他租户的project_id，创建失败	400
# 		IEF_NODE_CERT_CreateNodeCertCount_064	创建节点证书，请求中project_id不存在，创建失败	400
# 		IEF_NODE_CERT_CreateNodeCertCount_065	创建节点证书，请求中node_id缺失，创建失败	404
# 		IEF_NODE_CERT_CreateNodeCertCount_066	创建节点证书，请求中不带token，创建失败	401

        self.assert_result(comment="TC_NODE_CERT_DeleteNodeCerts_001	删除节点证书，请求中node_id不存在，删除失败")
        code, response = self.delete_node_cert(node_id="xxxxx", cert_id=node_cert_id)
        assert code == 404
        # 		TC_NODE_CERT_DeleteNodeCerts_002	删除节点证书，请求中node_id为其他project节点id，删除失败	404
        fake_node_id = str(uuid.uuid4())
        self.assert_result(comment="TC_NODE_CERT_DeleteNodeCerts_002	删除节点证书，请求中node_id为其他project节点id，删除失败")
        code, response = self.delete_node_cert(node_id=fake_node_id, cert_id=node_cert_id)
        assert code == 404
        # 		TC_NODE_CERT_DeleteNodeCerts_003	删除节点证书，请求中project_id缺失，删除失败	400
        # 		TC_NODE_CERT_DeleteNodeCerts_004	删除节点证书，请求中project_id为其他租户的project_id，删除失败	400
        # 		TC_NODE_CERT_DeleteNodeCerts_005	删除节点证书，请求中project_id不存在，删除失败	400
        # 		TC_NODE_CERT_DeleteNodeCerts_006	删除节点证书，请求中node_id缺失，删除失败	404
        self.assert_result(comment="TC_NODE_CERT_DeleteNodeCerts_006	删除节点证书，请求中node_id缺失，删除失败")
        code, response = self.delete_node_cert(node_id="", cert_id=node_cert_id)
        assert code == 404
        # 		TC_NODE_CERT_DeleteNodeCerts_007	删除节点证书，请求中不带token，删除失败	401
        # 		TC_NODE_CERT_DeleteNodeCerts_008	删除节点证书，请求中带无效token，删除失败	401
        # 		TC_NODE_CERT_DeleteNodeCerts_009	删除节点证书，请求中cert_id不存在，删除失败	404
        self.assert_result(comment="# TC_NODE_CERT_DeleteNodeCerts_009	删除节点证书，请求中cert_id不存在，删除失败")
        code, response = self.delete_node_cert(node_id=node_id, cert_id=fake_node_id)
        assert code == 404
        # 		TC_NODE_CERT_DeleteNodeCerts_010	删除节点证书，请求中cert_id为其他project，删除失败	404
        self.assert_result(comment="TC_NODE_CERT_DeleteNodeCerts_010	删除节点证书，请求中cert_id为其他project，删除失败")
        code, response = self.delete_node_cert(node_id=node_id, cert_id=fake_node_id)
        assert code == 404
        # 		TC_NODE_CERT_DeleteNodeCerts_011	删除节点证书，请求中cert_id为其他node，删除失败	404
        self.assert_result(comment="# TC_NODE_CERT_DeleteNodeCerts_011	删除节点证书，请求中cert_id为其他node，删除失败")
        code, response = self.delete_node_cert(node_id=node_id, cert_id=fake_node_id)
        assert code == 404

    def test_list_node_certs(self):
        nodes = self.list_ress(resource_type="nodes")
        node_id = nodes.get("nodes")[0].get("id")
        self.assert_result(comment="# TC_NODE_CERT_ListNodeCerts_010	请求体中带所有必选参数，查询节点证书成功")
        code, response = self.get_node_certs(node_id=node_id)
        assert code == 200
        # Depth	特性_名称	测试用例_编号	测试用例_名称	测试预期结果（返回码保持一致）	测试结果
        # …	查询节点证书	 TC_NODE_CERT_ListNodeCerts	GET /{version}/{project_id}/nodes/{node_id}/certs
        # 		         TC_NODE_CERT_ListNodeCerts_001	查询节点证书，请求中node_id不存在，查询失败	400
        self.assert_result(comment="# TC_NODE_CERT_ListNodeCerts_001	查询节点证书，请求中node_id不存在，查询失败")
        code, response = self.get_node_certs(node_id="xxxxx")
        assert code == 404
        # 		         TC_NODE_CERT_ListNodeCerts_002	查询节点证书，请求中node_id为其他project节点id，查询失败	404
        self.assert_result(comment="# TC_NODE_CERT_ListNodeCerts_002	查询节点证书，请求中node_id为其他project节点id，查询失败")
        fake_node_id = str(uuid.uuid4())
        code, response = self.get_node_certs(node_id=fake_node_id)
        assert code == 404
        # 		         TC_NODE_CERT_ListNodeCerts_004	查询节点证书，请求中project_id缺失，查询失败	404
        self.assert_result(comment="# TC_NODE_CERT_ListNodeCerts_004	查询节点证书，请求中project_id缺失，查询失败")
        # code, response = self.get_node_certs(node_id="xxxxx")
        # assert code == 400
        # 		         TC_NODE_CERT_ListNodeCerts_005	查询节点证书，请求中project_id为其他租户的project_id，查询失败	400
        # self.assert_result(comment="# TC_NODE_CERT_ListNodeCerts_001	查询节点证书，请求中node_id不存在，查询失败")
        # code, response = self.get_node_certs(node_id="xxxxx")
        # assert code == 400
        # 		         TC_NODE_CERT_ListNodeCerts_006	查询节点证书，请求中project_id不存在，查询失败	400
        self.assert_result(comment="# TC_NODE_CERT_ListNodeCerts_001	查询节点证书，请求中node_id不存在，查询失败")
        # code, response = self.get_node_certs(node_id="xxxxx")
        # assert code == 400
        # 		         TC_NODE_CERT_ListNodeCerts_007	查询节点证书，请求中node_id缺失，查询失败	404
        self.assert_result(comment="# TC_NODE_CERT_ListNodeCerts_007	查询节点证书，请求中node_id缺失，查询失败")
        code, response = self.get_node_certs(node_id="")
        assert code == 400
        # 		TC_NODE_CERT_ListNodeCerts_008	查询节点证书，请求中不带token，查询失败	401
        # self.assert_result(comment="# TC_NODE_CERT_ListNodeCerts_001	查询节点证书，请求中node_id不存在，查询失败")
        # code, response = self.get_node_certs(node_id="xxxxx")
        # assert code == 400
        # 		         TC_NODE_CERT_ListNodeCerts_009	查询节点证书，请求中带无效token，查询失败	401
        # self.assert_result(comment="# TC_NODE_CERT_ListNodeCerts_001	查询节点证书，请求中node_id不存在，查询失败")
        # code, response = self.get_node_certs(node_id="xxxxx")
        # assert code == 400

    def test_delete_node_cert(self):
        nodes = self.list_ress(resource_type="nodes")
        node_id = nodes.get("nodes")[0].get("id")
        self.assert_result(comment="# TC_NODE_CERT_ListNodeCerts_010	请求体中带所有必选参数，查询节点证书成功")
        code, response = self.get_node_certs(node_id=node_id)
        assert code == 200
        node_certs = response.get("certs")
        if node_certs:
            node_cert_id = node_certs[0].get("id")
        else:
            now = str(time.time())
            code, node_cert = self.create_node_cert(node_id=node_id, name="testnodecert", type="device", description=now)
            assert code == 201
            node_cert_id = node_cert.get("id")
        # Depth	特性_名称	测试用例_编号	测试用例_名称	测试预期结果（返回码保持一致）	测试结果
        # ..	删除节点证书	 TC_NODE_CERT_DeleteNodeCerts	DELETE /{version}/{project_id}/nodes/{node_id}/certs/{cert_id}
        # 	权限校验	 TC_NODE_CERT_DeleteNodeCerts_001	删除节点证书，请求中node_id不存在，删除失败	404

        self.assert_result(comment="TC_NODE_CERT_DeleteNodeCerts_001	删除节点证书，请求中node_id不存在，删除失败")
        code, response = self.delete_node_cert(node_id="xxxxx", cert_id=node_cert_id)
        assert code == 404
        # 		TC_NODE_CERT_DeleteNodeCerts_002	删除节点证书，请求中node_id为其他project节点id，删除失败	404
        fake_node_id = str(uuid.uuid4())
        self.assert_result(comment="TC_NODE_CERT_DeleteNodeCerts_002	删除节点证书，请求中node_id为其他project节点id，删除失败")
        code, response = self.delete_node_cert(node_id=fake_node_id, cert_id=node_cert_id)
        assert code == 404
        # 		TC_NODE_CERT_DeleteNodeCerts_003	删除节点证书，请求中project_id缺失，删除失败	400
        # 		TC_NODE_CERT_DeleteNodeCerts_004	删除节点证书，请求中project_id为其他租户的project_id，删除失败	400
        # 		TC_NODE_CERT_DeleteNodeCerts_005	删除节点证书，请求中project_id不存在，删除失败	400
        # 		TC_NODE_CERT_DeleteNodeCerts_006	删除节点证书，请求中node_id缺失，删除失败	404
        self.assert_result(comment="TC_NODE_CERT_DeleteNodeCerts_006	删除节点证书，请求中node_id缺失，删除失败")
        code, response = self.delete_node_cert(node_id="", cert_id=node_cert_id)
        assert code == 404
        # 		TC_NODE_CERT_DeleteNodeCerts_007	删除节点证书，请求中不带token，删除失败	401
        # 		TC_NODE_CERT_DeleteNodeCerts_008	删除节点证书，请求中带无效token，删除失败	401
        # 		TC_NODE_CERT_DeleteNodeCerts_009	删除节点证书，请求中cert_id不存在，删除失败	404
        self.assert_result(comment="# TC_NODE_CERT_DeleteNodeCerts_009	删除节点证书，请求中cert_id不存在，删除失败")
        code, response = self.delete_node_cert(node_id=node_id, cert_id=fake_node_id)
        assert code == 404
        # 		TC_NODE_CERT_DeleteNodeCerts_010	删除节点证书，请求中cert_id为其他project，删除失败	404
        self.assert_result(comment="TC_NODE_CERT_DeleteNodeCerts_010	删除节点证书，请求中cert_id为其他project，删除失败")
        code, response = self.delete_node_cert(node_id=node_id, cert_id=fake_node_id)
        assert code == 404
        # 		TC_NODE_CERT_DeleteNodeCerts_011	删除节点证书，请求中cert_id为其他node，删除失败	404
        self.assert_result(comment="# TC_NODE_CERT_DeleteNodeCerts_011	删除节点证书，请求中cert_id为其他node，删除失败")
        code, response = self.delete_node_cert(node_id=node_id, cert_id=fake_node_id)
        assert code == 404
