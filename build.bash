#!/bin/bash

path=$(pwd)

# 创建必要的目录
mkdir -p $path/temp
mkdir -p $path/output

# 下载 wqy-bitmapsong-bdf-1.0.0-RC1 的压缩包
download_url="https://downloads.sourceforge.net/project/wqy/wqy-bitmapfont/1.0.0-RC1/wqy-bitmapsong-bdf-1.0.0-RC1.tar.gz"
wget "$download_url" -O $path/temp/wqy-bitmapsong-bdf-1.0.0-RC1.tar.gz

# 检查下载是否成功
if [ $? -ne 0 ]; then
    echo "错误: 下载文件失败。"
    exit 1
fi

# 解压下载的压缩包
tar -xf $path/temp/wqy-bitmapsong-bdf-1.0.0-RC1.tar.gz -C $path/temp/

# 检查解压是否成功
if [ $? -ne 0 ]; then
    echo "错误: 解压文件失败。"
    exit 1
fi

# 列出解压后的目录内容
ls $path/temp/wqy-bitmapsong/

# 运行 Python 脚本
python3 $path/build_font_from_bdf.py > $path/output/xibo.txt

# 检查脚本执行是否成功
if [ $? -ne 0 ]; then
    echo "错误: 运行 Python 脚本失败。"
    exit 1
fi

# 下载并编译 psftools
wget https://www.seasip.info/Unix/PSF/psftools-1.0.14.tar.gz -O $path/temp/psftools-1.0.14.tar.gz
tar -xf $path/temp/psftools-1.0.14.tar.gz -C $path/temp/
cd $path/temp/psftools-1.0.14
./configure
make
cd $path/

# 检查压缩是否成功
if [ $? -ne 0 ]; then
    echo "错误: 下载并编译 psftools失败。"
    exit 1
fi

# 将 txt 文件转换为 psf 文件
$path/temp/psftools-1.0.14/tools/txt2psf $path/output/xibo.txt $path/output/xibo.psf

# 检查转换是否成功
if [ $? -ne 0 ]; then
    echo "错误: 转换文件失败。"
    exit 1
fi

# 压缩 psf 文件
gzip -c $path/output/xibo.psf > $path/output/xibo.psfu.gz

# 检查压缩是否成功
if [ $? -ne 0 ]; then
    echo "错误: 文件压缩失败。"
    exit 1
fi