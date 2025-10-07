#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
检查 other_characters 文件中每行是否存在重复字符
"""

def check_duplicate_characters(file_path):
    """
    检查文件中每行是否存在重复字符
    
    Args:
        file_path: 文件路径
    
    Returns:
        tuple: (是否有重复, 重复行的详细信息)
    """
    has_duplicates = False
    duplicate_lines = []
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        for line_num, line in enumerate(lines, 1):
            line = line.strip()
            if not line:
                continue
                
            # 检查每个字符是否重复
            char_count = {}
            duplicates = []
            
            for char in line:
                if char in char_count:
                    char_count[char] += 1
                else:
                    char_count[char] = 1
            
            # 找出重复的字符
            for char, count in char_count.items():
                if count > 1:
                    duplicates.append(f"'{char}' (出现 {count} 次)")
            
            if duplicates:
                has_duplicates = True
                duplicate_lines.append({
                    'line_number': line_num,
                    'line_content': line,
                    'duplicates': duplicates
                })
    
    except UnicodeDecodeError as e:
        print(f"错误：无法读取文件 {file_path}，编码问题：{e}")
        return False, []
    except FileNotFoundError:
        print(f"错误：文件 {file_path} 不存在")
        return False, []
    
    return has_duplicates, duplicate_lines

def main():
    file_path = 'original/references/other_characters'
    
    print("正在检查文件中的重复字符...")
    print(f"文件路径：{file_path}")
    print("-" * 50)
    
    has_duplicates, duplicate_lines = check_duplicate_characters(file_path)
    
    if not has_duplicates:
        print("✅ 检查完成：没有发现重复字符")
    else:
        print(f"❌ 发现 {len(duplicate_lines)} 行存在重复字符：")
        print()
        
        for line_info in duplicate_lines:
            print(f"第 {line_info['line_number']} 行：")
            print(f"  内容：{line_info['line_content']}")
            print(f"  重复字符：{', '.join(line_info['duplicates'])}")
            print()
        
        print("请手动修复这些重复字符后重新运行检查。")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())