"""调试元素添加"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))

from services.export_service import ExportService
import logging

logging.basicConfig(level=logging.DEBUG)

# 测试路径
test_image = "/mnt/d/Desktop/banana-slides/uploads/13ef1d13-24cf-49a9-813d-22e27032145c/pages/b0f3436f-75cc-48a0-9fe4-f7f2a2610fb6_1766468499164.png"

# 读取最近生成的mineru结果
import os
mineru_base = "/mnt/d/Desktop/banana-slides/uploads/mineru_files"
dirs = sorted([d for d in os.listdir(mineru_base) if os.path.isdir(os.path.join(mineru_base, d))], 
              key=lambda x: os.path.getmtime(os.path.join(mineru_base, x)), 
              reverse=True)
latest_mineru = os.path.join(mineru_base, dirs[0])

print(f"使用MinerU结果: {latest_mineru}")
print(f"测试图片: {test_image}")
print()

# 检查文件
layout_file = os.path.join(latest_mineru, "layout.json")
if os.path.exists(layout_file):
    import json
    with open(layout_file) as f:
        layout = json.load(f)
    
    print(f"layout.json存在")
    print(f"页数: {len(layout.get('pdf_info', []))}")
    
    if layout.get('pdf_info'):
        page0 = layout['pdf_info'][0]
        print(f"第0页:")
        print(f"  page_size: {page0.get('page_size')}")
        print(f"  para_blocks数量: {len(page0.get('para_blocks', []))}")
        
        # 显示前几个block
        for i, block in enumerate(page0.get('para_blocks', [])[:5]):
            print(f"  Block {i}: type={block.get('type')}, bbox={block.get('bbox')}")
            if block.get('type') == 'text' and block.get('lines'):
                for line in block['lines'][:1]:
                    for span in line.get('spans', [])[:1]:
                        print(f"    文本: {span.get('content', '')[:30]}")
else:
    print("layout.json不存在")

print("\n检查images目录:")
images_dir = os.path.join(latest_mineru, "images")
if os.path.exists(images_dir):
    images = os.listdir(images_dir)
    print(f"  图片数量: {len(images)}")
    for img in images[:3]:
        print(f"  - {img}")
else:
    print("  images目录不存在")

