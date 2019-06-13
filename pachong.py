import requests
Url = "http://img0.ph.126.net/WPoHgfhyqEjUG_HP2AK7ow==/6631872608210454282.jpg"   #请求图片的url
imgresponse = requests.get(Url, stream=True)   #以流的方式打开
image = imgresponse.content
address="E:"+"\\"   #保存地址
try:
    with open(address+"6631872608210454282.jpg" ,"wb") as jpg:
        jpg.write(image)
except IOError:
    print("IO Error\n")
finally:
    jpg.close()

