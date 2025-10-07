#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
自动去除 other_characters 文件中的重复字符，只保留重复字符中的第一个
"""

import os
import shutil

def remove_duplicate_characters(file_path):
    """
    去除文件中每行的重复字符，只保留第一个出现的字符
    
    Args:
        file_path: 文件路径
    
    Returns:
        tuple: (是否修改过, 修改的行数)
    """
    modified = False
    modified_lines = 0
    
    try:
        # 创建备份
        # backup_path = file_path + '.backup'
        # shutil.copy2(file_path, backup_path)
        # print(f"已创建备份文件：{backup_path}")
        
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        new_lines = []
        
        for line_num, line in enumerate(lines, 1):
            original_line = line.strip()
            if not original_line:
                new_lines.append(line)
                continue
                
            # 去除重复字符，只保留第一个
            seen_chars = set()
            new_line_chars = []
            
            for char in original_line:
                if char not in seen_chars:
                    seen_chars.add(char)
                    new_line_chars.append(char)
                else:
                    modified = True
            
            new_line = ''.join(new_line_chars) + '\n'
            new_lines.append(new_line)
            
            if len(new_line_chars) != len(original_line):
                modified_lines += 1
                print(f"第 {line_num} 行：去除 {len(original_line) - len(new_line_chars)} 个重复字符")
        
        # 写入修改后的内容
        with open(file_path, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)
            
    except UnicodeDecodeError as e:
        print(f"错误：无法读取文件 {file_path}，编码问题：{e}")
        return False, 0
    except FileNotFoundError:
        print(f"错误：文件 {file_path} 不存在")
        return False, 0
    except Exception as e:
        print(f"错误：处理文件时发生异常：{e}")
        return False, 0
    
    return modified, modified_lines

def main():
    file_path = 'original/references/other_characters'
    
    print("正在去除文件中的重复字符...")
    print(f"文件路径：{file_path}")
    print("-" * 50)
    
    if not os.path.exists(file_path):
        print(f"错误：文件 {file_path} 不存在")
        return 1
    
    modified, modified_lines = remove_duplicate_characters(file_path)
    
    if not modified:
        print("✅ 文件中没有需要去除的重复字符")
    else:
        print(f"✅ 已完成：修改了 {modified_lines} 行，去除了重复字符")
        print()
        print("验证修改结果...")
        
        # 运行检查脚本验证
        import subprocess
        try:
            result = subprocess.run(['python3', 'scripts/check_duplicate_chars.py'], 
                                  capture_output=True, text=True)
            
            if result.returncode == 0:
                print("✅ 验证通过：文件中已无重复字符")
            else:
                print("❌ 验证失败：文件中仍有重复字符")
                print(result.stdout)
                return 1
        except Exception as e:
            print(f"警告：无法运行验证脚本：{e}")
    
    return 0

if __name__ == "__main__":
    exit(main())