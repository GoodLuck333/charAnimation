# -*- coding:utf-8 -*-

from PIL import Image
import os
import shutil
import json

class Tool:

    # 流程信息
    def process_info(self, i, n, info):
        print('-' * 60)
        print(f'[{i}/{n}]{info}...')
        print('-' * 60 + '\r\n')

    # 进度条
    def progress_bar(self, current, total, len, text):
        # 已进行进度调整
        current += 1
        # 已运行进度值
        pro_num = int((current / total) * len)
        # 已运行百分比
        precent = (current / total) * 100
        print('\r' + '>' * pro_num + '.' * (len - pro_num) + f' {precent:.2f}%（{current}/{total}) - {text}', end = '')

    # 创建文件（图片文件、字符画文件、输出文件）
    def create_path(self, pic_path, ascii_path = '', out_path = ''):
        # 创建图片文件
        if not os.path.exists(pic_path):
            os.makedirs(pic_path)
        else:
            # 删除文件重新创建
            shutil.rmtree(pic_path)
            os.makedirs(pic_path)
        print('图片文件   已完成')

        if ascii_path:
            # 创建字符画文件
            if not os.path.exists(ascii_path):
                os.makedirs(ascii_path)
            else:
                # 删除文件重新创建
                shutil.rmtree(ascii_path)
                os.makedirs(ascii_path)
            print('字符画文件 已完成')

        if out_path:
            # 创建输出文件
            if not os.path.exists(out_path):
                os.makedirs(out_path)
            print('输出文件   已完成\n')

    # 视频分割图片
    def videoConvertImage(self, file_name, pic_path):
        # cmd：ffmpeg -i [输入文件名] -r [fps,帧率] [分割图存储路径]
        # 使用ffmpeg切割图片，命令行如下
        cmd = f'ffmpeg -i {file_name} -r 24 {pic_path}/%06d.jpeg'
        # 执行命令
        os.system(cmd)

    # 图片缩放、转ascii字符画
    def imageConvertAscii(self, pic_path, pic, resize_width, resize_height, ascii_char):
        # 图片完整路径
        img_path = os.path.join(pic_path, pic)
        if os.path.exists(img_path):
            try:
                # 打开图片，获取图片对象
                origin_img = Image.open(img_path)
            except Exception as e:
                origin_img = None
                print(e)
            if not origin_img == None:
                # 图片重置大小且灰度化
                resize_img = origin_img.resize((resize_width, resize_height), Image.ANTIALIAS).convert("L")
                # 字符集数量
                ascii_char_len = len(ascii_char)
                # ascii字符画
                code_pic = ''
                for h in range(resize_height):
                    for w in range(resize_width):
                        # 获取当前坐标的像素值
                        gray = resize_img.getpixel((w, h))
                        # 添加该灰度值所对应字符
                        code_pic += ascii_char[int(ascii_char_len * gray / 256)]
                    # 行末添加换行符
                    code_pic += '\n'
                return code_pic
        elif not os.path.exists(img_path):
            print('Error：Invalid directory.')

    # 保存字符画数据
    def save_chars_image(self, pic_path, file_name, resize_width, resize_height, ascii_char, ascii_path, type = False):
        # 升序排列图片目录
        pic_list = sorted(os.listdir(pic_path))
        # 图片数量
        pic_len = len(pic_list)
        # 计数器
        count = 1
        # json数据
        json_data = []
        for pic in pic_list:
            # 图片缩放、转ascii字符画
            code_pic = tool.imageConvertAscii(pic_path, pic, resize_width, resize_height, ascii_char)
            # json数据添加字符画
            json_data.append(code_pic)
            # 提示信息
            tool.progress_bar(count, pic_len, 30, pic)
            count += 1
        print()
        # 保存字符画json数据
        with open(os.path.join(ascii_path, file_name.split('.')[0] + '.json'), 'w') as f:
            # dict类型的数据转成str并写入
            f.write(json.dumps(json_data))
        if type:
            # 保存HTML需要的json数据
            with open(os.path.join(ascii_path, file_name.split('.')[0] + 'Html.json'), 'w') as f:
                # dict类型的数据转成str并写入
                f.write('cb(' + json.dumps(json_data) + ')')
        print('字符画保存成功！')

tool = Tool()
