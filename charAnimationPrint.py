# -*- coding:utf-8 -*-

import os
import sys
import time
import curses

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

        # 图片文件路径
        self.pic_path = 'temp_pic'

        # 画布宽、高
        self.resize_width, self.resize_height = map(int, canvas_size.split('*'))

    # 图片转换字符画 && 终端显示
    def convert_print(self):
        # 升序排列图片目录
        pic_list = sorted(os.listdir(self.pic_path))
        # 初始化curses
        stdscr = curses.initscr()
        # curses字体颜色
        curses.start_color()
        try:
            for pic in pic_list:
                # 防止改变窗口大小停止播放
                # 调整窗口大小，宽度最好大于字符画宽度。另外注意curses的height和width的顺序。
                stdscr.resize(self.resize_height * 2, self.resize_width * 2)
                # 图片缩放、转ascii字符画
                code_pic = tool.imageConvertAscii(self.pic_path, pic, self.resize_width, self.resize_height, self.ascii_char)
                # 打印code_pic(0, 0)表示从第0行的第0列开始写入，最后一个参数设置字符为白色
                stdscr.addstr(0, 0, code_pic, curses.COLOR_WHITE)
                stdscr.refresh()  # 写入后需要refresh才会立即更新界面
                time.sleep(1 / 50)  # fps
        finally:
            # curses 使用前要初始化，用完后无论有没有异常，都要关闭
            curses.endwin()

    def run(self):
        """
        > 运行流程：
            1、创建文件（图片文件、字符画文件、输出文件）
            2、使用ffmpeg将视频切割图片组
            3、将图片缩放、转ascii字符画，打印字符画
        """
        tool.process_info(1, 3, '正在创建文件路径')
        tool.create_path(self.pic_path)
        tool.process_info(2, 3, '正在切割原视频为图片组')
        tool.videoConvertImage(self.file_name, self.pic_path)
        tool.process_info(3, 3, '正在处理分析图片，转ascii字符画 && 字符画显示')
        self.convert_print()


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('参数错误，请参考(python3 脚本 视频文件名 宽*高)：python3 videoChar.py test.mp4 90*40')
    else:
        CharAnimation(sys.argv[1], sys.argv[2]).run()
