import os
import re

# 原始的Markdown文件路径
markdown_file_path = 'vscode界面认识.md'

# GitHub存储路径的基础URL
github_base_url = "https://github.com/Spike-Julia/markdown-photos/blob/8bdcbe9f81eb6f3025270f476653c58ae4292b19/Spike-Julia/Visual%20Stuido%20Code%20develop/"

# 读取Markdown文件
with open(markdown_file_path, 'r', encoding='utf-8') as file:
    markdown_content = file.read()

# 使用正则表达式匹配 img 标签中的本地路径，并替换为 GitHub 路径
def replace_image_paths(content):
    # 匹配 <img src="..."> 格式
    img_tag_pattern = re.compile(r'<img src="([^"]+)" alt="([^"]+)"( style="[^"]*")? />')
    
    # 匹配 ![alt_text](local_path) 格式
    markdown_img_pattern = re.compile(r'!\[([^\]]*)\]\(([^)]+)\)')
    
    # 替换 <img> 标签中的本地路径
    def replace_img_tag(match):
        local_path = match.group(1)
        alt_text = match.group(2)
        style = match.group(3) if match.group(3) else ''  # 保留style属性（如果有的话）
        
        # 提取文件名
        filename = os.path.basename(local_path)
        
        # 构建新的GitHub URL
        github_url = github_base_url + filename
        
        # 返回更新后的 img 标签，不改变 style 部分
        return f'<img src="{github_url}" alt="{alt_text}"{style} />'
    
    # 替换 Markdown 图片语法中的本地路径
    def replace_markdown_img(match):
        alt_text = match.group(1)
        local_path = match.group(2)
        
        # 提取文件名
        filename = os.path.basename(local_path)
        
        # 构建新的GitHub URL
        github_url = github_base_url + filename
        
        # 返回更新后的 Markdown 图片语法
        return f'![{alt_text}]({github_url})'

    # 替换两个格式的图片路径
    content = re.sub(img_tag_pattern, replace_img_tag, content)
    content = re.sub(markdown_img_pattern, replace_markdown_img, content)

    return content

# 替换Markdown中的图片路径
updated_markdown_content = replace_image_paths(markdown_content)

# 将替换后的内容写回到文件
with open(markdown_file_path, 'w', encoding='utf-8') as file:
    file.write(updated_markdown_content)

print(f"Markdown文件中的图片路径已成功更新为GitHub链接！")
