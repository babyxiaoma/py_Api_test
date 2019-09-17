# -*- coding: utf-8 -*-
#!/usr/bin/python

#@Author     :xiao hei ma
#@Time       :2019-08-30 13:38:05
#@File       :test1313.py
#@Ide        :PyCharm


import requests



url = " https://api.hydw99.com/platform/games?api_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1Njg2ODkxOTMsImV4cCI6MTU2ODczMjM5MywiaXNzIjoiYm9uZyIsInN1YiI6Nn0.zzrbhgSfrAdMsfHQXEEKjowh65wTi-PALmWKvX1ZkgE"
data = []
response = requests.get(url).json()
for i in response['data']['AGIN']:
    name = i['name']
    data.append(name)
print(data)
print(",".join(data))
print(len(data))

data1 = ['抢庄牛牛', '炸金花', '三公', '看牌抢庄牛牛', '捕鱼达人', '金鲨银鲨', '金拉霸进入游戏使用', '二八杠', '押庄龙虎', '百家乐', '糖果派对2', '二人麻将', '糖果派对', '开心消消乐', '糖果派对3', '连环夺宝2', '连环夺宝', '财神捕鱼', '龙王捕鱼', '龙王捕鱼2', '芝麻开门', '加多宝变脸', '德州扑克', '21点', '通比牛牛', '极速炸金花', '抢庄牌九', '十三水', '斗地主', '森林舞会', '百人牛牛', '奔驰宝马', '百搭777-入游戏使用', '金龙珠进入游戏使用', '猛龙传奇进入游戏使用', '魅惑魔女进入游戏', '芝麻开门2']



# url = "http://47.91.245.176/index/games"
# data = {
#     'api_token':"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NjgyNzc3NDMsImV4cCI6MTU2ODMyMDk0MywiaXNzIjoiYm9uZyIsInN1YiI6MTczMDQyfQ.84qeETO9nHp0WDqxkvHyY1LZo2i4z9wfTBsQ2bAqg-0",
#     'platform':"JDB",
#     "type":"1"
# }
# _list = []
# response = requests.post(url,data).json()
# for i in response['data']:
#     _list.append(i['name'])
# print(_list)

