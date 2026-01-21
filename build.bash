#!/bin/bash

path=$(pwd)

# 品牌名称，可通过第一个参数覆盖
if [ $# -ge 1 ]; then
  case "$1" in
    -h|--help)
      echo "用法: $0 [品牌名称]"
      echo "生成指定品牌的字体文件。"
      echo "如果不提供参数，默认使用 'cengluan'。"
      exit 0
      ;;
    *)
      brand="$1"
      ;;
  esac
else
  brand="cengluan"
fi

# 创建必要的目录
mkdir -p $path/temp
mkdir -p $path/output

# 检查字体包是否已经存在
if [ ! -f "$path/temp/fusion-pixel-12px-monospaced-zh_hans.bdf" ]; then
  # 下载 fusion-pixel-12px-monospaced-zh_hans 的压缩包
  download_url="https://github.com/TakWolf/fusion-pixel-font/releases/download/2026.01.04/fusion-pixel-font-12px-monospaced-bdf-v2026.01.04.zip"
  wget "$download_url" -O $path/temp/font.zip

  # 检查下载是否成功
  if [ $? -ne 0 ]; then
    echo "错误: 下载文件失败。"
    exit 1
  fi

  # 解压下载的压缩包到 $path/temp
  unzip $path/temp/font.zip -d $path/temp

  # 检查解压是否成功
  if [ $? -ne 0 ]; then
    echo "错误: 解压文件失败。"
    exit 1
  fi

  # 列出解压后的目录内容
  ls $path/temp/
else
  echo "字体包已存在，跳过下载和解压。"
fi

# 运行 Python 脚本
python3 $path/build_font_from_bdf.py "$path/temp/fusion-pixel-12px-monospaced-zh_hans.bdf" > $path/output/$brand.txt
python3 $path/build_font_from_bdf_new.py "$path/temp/fusion-pixel-12px-monospaced-zh_hans.bdf" > $path/output/$brand-new.txt
# python3 $path/build_font_from_bdf.py "$path/temp/fusion-pixel-12px-monospaced-zh_hant.bdf" > $path/output/$brand-zh_hant.txt

# 检查脚本执行是否成功
if [ $? -ne 0 ]; then
  echo "错误: 运行 Python 脚本失败。"
  exit 1
fi

# 检查 psftools 是否已经编译
if [ ! -f "$path/temp/psftools-1.0.14/tools/txt2psf" ]; then
  # 下载并编译 psftools
  wget https://www.seasip.info/Unix/PSF/psftools-1.0.14.tar.gz -O $path/temp/psftools-1.0.14.tar.gz
  tar -xf $path/temp/psftools-1.0.14.tar.gz -C $path/temp/
  cd $path/temp/psftools-1.0.14 && \
  ./configure && \
  make
  if [ $? -ne 0 ]; then
    echo "错误: 下载并编译 psftools失败。"
    exit 1
  fi
  cd $path/
else
  echo "psftools 已编译，跳过下载和编译。"
fi

# 将 txt 文件转换为 psf 文件
$path/temp/psftools-1.0.14/tools/txt2psf $path/output/$brand.txt $path/output/$brand.psf
$path/temp/psftools-1.0.14/tools/txt2psf $path/output/$brand-new.txt $path/output/$brand-new.psf
# $path/temp/psftools-1.0.14/tools/txt2psf $path/output/$brand-zh_hant.txt $path/output/$brand-zh_hant.psf

# 检查转换是否成功
if [ $? -ne 0 ]; then
  echo "错误: 转换文件失败。"
  exit 1
fi

# 压缩 psf 文件
gzip -c $path/output/$brand.psf > $path/output/$brand.psfu.gz
gzip -c $path/output/$brand-new.psf > $path/output/$brand-new.psfu.gz
# gzip -c $path/output/$brand-zh_hant.psf > $path/output/$brand-zh_hant.psfu.gz

# 检查压缩是否成功
if [ $? -ne 0 ]; then
  echo "错误: 文件压缩失败。"
  exit 1
fi
