## 下载安装utx和coverage ##
	git clone https://github.com/qdyxmas/utx.git
	cd utx
	python3 setup.py install
	pip3 install coverage
	pip3 install colorama
## 运行testrun.py ##
	拷贝testrun.py到后台的根目录下
	cp testrun.py xxxx/backend
	cd xxxx/backend
	python3 testrun.py
## 日志查看 ##
	运行完成后在当前创建一个report目录，每次运行结果在report/时间戳目录下
