import base64
from os.path import exists
import qrcode
from tkinter import *
from PIL import Image, ImageFont, ImageDraw
import pandas as pd

# arr = [
# 'ราชดำริห์|GCR120-121|ค่าไฟฟ้า|9367646|60',
# 'ราชดำริห์|4CR420|ค่าไฟฟ้า|A221-7004966UL|1',
# 'ราชดำริห์|BMA002|ค่าไฟฟ้า|12300443|1',
# 'ราชดำริห์|4CR405|ค่าไฟฟ้า|9317413|1',
# 'ราชดำริห์|4CR405|ค่าน้ำ|219186|1',
# 'ราชดำริห์|4CR420|ค่าน้ำ|211473|1',
# 'ราชดำริห์|4FC007|ค่าน้ำ|KENT-041-6653-50|1',
# 'ราชดำริห์|4FC007|ค่าแก๊ส|46249HP|1',
# 'ราชดำริห์|4CR405|ค่าแก๊ส|9317413|1',
# 'ราชดำริห์|4CR409|ค่าแก๊สBJ|46217HP|1'
# ]
# en_arr = []
# de_arr = []

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

# for i in arr:
# 	b64 = encode_64(i)
# 	en_arr.append(b64)

# for i, v in enumerate(en_arr):
#   img = gen_qrcode(v)
#   img.save('qr_img/'+'meter_'+str(i+1)+'.png')

def query_data_excel(file_name):
	ex_rd = pd.read_excel(file_name, sheet_name='Sheet1', skiprows=1)
	print(ex_rd)
	ex_arr = ex_rd['Value'].values.tolist()
	print(type(ex_arr))
	err = []
	for i, v in enumerate(ex_arr):
		s = v.split('|')
		if (len(s) != 6):
			err.push(i)
	c = open('error_list.txt', 'w')
	c.close()
	f = open('error_list.txt', 'a')
	for i in err:
		f.write(i)
	f.close()
	return ex_arr

def add_text_below_img(img, msg):
	W, H = img.size
	font = ImageFont.truetype('georgia_bold.ttf', 30)
	draw = ImageDraw.Draw(img)
	_, _, w, h = draw.textbbox((0, 0), msg, font=font)
	draw.text(((W-w)/2, H-35), msg, font=font, fill=0)
	return img


arr = query_data_excel('file_to_gen.xlsx')
for i, v in enumerate(arr):
	data = v.split('|')
	# b64 = encode_64(v)
	img = gen_qrcode(v)
	re_img = add_text_below_img(img, data[4])
	re_img.save('qr_img/'+'meter_'+data[4]+'.png')


