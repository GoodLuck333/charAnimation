# charAnimation 

### 【字符动画】(python版)
在线预览: https://goodluck333.github.io/charAnimation/temp_out/badApple.html

---

#### 前置需求

* ffmpeg -- FFmpeg是一个自由软件，可以运行音频和视频多种格式的录影、转换、流功能。这是一个用于多个项目中音频和视频的解码器库，以及libavformat，一个音频与视频格式转换库。

  下载移步官网: http://ffmpeg.org/

* PIL -- PIL是Python平台事实上的图像处理标准库，支持多种格式，并提供强大的图形与图像处理功能。PIL并不支持python3，因此我们用pillow代替，敲入以下代码进行安装
```
  pip3 install pillow
```

#### 简介

* 目前写了三种有所区别的版本：【Print版】【JSON版】【Html版】

* 主要使用ffmpeg将视频以帧的形势转换成图片，将图片灰度化，根据灰度值决定该像素位置的字符

#### 【Print版介绍】

1. 创建临时图片文件夹
2. 使用ffmpeg将视频切割图片组，将切割好的图片组保存到临时图片文件夹
3. 将图片缩放、灰度化转ascii字符画，控制好时间打印每张字符画

##### 使用方法

> python3 脚本 视频文件名 宽*高
> 
> 例: python3 charAnimationPrint.py test.mp4 90*40

#### 【JSON版介绍】

1. 创建文件夹（临时图片文件夹、JSON文件夹）
2. 使用ffmpeg将视频切割图片组，将切割好的图片组保存到临时图片文件夹
3. 将图片缩放、灰度化转ascii字符画，把每张字符画保存到JSON文件
4. 读取JSON文件内数据，控制好时间打印每张字符画

##### 使用方法

> python3 脚本 视频文件名 宽*高
> 
> 例: python3 charAnimationJson.py test.mp4 90*40

#### 【Html版介绍】

1. 创建文件夹（临时图片文件夹、JSON文件夹、输出文件夹）
2. 使用ffmpeg将视频切割图片组，将切割好的图片组保存到临时图片文件夹
3. 将图片缩放、灰度化转ascii字符画，把每张字符画保存到JSON文件
4. 生成Html文件保存到输出文件夹，在Html展示字符动画及源视频

##### 使用方法

> python3 脚本 视频文件名 宽*高
> 
> 例: python3 charAnimationHTML.py test.mp4 90*40

  Print版属于执行中打印，电脑的执行效率可能会影响到打印效果。而且效果只能在当前终端展示，具有一定的局限性。
  
  JSON、Html版都属于生成文件打印，如果有其它地方需要使用，都可直接调用文件数据。但同样会有一些问题，如果画布太大也会导致生成文件过大，生成等待时间过长，加载起来也会很慢长。（注: Html使用JSONP方法，方法名为cb）

                                                                                    By:GoodLuck333
