# -*- coding: utf-8 -*-
from scrapy import cmdline
import os
import argparse

if __name__ == '__main__':
    # 解析命令行，获取从命令行输入的参数值。在pycharm的run/debug configuration中输入参数
    parser = argparse.ArgumentParser(description='运行指定爬虫')
    parser.add_argument('-p', '--project', type=str, help='爬虫项目,默认study_scrapy', default='study_scrapy')
    parser.add_argument('-s', '--spider', type=str, help='需要执行的爬虫名称', required=True)
    args = parser.parse_args()

    # 将参数值传入到命令中，从而可以启动爬虫
    # __file__ 是当前脚本文件
    # os.path.abspath(path) 返回path规范化的绝对路径
    # os.path.dirname(path) 返回path的目录
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    # 此处进入的目录是：D:\python_test\study_scrapy
    cmdline.execute(("scrapy crawl %s" % args.spider).split())