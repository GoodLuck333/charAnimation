# charAnimation 

### 【字符动画】(python版)
在线预览: https://goodluck333.github.io/charAnimation/temp_out/badApple.html

---

#### 前置需求

ffmpeg -- FFmpeg是一个自由软件，可以运行音频和视频多种格式的录影、转换、流功能。这是一个用于多个项目中音频和视频的解码器库，以及libavformat，一个音频与视频格式转换库。
下载移步官网: http://ffmpeg.org/

PIL -- PIL是Python平台事实上的图像处理标准库，支持多种格式，并提供强大的图形与图像处理功能。PIL并不支持python3，因此我们用pillow代替，敲入以下代码进行安装
```
  pip3 install pillow
```

#### 简介

目前写了三种有所区别的版本：【Print版】【JSON版】【Html版】

主要使用ffmpeg将视频以帧的形势转换成图片，将图片灰度化，根据灰度值决定该像素位置的字符

#### 【Print版介绍】

1. 创建临时图片文件夹
2. 使用ffmpeg将视频切割图片组，将切割好的图片组保存到临时图片文件夹
3. 将图片缩放、灰度化转ascii字符画，控制好时间打印每张字符画

##### 使用方法

python3 脚本 视频文件名 宽*高

例: python3 charAnimationPrint.py test.mp4 90*40

#### 【JSON版介绍】

1. 创建文件夹（临时图片文件夹、JSON文件夹）
2. 使用ffmpeg将视频切割图片组，将切割好的图片组保存到临时图片文件夹
3. 将图片缩放、灰度化转ascii字符画，把每张字符画保存到JSON文件
4. 读取JSON文件内数据，控制好时间打印每张字符画

##### 使用方法

python3 脚本 视频文件名 宽*高

例: python3 charAnimationJson.py test.mp4 90*40

#### 【Html版介绍】

1. 创建文件夹（临时图片文件夹、JSON文件夹、输出文件夹）
2. 使用ffmpeg将视频切割图片组，将切割好的图片组保存到临时图片文件夹
3. 将图片缩放、灰度化转ascii字符画，把每张字符画保存到JSON文件
4. 生成Html文件保存到输出文件夹，在Html展示字符动画及源视频

##### 使用方法

python3 脚本 视频文件名 宽*高

例: python3 charAnimationHTML.py test.mp4 90*40
