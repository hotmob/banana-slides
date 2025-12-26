"""
检查任务状态和详细信息
"""
import sys
from pathlib import Path

# 添加backend目录到路径
sys.path.insert(0, str(Path(__file__).parent))

from app import create_app
from models.task import Task
from database import db

app = create_app()

with app.app_context():
    # 查询最近的任务
    tasks = Task.query.order_by(Task.created_at.desc()).limit(5).all()
    
    print("\n" + "="*80)
    print("最近5个任务状态")
    print("="*80)
    
    for task in tasks:
        print(f"\n任务ID: {task.id}")
        print(f"类型: {task.task_type}")
        print(f"状态: {task.status}")
        print(f"创建时间: {task.created_at}")
        print(f"完成时间: {task.completed_at}")
        
        if task.error_message:
            print(f"❌ 错误信息: {task.error_message}")
        
        progress = task.get_progress()
        if progress:
            print(f"进度: {progress}")
        
        print("-" * 80)

