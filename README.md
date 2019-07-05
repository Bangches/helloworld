# zy_new_and_old

系统环境 windows x64
编程语言 python37

涉及模块
time 自带模块
requests 非自带，可使用pip安装
系统功能：

1、名称：zy_say_sentence_to_overweight
实现功能：把参数
参数：
（1）string：字符串，长度不限，不超过5100
（2）url：发送机器人的url，可以自行修改
（3）d：第一个d为直接发送，第二个d可以艾特别人，如需使用，把第二个d取消注释，然后把要艾特的人的手机号以字符串的形式填写在mentioned_mobile_list中

2、名称：zy_say_paragraph_to_overweight
实现功能：把参数文件中的文字，以'\n'（windows环境下的回车符）为分割，逐行发送
参数：
（1）文件：文件名必须为qywxapi_p.txt，以utf-8编码，放在py文件同目录下
其他说明：艾特功能与1相同

3、名称：zy_say_to_overweight_wordbyword
实现功能：把参数文件中的，
参数：
（1）文件：文件名必须为qywxapi_w.txt，以utf-8编码，放在py文件同目录下
（2）o：正整数值，建议1-5000，表示每次发送文字的长度，例如文件共2005字，o=100，则会拆分成21次发送
（3）url：同1-（2）
其他说明：把参数文件中的文字，每次发送o个文字，依次发送发完为止

备注：
zy_say_sentence_to_overweight和zy_say_to_overweight_wordbyword中的url不同，可自行修改
zy_say_paragraph_to_overweight中的url会使用zy_say_sentence_to_overweight的url
