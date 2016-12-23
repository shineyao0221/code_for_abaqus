#!/usr/bin/python
# -*- coding: UTF-8 -*-
class Node:
    """Good luck! Have fun!"""
    def __init__(self, input_path):   # 类初始化，根据path读取指定的*.inp文件并提取参数
        self.node_data = []
        fo = open(input_path, 'r')     # 打开文件
        self.inp_data = fo.readlines()  # 遍历文档的数据
        for i in range(len(self.inp_data)):
            if self.inp_data[i].startswith('*NODE'):
                self.ls = i+1       # NODE数据开始行
                break
        for i in range(self.ls, len(self.inp_data)):
            if self.inp_data[i].startswith('*'):
                self.le = i     # NODE数据结束行+1
                break
            temp_data = self.inp_data[i].split(',')
            self.node_data.append([int(temp_data[0]), float(temp_data[1]), float(temp_data[2]), float(temp_data[3])])
        fo.close()
        
    def shift(self, node_id, dx=0, dy=0, dz=0):  # 类成员，根据提供的NODE编号和位移移动指定NODE
        if node_id == 'all':    # 根据不同情况设定范围
            id_range = [0, self.le-self.ls]
        elif type(node_id) == list or type(node_id) == tuple:
            id_range = [node_id[0]-1, node_id[1]]
        elif type(node_id) == int:
            id_range = [node_id - 1, node_id]
        for i in range(id_range[0], id_range[1]):
            self.node_data[i][1] += dx
            self.node_data[i][2] += dy
            self.node_data[i][3] += dz
            self.inp_data[i+self.ls] = str(self.node_data[i]).replace('[', '').replace(']', '\n')

    def set_nset(self, nset):    # 类成员，修改指定对象的NSET名称
        self.inp_data[self.ls-1] = self.inp_data[self.ls-1][0:self.inp_data[self.ls-1].index('=')+1] + nset + '\n'
        # 将*NODE行第一个等号后的内容替换成节点组名字
        
    def write(self, output_path):  # 类成员，把最后处理好的节点信息写入制定的inp中
        fw = open(output_path, 'w')
        fw.writelines(self.inp_data)
        fw.close()