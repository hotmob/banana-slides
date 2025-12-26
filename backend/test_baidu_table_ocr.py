"""
测试百度表格OCR识别功能
"""
import os
import sys
from pathlib import Path

# 添加项目根目录到路径
sys.path.insert(0, str(Path(__file__).parent))

from services.ai_providers.ocr import create_baidu_table_ocr_provider


def test_baidu_table_ocr():
    """测试百度表格OCR"""
    
    # 从环境变量获取api_key
    api_key = os.getenv('BAIDU_OCR_API_KEY')
    api_secret = os.getenv('BAIDU_OCR_API_SECRET')
    
    if not api_key:
        print("❌ 未配置 BAIDU_OCR_API_KEY 环境变量")
        print("请在 .env 文件中添加:")
        print("  BAIDU_OCR_API_KEY=bce-v3/ALTAK-...")
        print("或")
        print("  BAIDU_OCR_API_KEY=your_access_token")
        return
    
    print("=" * 80)
    print("测试百度表格OCR识别")
    print("=" * 80)
    print(f"API Key: {api_key[:20]}...")
    
    # 创建provider
    provider = create_baidu_table_ocr_provider(api_key, api_secret)
    
    if not provider:
        print("❌ 创建provider失败")
        return
    
    print("✅ Provider创建成功\n")
    
    # 测试图片路径
    test_image = "/mnt/d/Desktop/banana-slides/uploads/mineru_files/bd74b690/images/0540d310b35ac699550e3b42f7dcd2227ac6b364cb894a023f353a188ca75600.jpg"
    
    if not Path(test_image).exists():
        print(f"❌ 测试图片不存在: {test_image}")
        return
    
    print(f"📸 测试图片: {test_image}\n")
    
    # 识别表格
    try:
        result = provider.recognize_table(
            image_path=test_image,
            cell_contents=True
        )
        
        print(f"\n✅ 识别成功!")
        print(f"  log_id: {result.get('log_id')}")
        print(f"  表格数量: {result.get('table_num')}")
        print(f"  图片尺寸: {result.get('image_size')}")
        print(f"  单元格数量: {len(result.get('cells', []))}")
        
        print("\n" + "=" * 80)
        print("单元格详情:")
        print("=" * 80)
        
        for i, cell in enumerate(result.get('cells', []), 1):
            section = cell.get('section', 'unknown')
            text = cell.get('text', '')
            bbox = cell.get('bbox', [])
            
            if section == 'body':
                row = f"[{cell.get('row_start')},{cell.get('row_end')}]"
                col = f"[{cell.get('col_start')},{cell.get('col_end')}]"
                print(f"{i:2d}. {section:6s} row={row} col={col} | {text}")
            else:
                print(f"{i:2d}. {section:6s} | {text}")
        
        print("\n" + "=" * 80)
        
        # 检查表格结构
        structure = provider.get_table_structure(result.get('cells', []))
        print(f"表格结构: {structure['rows']} 行 x {structure['cols']} 列")
        
    except Exception as e:
        print(f"❌ 识别失败: {e}")
        import traceback
        traceback.print_exc()


if __name__ == '__main__':
    # 加载.env文件
    from dotenv import load_dotenv
    load_dotenv()
    
    test_baidu_table_ocr()

