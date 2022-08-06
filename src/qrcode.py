import time

from MyQR import myqr
from PIL import Image
from robomaster import conn

QRCODE_NAME = "qrcode.png"

if __name__ == '__main__':

	helper = conn.ConnectionHelper()
	info = helper.build_qrcode_string(ssid="比赛专用网络", password="43214321")
	myqr.run(words=info)
	time.sleep(1)
	img = Image.open(QRCODE_NAME)
	img.show()
	if helper.wait_for_connection():
		print("Connected!")
	else:
		print("Connect failed!")
