import requests
import time


def zy_say_sentence_to_overweight(string="这是一段默认文本"):
    d = '{"msgtype": "text","text": {"content": "{0}"}' # 把"{0}"替换成发送的内容
    # d = '{"msgtype": "text","text": {"content": "{0}","mentioned_mobile_list":["@all"]}' # mentioned_mobile_list是需要艾特的人的手机号，可以替换成'@all' 表示艾特所有人
    
    s = string
    url1 = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=35680dae-ebc8-40e7-a3a9-2c0ea5797b55"
    n = 49
    while True:
        data1 = d.replace("{0}",s).encode("utf-8") # 发送前需要先编码，给过去的是一段二进制码
        r = requests.post(url = url1, data = data1) # post制定url，数据存data
        # print("n={},总长度为{}".format(str(n),str((n+1)*10)) ) # 用于测试最大长度，每次递增100直至发送失败
        print(r.text)
        break
        n = n+10
        time.sleep(3) # 限定每分钟只能发20条消息，所以多次发送的时候需要间隔3秒
        print(time.time())

def zy_say_paragraph_to_overweight(paragraph=["这是一段默认文本"]):
    with open('qywxapi_p.txt',encoding='utf-8') as f:
        paragraph = f.readlines()
    paragraph = map(lambda x:x.replace('\n',''), paragraph)
    for s in paragraph:
        #zy_say_sentence_to_overweight(string=s)
        print(s)
        time.sleep(3)
        

def zy_say_to_overweight_wordbyword():
    d = '{"msgtype": "text","text": {"content": "{0}","mentioned_mobile_list":[{1}]}' # 把"{0}"替换成发送的内容,"{1}"替换成要艾特的人
    with open("qywxapi_w.txt",encoding="utf-8") as f:
        s = f.read()
    o = 5000 # 最大长度是5100多，不超过这个数值即可
    
    mobile1 = "15555555555" # 可以替换成要艾特人的手机号
    mobile2 = "@all"
    d = d.replace("{1}", mobile2)
    
    for x in range(0,int( (len(s)-1) /o )+1):
        data1 = d.replace("{0}",s[x*o:x*o+o]).encode("utf-8")
        r = requests.post(url = url1, data = data1)
        print(r.text)
        time.sleep(1)
        print(time.time())

if __name__ == '__main__':
    zy_say_paragraph_to_overweight()
