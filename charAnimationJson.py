# -*- coding:utf-8 -*-

import os
import sys
import time
import curses
import json

sys.path.append('..')
from common.tool import tool

class CharAnimation:

    def __init__(self, file_name, canvas_size):
        # 判断视频文件是否存在
        if not os.path.isfile(file_name):
            print('源文件未找到或不存在~')
            exit()

        # 字符列表，根据灰度值对应不同字符
        # self.ascii_char = list(''' .,-'`:!1+*abcdefghijklmnopqrstuvwxyz<>()\/{}[]?234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ%&@#$''')
        self.ascii_char = list(' $')

        # 接收视频文件名
        self.file_name = file_name

        # 图片文件路径、字符画文件路径
        self.pic_path = 'temp_pic'
        self.ascii_path = 'temp_ascii'

        # 画布宽、高
        self.resize_width, self.resize_height = map(int, canvas_size.split('*'))

    # 打印json文件内的字符画
    def print_chars_image(self):
        # 字符画文件路径
        json_path = os.path.join(self.ascii_path, self.file_name.split('.')[0] + '.json')
        # 判断字符画文件路径是否存在
        if os.path.exists(json_path):
            # 读取数据
            with open(json_path, 'r') as f:
                pic_list = json.load(f)
            # 初始化curses
            stdscr = curses.initscr()
            # 设置字体颜色
            curses.start_color()
            try:
                for code_pic in pic_list:
                    # 防止改变窗口大小停止播放
                    # 调整窗口大小，宽度最好大于字符画宽度。另外注意curses的height和width的顺序。
                    stdscr.resize(self.resize_height * 2, self.resize_width * 2)
                    # 打印code_pic(0, 0)表示从第0行的第0列开始写入，最后一个参数设置字符为白色
                    stdscr.addstr(0, 0, code_pic, curses.COLOR_WHITE)
                    stdscr.refresh()  # 写入后需要refresh才会立即更新界面
                    time.sleep(1 / 27.2)  # fps
            finally:
                # curses 使用前要初始化，用完后无论有没有异常，都要关闭
                curses.endwin()
        elif not os.path.exists(json_path):
            print('Error：Invalid directory.')

    def run(self):
        """
        > 运行流程：
            1、创建文件（图片文件、字符画文件、输出文件）
            2、将视频切割图片组
            3、将图片缩放、转ascii字符画，保存字符画
            4、打印字符画
        """
        tool.process_info(1, 4, '正在创建文件路径')
        tool.create_path(self.pic_path, self.ascii_path)
        tool.process_info(2, 4, '正在切割原视频为图片组')
        tool.videoConvertImage(self.file_name, self.pic_path)
        tool.process_info(3, 4, '正在处理分析图片，转ascii字符画 && 保存字符画')
        tool.save_chars_image(self.pic_path, self.file_name, self.resize_width, self.resize_height, self.ascii_char, self.ascii_path)
        tool.process_info(4, 4, '正在分析json文件，等待字符画显示')
        self.print_chars_image()


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('参数错误，请参考(python3 脚本 视频文件名 宽*高)：python3 videoChar.py test.mp4 90*40')
    else:
        CharAnimation(sys.argv[1], sys.argv[2]).run()
