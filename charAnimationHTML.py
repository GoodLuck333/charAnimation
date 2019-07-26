# -*- coding:utf-8 -*-

import os
import sys

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

        # 图片文件路径、字符画文件路径、输出文件路径
        self.pic_path = 'temp_pic'
        self.ascii_path = 'temp_ascii'
        self.out_path = 'temp_out'

        # 画布宽、高
        self.resize_width, self.resize_height = map(int, canvas_size.split('*'))

    # 生成html
    def createHTML(self):
        # HTML文件名
        file_name = self.file_name.split('.')[0]
        # 路径
        path = f'{self.out_path}/{file_name}.html'
        html_code = \
        ('<html>\n'
        '   <head></head>\n'
        '   <style>\n'
        '       * {\n'
        '           padding: 0;\n'
        '           margin: 0;\n'
        '       }\n'
        '       #chars_image {\n'
        '           display: inline-block;\n'
        '           width: 49%;\n'
        '           font-size: 10px;\n'
        '           line-height: 14px;\n'
        '       }\n'
        '   </style>\n'
        '   <body>\n'
        '       <pre id="chars_image"></pre>\n'
       f'      <video id="video" width="49%" src="../{self.file_name}" autobuffer autoplay muted>\n'
        '           <div>\n'
        '               <p>You must have an HTML5 capable browser.</p>\n'
        '           </div>\n'
        '       </video>\n'
        '       <script type="text/javascript">\n'
        '           window.requestAnimationFrame = window.requestAnimationFrame || window.mozRequestAnimationFrame || window.webkitRequestAnimationFrame || window.msRequestAnimationFrame;\n'
        '           let cb = (result) => {\n'
        '               let chars_image = document.getElementById("chars_image"),\n'
        '                   i = 0\n'
        '               run = () => {\n'
        '                   if (i >= result.length) {\n'
        '                       clearTimeout(timer)\n'
        '                   } else {\n'
        '                       chars_image.innerHTML = result[i]\n'
        '                       timer = setTimeout(run, 40)\n'
        '                   }\n'
        '                   i++;\n'
        '               }\n'
        '               timer = setTimeout(run, 0)\n'
        '           }\n'
        '       </script>\n'
       f'       <script type="text/javascript" src="../{self.ascii_path}/{file_name}Html.json?callback=cb"></script>\n'
        '   </body>\n'
        '</html>')
        try:
            with open(path, 'w') as f:
                # 写入html
                f.write(html_code)
            print('html生成成功！')
        except Exception as e:
            print(e)

    def run(self):
        """
        > 运行流程：
            1、创建文件（图片文件、字符画文件、输出文件）
            2、将视频切割图片组
            3、将图片缩放、转ascii字符画，保存字符画
            4、生成html文件
        """
        tool.process_info(1, 4, '正在创建文件路径')
        tool.create_path(self.pic_path, self.ascii_path, self.out_path)
        tool.process_info(2, 4, '正在切割原视频为图片组')
        tool.videoConvertImage(self.file_name, self.pic_path)
        tool.process_info(3, 4, '正在处理分析图片，转ascii字符画 && 保存字符画')
        tool.save_chars_image(self.pic_path, self.file_name, self.resize_width, self.resize_height, self.ascii_char, self.ascii_path, True)
        tool.process_info(4, 4, '正在分析json文件，等待生成html文件')
        self.createHTML()


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('参数错误，请参考(python3 脚本 视频文件名 宽*高)：python3 videoChar.py test.mp4 90*40')
    else:
        CharAnimation(sys.argv[1], sys.argv[2]).run()
