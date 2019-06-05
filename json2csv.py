#-*-coding:utf-8-*-
import csv
import json
import sys
import codecs

def trans(path):
    jsonData = codecs.open(path+'.json', 'r', 'utf-8')
    # csvfile = open(path+'.csv', 'w') # 此处这样写会导致写出来的文件会有空行
    # csvfile = open(path+'.csv', 'wb') # python2下
    csvfile = open(path+'.csv', 'w', newline='') # python3下
    writer = csv.writer(csvfile)
    flag = True  
    json_data= json.load(jsonData)
    print(json_data[0]["_index"])
    for index, item in enumerate(json_data):
         try:
             id = item["_source"]["layers"]["frame"]["frame.number"]
             data = item["_source"]["layers"]["data-text-lines"]
             print(data)
             print(index)
             writer.writerow([id,str(data)])
         except KeyError:
             id = item["_source"]["layers"]["frame"]["frame.number"]
             print("err:",id)
             data = item["_source"]["layers"]["websocket"]
             print(data)
             writer.writerow([id,str(data)])
             pass
         continue

    # for line in jsonData:
    #     dic = json.loads(line[0:-1])
    #     if flag:
    #         # 获取属性列表
    #         keys = list(dic.keys())
    #         print (keys)
    #         writer.writerow(keys) # 将属性列表写入csv中
    #         flag = False
    #     # 读取json数据的每一行，将values数据一次一行的写入csv中
    #     writer.writerow(list(dic.values()))
    jsonData.close()
    csvfile.close()

if __name__ == '__main__':
    path=str(sys.argv[1]) # 获取path参数
    print (path)
    trans(path)
