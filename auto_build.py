import os

# 完整目录结构字典
book_structure = {
    "index": "振动力学数字教材",
    "ch01": {"1.1": "引言", "1.2": "自由振动", "1.3": "简谐载荷作用下的强迫振动", "1.4": "周期激励作用下的强迫振动", "1.5": "任意激励载荷下作用下的强迫振动", "1.6": "隔振原理", "exercises": "习题"},
    "ch02": {"2.1": "引言", "2.2": "多自由度系统的自由振动", "2.3": "多自由度系统的强迫振动", "2.4": "主从系统的耦合振动", "2.5": "动力吸振器的基本原理", "exercises": "习题"},
    "ch03": {"3.1": "引言", "3.2": "杆的振动", "3.3": "梁的振动", "3.4": "板的振动", "3.5": "弹性系统计算分析", "exercises": "习题"},
    "ch04": {"4.1": "引言", "4.2": "舷外水对船体总振动的影响", "4.3": "船体梁总振动固有特性", "4.4": "船体强迫振动响应", "exercises": "习题"},
    "ch05": {"5.1": "引言", "5.2": "船舶板架的振动", "5.3": "上层建筑的振动", "5.4": "桅杆振动", "5.5": "艉轴架振动", "exercises": "习题"},
    "ch06": {"6.1": "引言", "6.2": "螺旋桨的激励", "6.3": "柴油机的激振力", "6.4": "波浪的激励", "6.5": "其他激励", "exercises": "习题"},
    "ch07": {"7.1": "船舶振动危害", "7.2": "船舶振动标准", "7.3": "船舶振动测试", "7.4": "船舶振动问题诊断", "7.5": "船舶振动控制", "exercises": "习题"},
    "references": "主要参考文献"
}

def create_markdown_file(filepath, title):
    """创建 markdown 文件并写入一级标题"""
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(f"# {title}\n\n此处添加内容...\n")

# 1. 创建首页
create_markdown_file("index.md", book_structure["index"])

# 2. 遍历章节创建文件夹和文件
for folder, sections in book_structure.items():
    if folder in ["index", "references"]:
        continue
    
    # 创建章节文件夹
    os.makedirs(folder, exist_ok=True)
    
    # 在文件夹内创建小节文件
    for filename, title_text in sections.items():
        # 给标题加上章节号前缀，习题除外
        display_title = f"{filename} {title_text}" if filename != "exercises" else title_text
        file_path = os.path.join(folder, f"{filename}.md")
        create_markdown_file(file_path, display_title)

# 3. 创建参考文献文件
create_markdown_file("references.md", book_structure["references"])

print("🎉 自动化构建完成！所有文件夹和带标题的 Markdown 文件已生成！")