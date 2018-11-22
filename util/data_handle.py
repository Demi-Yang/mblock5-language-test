#encoding:utf-8
import sys

#======================== 数据编码处理 ========================   
#将dict里的unicode转成utf-8编码，解决中文转码问题（遍历）
def byteify(input):
    if isinstance(input, dict):
        return {byteify(key): byteify(value) for key, value in input.iteritems()}
    elif isinstance(input, list):
        return [byteify(element) for element in input]
    elif isinstance(input, unicode):
        return input.encode('utf-8')
    else:
        #print('data_handle:', sys.path)
        return input
    