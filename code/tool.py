#!/usr/bin/env python
# _*_ coding: utf-8 _*_
'''
Created on 2018-09-23 18:15:49
@author: wind
'''

import argparse
import os

parser = argparse.ArgumentParser(description="文件解析工具")
parser.add_argument('-s','--summary',action='store_true', default=False,help='是否更新SUMMARY内容')

args = parser.parse_args()
state = {k:v for k,v in args._get_kwargs()}

def get_markdown_list(name):
    result = "## %s"%name
    dir_base = 'content/%s/'%name
    g = os.walk(dir_base)
    for dirpath,dirnames,filenames in g:
        filenames = sorted(filenames)
        result += '\n'
        for filename in filenames:
            if filename.endswith('.md'):
                filepath = os.path.join(dirpath, filename)
                result += "* [{0}]({1})".format(filename[:-3],filepath)+'\n'

    return result

def write_content(file_handle,content):
    file_handle.write(content+'\n\n')

def create_summary():
    with open('./SUMMARY1.md','w',encoding='utf-8') as f:
        write_content(f,'# 目录')
        write_content(f,get_markdown_list("读书"))
        write_content(f,get_markdown_list("日记"))
        write_content(f,get_markdown_list("附加"))
    
if __name__ == '__main__':
    if args.summary:
        create_summary()


# 更新summary
# python code/tool.py -s