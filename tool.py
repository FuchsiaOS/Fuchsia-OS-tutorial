import base64
f=open('./3.jpg','rb')
ls_f=base64.b64encode(f.read())
f.close()
print(ls_f)
