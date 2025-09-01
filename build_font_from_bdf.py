#!/usr/bin/env python3

# 导入所需的库
from bdflib import reader

# 读取 BDF 格式的字体文件
font = reader.read_bdf(open("temp/wqy-bitmapsong/wenquanyi_9pt.bdf", "rb"))

# File format version; currently this must be 0.
version = '0'

# 定义字体的高度和宽度
height = 13
width = 12

# 定义垂直偏移量
v_offset = -2

# 初始化计数器
count = 0

print(f'''%PSF2
Version: {version}
Flags: 1
Length: 512
Width: {width}
Height: {height}''', end='')

def PrintNonChineseCharacter(index):
    count = index
    # 输出空格
    PrintCharacters('              　', count)
    count += 1

    # 打开包含其他字符的参考文件
    with open("original/references/other_characters", encoding="utf-8") as f:
        for lines in f:
            line = lines.split()
            PrintCharacters(line[0], count)
            count += 1
    return count

def PrintCharacters(Characters, count):
    Character = Characters[0]
    try:
        # 将汉字编码为对应编码
        encoding = "utf-8"
        # _enc = codecs.encode(Character, encoding=encoding)
        # 获取对应的字形：即取 ENCODING 变量为字的 Unicode 编码的字形，不同字体中，ENCODING 变量数值的含义可能不同
        try:
            glyph = font[ord(Character)]
        except KeyError:
            print(f"警告：字符“{Character}”的 {encoding} 编码：“{ord(Character)}”无法在文件中找到。")
            exit(1)

        print("\n%")
        print("//", count, Character)

        # 打印字形的位图表示
        print("Bitmap: ", end="")
        o_pixels = [[y for y in x] for x in glyph.iter_pixels()]
        [left, bottom, w, h] = glyph.get_bounding_box()

        # 初始化一个空的像素矩阵
        pixels = [["-" for j in range(0, width)] for i in range(0, height)]

        # 填充像素矩阵
        for i in range(0, h):
            for j in range(0, w):
                pixels[-bottom - h + i + v_offset][left + j] = ("#" if o_pixels[i][j] else "-")

        # 打印像素矩阵
        for l in range(0, height):
            ll = "".join(pixels[l])
            if l < height - 1:
                ll = ll + " \\"
            print(ll)

        # 打印汉字的 Unicode 编码
        print("Unicode: ", end="")
        for h in Characters:
            # 遇到 # 则停止
            if h == "#":
                break
            print("[{0:08x}];".format(ord(h)), end="")

    except UnicodeError:
        # 捕获并处理 Unicode 错误
        pass

# 打开包含拼音和对应汉字的参考文件
with open("original/references/pinyin_hanzi", encoding="utf-8") as f:
    count = 0
    for line in f:
        if count == 32:
            count = PrintNonChineseCharacter(count)
        # 跳过注释行
        if line.startswith("#"):
            continue
        s = line.split()
        if len(s) >= 2:
            hanzis = s[1]
            PrintCharacters(hanzis, count)
            count += 1
