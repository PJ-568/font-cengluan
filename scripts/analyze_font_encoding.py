#!/usr/bin/env python3

# 分析字体文件中的编码映射

print("分析 ark-pixel-10px-monospaced-zh_cn.bdf 字体文件的编码...")

# 查找所有中文字符的编码
import subprocess
result = subprocess.run(
    ["grep", "-A", "1", "STARTCHAR u[456]", "temp/ark-pixel-10px-monospaced-zh_cn.bdf"],
    capture_output=True,
    text=True
)

lines = result.stdout.split('\n')
encodings = []
char_names = []

for i, line in enumerate(lines):
    if line.startswith('STARTCHAR'):
        char_name = line.split()[1]
        char_names.append(char_name)
    elif line.startswith('ENCODING'):
        encoding = int(line.split()[1])
        encodings.append(encoding)

print(f"找到 {len(encodings)} 个中文字符")
print("\n前20个字符的编码映射:")
for i in range(min(20, len(char_names))):
    char_name = char_names[i]
    encoding = encodings[i]
    # 提取 Unicode 码位
    if char_name.startswith('u'):
        unicode_hex = char_name[1:].split('-')[0]
        try:
            unicode_code = int(unicode_hex, 16)
            char = chr(unicode_code)
            print(f"  {char_name}: Unicode={unicode_code} ({char}), ENCODING={encoding}")
        except:
            print(f"  {char_name}: Unicode={unicode_hex} (?), ENCODING={encoding}")

# 检查是否有"啊"字
a_unicode = 0x554a  # "啊"的 Unicode 码位
print(f"\n查找'啊'字 (Unicode: {a_unicode}):")
found = False
for i, char_name in enumerate(char_names):
    if char_name.startswith('u554a') or f"u{a_unicode:04x}" in char_name.lower():
        print(f"  找到: {char_name}, ENCODING={encodings[i]}")
        found = True

if not found:
    print("  字体文件中没有找到'啊'字")
    
    # 查找编码范围
    print(f"\n编码范围分析:")
    print(f"  最小编码: {min(encodings)}")
    print(f"  最大编码: {max(encodings)}")
    print(f"  编码数量: {len(encodings)}")
    
    # 查看是否有连续的编码
    sorted_encodings = sorted(encodings)
    gaps = []
    for i in range(1, len(sorted_encodings)):
        if sorted_encodings[i] - sorted_encodings[i-1] > 1:
            gaps.append((sorted_encodings[i-1], sorted_encodings[i]))
    
    if gaps:
        print(f"  编码不连续，有 {len(gaps)} 个间隙")
        print(f"  前5个间隙: {gaps[:5]}")
    else:
        print("  编码是连续的")