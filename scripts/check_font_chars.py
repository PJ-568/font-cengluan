#!/usr/bin/env python3

from bdflib import reader

# 尝试用不同的方式读取 BDF 格式的字体文件
try:
    # 尝试文本模式读取
    with open("temp/ark-pixel-10px-monospaced-zh_cn.bdf", "r", encoding="utf-8") as f:
        font = reader.read_bdf(f)
    print("使用文本模式 UTF-8 编码读取成功")
except Exception as e:
    print(f"文本模式读取失败: {e}")
    try:
        # 尝试二进制模式读取
        with open("temp/ark-pixel-10px-monospaced-zh_cn.bdf", "rb") as f:
            font = reader.read_bdf(f)
        print("使用二进制模式读取成功")
    except Exception as e2:
        print(f"二进制模式读取也失败: {e2}")
        exit(1)

# 获取字体中的所有字符编码
font_chars = {}
for glyph in font.glyphs:  # 注意这里是属性不是方法
    if hasattr(glyph, 'encoding'):
        font_chars[glyph.encoding] = glyph

print(f"字体文件总字符数: {len(font_chars)}")

# 检查字体中中文字符的编码范围
chinese_codes = [code for code in font_chars.keys() if 19968 <= code <= 40959]
if chinese_codes:
    print(f"字体中中文字符编码范围: {min(chinese_codes)} - {max(chinese_codes)}")
    print(f"字体中中文字符总数: {len(chinese_codes)}")
    print(f"前10个中文字符编码: {chinese_codes[:10]}")
else:
    print("字体中没有找到中文字符！")

# 检查具体的"啊"字符
a_code = ord('啊')
print(f"\n检查字符'啊' (Unicode: {a_code}):")
if a_code in font_chars:
    print("  字体中包含'啊'字符")
else:
    print("  字体中不包含'啊'字符")
    # 查看字体中编码相近的字符
    nearby_codes = [code for code in font_chars.keys() if 21000 <= code <= 23000]
    print(f"  字体中编码在21000-23000范围的字符: {nearby_codes[:10]}...")