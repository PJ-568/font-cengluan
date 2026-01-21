#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
将文本文件中每一行的第二个字符移动到行首
"""

import sys
import os

def switch_first_two_chars(line):
    """
    将字符串的第二个字符移动到行首
    
    Args:
        line: 输入字符串（不含换行符）
    
    Returns:
        转换后的字符串
    """
    if len(line) < 2:
        return line
    
    # 第二个字符移动到行首
    return line[1] + line[0] + line[2:]

def process_file(file_path):
    """
    处理文件，将每一行的第二个字符移动到行首
    
    Args:
        file_path: 文件路径
    
    Returns:
        bool: 是否成功
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        new_lines = []
        modified_count = 0
        
        for line in lines:
            # 去除末尾换行符
            stripped = line.rstrip('\n')
            # 保留原始行结束符（可能是\r\n或其他）
            line_ending = line[len(stripped):] if len(line) > len(stripped) else ''
            
            if len(stripped) >= 2:
                new_stripped = switch_first_two_chars(stripped)
                new_lines.append(new_stripped + line_ending)
                if new_stripped != stripped:
                    modified_count += 1
            else:
                new_lines.append(line)
        
        # 写回文件
        with open(file_path, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)
        
        print(f"✅ 处理完成：修改了 {modified_count} 行")
        return True
        
    except UnicodeDecodeError:
        print(f"错误：无法读取文件 {file_path}，请检查文件编码是否为 UTF-8")
        return False
    except FileNotFoundError:
        print(f"错误：文件 {file_path} 不存在")
        return False
    except PermissionError:
        print(f"错误：没有权限写入文件 {file_path}")
        return False
    except Exception as e:
        print(f"错误：处理文件时发生异常：{e}")
        return False

def main():
    if len(sys.argv) != 2:
        print("用法: python3 switch_1_2.py <文件路径>")
        print("将文本文件中每一行的第二个字符移动到行首")
        return 1
    
    file_path = sys.argv[1]
    
    if not os.path.exists(file_path):
        print(f"错误：文件 {file_path} 不存在")
        return 1
    
    if os.path.isdir(file_path):
        print(f"错误：{file_path} 是一个目录，不是文件")
        return 1
    
    print(f"正在处理文件：{file_path}")
    print("将每一行的第二个字符移动到行首...")
    print("-" * 50)
    
    success = process_file(file_path)
    
    if not success:
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())
