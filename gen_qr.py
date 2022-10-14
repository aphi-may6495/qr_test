import base64
from os.path import exists
import qrcode

arr = [
	'ราชดำริห์|GCR120-121|ค่าไฟฟ้า|9367646|60',
'111172|4CR420|E|A221-7004966UL|1|7252',
'111172|BMA002|E|12300443|1|427020',
'111172|4CR405|E|9317413|1|99980',
'111172|4CR405|E|219186|1|33351',
'111172|4CR420|E|211473|1|1034',
'111172|4FC007|W|KENT-041-6653-50|1|2575',
'111172|4FC007|G|46249HP|1|2578',
'111172|4CR405|G|9317413|1|2422',
'111172|4CR409|GBJ|46217HP|1|4435'
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