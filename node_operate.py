#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Node:
    'Good luck! Have fun!'

    node_data = []
    #用于存储读取的NODE编号和坐标
    a_line = []
    #用于存放文档所有数据
    ls = []
    le = []
    #ls,le用于记录a_line中Node的起始、结束位置

    def __init__(self, path):
    #类初始化，根据path读取指定的*.inp文件并提取参数        
        fo = open(path, 'r')
        #打开文件
        Node.a_line = fo.readlines()
        #遍历文档的数据
        for i in range(len(Node.a_line)):
            if Node.a_line[i].startswith('*NODE'):
                Node.ls = i+1
                #NODE数据开始行
                break
        for i in range(Node.ls,len(Node.a_line)):
            if Node.a_line[i].startswith('*'):
                Node.le = i
                #NODE数据结束行+1
                break
            Node.node_data.append(map(float,Node.a_line[i].split(',')))
            #将NODE数据读取转换后加入数组
        fo.close()
        
    def shift(self, node_id, dx=0, dy=0, dz=0):
    #类成员，根据提供的NODE编号和位移移动指定NODE
        if node_id == 'all':
            for i in range(0,Node.le-Node.ls):
                Node.node_data[i][1] += dx
                Node.node_data[i][2] += dy
                Node.node_data[i][3] += dz
                Node.a_line[i+Node.ls] = str(Node.node_data[i]).replace('[','').replace(']','\n')
        elif type(node_id) == list or type(node_id) == tuple:
            for i in range(node_id[0]-1,node_id[1]):
                Node.node_data[i][1] += dx
                Node.node_data[i][2] += dy
                Node.node_data[i][3] += dz
                Node.a_line[i+Node.ls] = str(Node.node_data[i]).replace('[','').replace(']','\n')
        elif type(node_id) == int:
                Node.node_data[node_id-1][1] += dx
                Node.node_data[node_id-1][2] += dy
                Node.node_data[node_id-1][3] += dz
                Node.a_line[node_id-1+Node.ls] = str(Node.node_data[node_id-1]).replace('[','').replace(']','\n')
        
    def set_nset(self, nset):
    #类成员，修改指定对象的NSET名称
        Node.a_line[Node.ls-1] = Node.a_line[Node.ls-1][0:Node.a_line[Node.ls-1].index('=')+1] + nset +'\n'
        
    def write(self, filepath):
    #类成员，把最后处理好的节点信息写入制定的inp中
        fw = open(filepath,'w')
        fw.writelines(Node.a_line)
        fw.close()
