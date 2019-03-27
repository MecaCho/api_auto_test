Depth	特性_名称	测试用例_编号	测试用例_名称	测试预期结果（返回码保持一致）	测试结果	问题备注
..	查询资源实例	 IEF_NODE_CERT_CreateNodeCert	POST /{version}/{project_id}/edgemgr/nodes/{node_id}/certs			
	节点证书名称检验	 IEF_NODE_CERT_CreateNodeCertCount_001	创建一个节点证书，证书名称name为null，创建失败	201		
		 IEF_NODE_CERT_CreateNodeCertCount_002	创建一个节点证书，证书名称name为"null"，创建成功	201		
		 IEF_NODE_CERT_CreateNodeCertCount_003	创建一个节点证书，证书名称name为空，创建失败	400		
		 IEF_NODE_CERT_CreateNodeCertCount_004	创建一个节点证书，证书名称name为空格，创建失败	400		
		 IEF_NODE_CERT_CreateNodeCertCount_005	创建一个节点证书，证书名称name长度为1，创建成功	201		
		 IEF_NODE_CERT_CreateNodeCertCount_006	创建一个节点证书，证书名称name长度为64，创建成功	201		
		 IEF_NODE_CERT_CreateNodeCertCount_007	创建一个节点证书，证书名称name长度为64(前面含有空格)，创建成功	201		
		 IEF_NODE_CERT_CreateNodeCertCount_008	创建一个节点证书，证书名称name长度为64(中间含有空格)，创建失败	400		
		 IEF_NODE_CERT_CreateNodeCertCount_009	创建一个节点证书，证书名称name长度为65，创建失败	400		
		 IEF_NODE_CERT_CreateNodeCertCount_010	创建一个节点证书，证书名称name字段缺失，创建失败	400		
		 IEF_NODE_CERT_CreateNodeCertCount_011	创建一个节点证书，证书名称name为“AAaa00-99_中”字符，创建失败	400		
		 IEF_NODE_CERT_CreateNodeCertCount_012	创建一个节点证书，证书名称name字段包含非打印字符ASCII（0~31），创建失败	400		
		 IEF_NODE_CERT_CreateNodeCertCount_013	创建一个节点证书，证书名称name字段包含特殊字符*，创建失败	400		
		 IEF_NODE_CERT_CreateNodeCertCount_014	创建一个节点证书，证书名称name字段包含特殊字符<，创建失败	400		
		 IEF_NODE_CERT_CreateNodeCertCount_015	创建一个节点证书，证书名称name字段包含特殊字符>，创建失败	400		
		 IEF_NODE_CERT_CreateNodeCertCount_016	创建一个节点证书，证书名称name字段包含特殊字符\，创建失败	400		
		 IEF_NODE_CERT_CreateNodeCertCount_017	创建一个节点证书，证书名称name字段包含特殊字符=，创建失败	400		
		 IEF_NODE_CERT_CreateNodeCertCount_018	创建一个节点证书，证书名称name字段包含特殊字符/，创建失败	400		
		 IEF_NODE_CERT_CreateNodeCertCount_019	创建一个节点证书，证书名称name字段包含特殊字符|，创建失败	400		
		 IEF_NODE_CERT_CreateNodeCertCount_020	创建一个节点证书，证书名称name字段包含特殊字符","，创建失败	400		
		 IEF_NODE_CERT_CreateNodeCertCount_021	创建一个节点证书，证书名称name字段包含特殊字符$，创建失败	400		
		 IEF_NODE_CERT_CreateNodeCertCount_022	创建一个节点证书，证书名称name字段包含特殊字符&，创建失败	400		
		 IEF_NODE_CERT_CreateNodeCertCount_023	创建一个节点证书，证书名称name字段包含特殊字符%，创建失败	400		
	节点证书类型检验	 IEF_NODE_CERT_CreateNodeCertCount_024	创建一个节点证书，证书类型type为null，创建失败	400		
		 IEF_NODE_CERT_CreateNodeCertCount_025	创建一个节点证书，证书证书类型type为"null"，创建失败	400		
		 IEF_NODE_CERT_CreateNodeCertCount_026	创建一个节点证书，证书证书类型type为空，创建失败	400		
		 IEF_NODE_CERT_CreateNodeCertCount_027	创建一个节点证书，证书证书类型type为空格，创建失败	400		
		 IEF_NODE_CERT_CreateNodeCertCount_028	创建一个节点证书，证书证书类型type为device，创建成功	201		
		 IEF_NODE_CERT_CreateNodeCertCount_029	创建一个节点证书，证书证书类型type为application，创建成功	201		
		 IEF_NODE_CERT_CreateNodeCertCount_030	创建节点证书，type值为DEVICE，创建失败	400		
		 IEF_NODE_CERT_CreateNodeCertCount_031	创建节点证书，type值为Device，创建失败	400		
		 IEF_NODE_CERT_CreateNodeCertCount_032	创建节点证书，type值为APPLICATION，创建失败	400		
		 IEF_NODE_CERT_CreateNodeCertCount_033	创建节点证书，type值为Application，创建失败	400		
		 IEF_NODE_CERT_CreateNodeCertCount_034	创建节点证书，type值为*，创建失败	400		
		 IEF_NODE_CERT_CreateNodeCertCount_035	创建节点证书，type值为0，创建失败	400		
		 IEF_NODE_CERT_CreateNodeCertCount_036	创建节点证书，type值为#，创建失败	400		
		 IEF_NODE_CERT_CreateNodeCertCount_037	创建节点证书，type值为node，创建失败	400		
	节点证书描述校验					

	 
特性_名称	测试用例_编号	测试用例_名称	测试预期结果（返回码保持一致）	测试用例_设计描述	测试用例_测试步骤
查询资源实例	 TC_TMS_QuerryResourceinstance	GET /{version}/{project_id}/{resource_type}/{resource_id}/tags			
 TC_TMS_QuerryAllTags_001	查询资源标签，请求中resource_id不存在，查询失败	400	failed	返回码为200，查询结果为空	200
 TC_TMS_QuerryAllTags_002	查询资源标签，请求中resource_id为其他资源ID，查询失败	400	failed	返回码为200，查询结果为空	400
 TC_TMS_QuerryAllTags_004	查询资源标签，请求中project_id缺失，查询失败	404	falied	返回码为400	400
 TC_TMS_QuerryAllTags_005	查询资源标签，请求中project_id为其他租户的project_id，查询失败	400	pass		
 TC_TMS_QuerryAllTags_006	查询资源标签，请求中project_id不存在，查询失败	400	pass		
 TC_TMS_QuerryAllTags_007	查询资源标签，请求中resource_type缺失，查询失败	404	pass		
 TC_TMS_QuerryAllTags_008	查询资源标签，请求中resource_type不存在，查询失败	400	pass		
 TC_TMS_QuerryAllTags_009	查询资源标签，请求中带无效token，查询失败	401	pass		
 TC_TMS_QuerryAllTags_010	查询资源标签，请求中不带token，查询失败	401	pass
