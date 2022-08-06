def start_connect(ep):
	print("连接EP中...")
	ep.initialize(conn_type='ap')
	v = ep.get_version()
	print("获取到机器固件版本：" + v)
	print("连接成功！")
