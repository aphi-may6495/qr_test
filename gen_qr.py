import base64
from os.path import exists
import qrcode

arr = [
'ราชดำริห์|GCR120-121|ค่าไฟฟ้า|9367646|60',
'ราชดำริห์|4CR420|ค่าไฟฟ้า|A221-7004966UL|1',
'ราชดำริห์|BMA002|ค่าไฟฟ้า|12300443|1',
'ราชดำริห์|4CR405|ค่าไฟฟ้า|9317413|1',
'ราชดำริห์|4CR405|ค่าน้ำ|219186|1',
'ราชดำริห์|4CR420|ค่าน้ำ|211473|1',
'ราชดำริห์|4FC007|ค่าน้ำ|KENT-041-6653-50|1',
'ราชดำริห์|4FC007|ค่าแก๊ส|46249HP|1',
'ราชดำริห์|4CR405|ค่าแก๊ส|9317413|1',
'ราชดำริห์|4CR409|ค่าแก๊สBJ|46217HP|1'
]
en_arr = []
de_arr = []

def encode_64(data):
	u8 = data.encode('utf8')
	b64 = base64.b64encode(u8)
	return b64

def decode_64(data):
	u8 = base64.b64decode(data)
	str = u8.decode('utf8')
	return str

def gen_qrcode(str):
  return qrcode.make(str)

for i in arr:
	b64 = encode_64(i)
	en_arr.append(b64)

for i, v in enumerate(en_arr):
  img = gen_qrcode(v)
  img.save('qr_img/'+'meter_'+str(i)+'.png')