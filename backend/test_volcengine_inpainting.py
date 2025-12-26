"""
测试 Volcengine Inpainting 配置
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))

from config import get_config
from services.inpainting_service import get_inpainting_service

print("="*60)
print("检查 Volcengine Inpainting 配置")
print("="*60)

# 检查配置
config = get_config()
print(f"\n1. Volcengine Access Key: {'✅ 已配置' if config.VOLCENGINE_ACCESS_KEY else '❌ 未配置'}")
print(f"2. Volcengine Secret Key: {'✅ 已配置' if config.VOLCENGINE_SECRET_KEY else '❌ 未配置'}")
print(f"3. Timeout: {config.VOLCENGINE_INPAINTING_TIMEOUT}秒")
print(f"4. Max Retries: {config.VOLCENGINE_INPAINTING_MAX_RETRIES}")

# 尝试初始化服务
print("\n正在初始化 Inpainting 服务...")
try:
    service = get_inpainting_service()
    provider_type = type(service.provider).__name__
    print(f"✅ 服务初始化成功！")
    print(f"   Provider类型: {provider_type}")
    
    if provider_type == "VolcengineInpaintingProvider":
        print("   ✅ 正在使用 Volcengine Inpainting Provider")
    else:
        print(f"   ⚠️  警告：Provider类型不是 Volcengine: {provider_type}")
        
except Exception as e:
    print(f"❌ 服务初始化失败: {e}")

print("\n" + "="*60)

