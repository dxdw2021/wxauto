#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
wxauto 逐步调试脚本
"""

def step1_check_dependencies():
    """步骤1：检查依赖"""
    print("=== 步骤1：检查依赖 ===")
    
    dependencies = [
        'tenacity', 'pywin32', 'pyperclip', 
        'pillow', 'psutil', 'colorama', 'comtypes'
    ]
    
    for dep in dependencies:
        try:
            __import__(dep)
            print(f"✓ {dep}")
        except ImportError as e:
            print(f"✗ {dep}: {e}")

def step2_check_wxauto_modules():
    """步骤2：检查 wxauto 模块"""
    print("\n=== 步骤2：检查 wxauto 模块 ===")
    
    try:
        import sys
        import os
        
        # 添加当前目录到路径
        current_dir = os.path.dirname(os.path.abspath(__file__))
        if current_dir not in sys.path:
            sys.path.insert(0, current_dir)
        
        # 检查各个子模块
        modules = [
            'wxauto.param',
            'wxauto.exceptions', 
            'wxauto.languages',
            'wxauto.logger',
            'wxauto.uiautomation',
            'wxauto.wx'
        ]
        
        for module in modules:
            try:
                __import__(module)
                print(f"✓ {module}")
            except Exception as e:
                print(f"✗ {module}: {e}")
                
    except Exception as e:
        print(f"模块检查失败: {e}")

def step3_test_main_import():
    """步骤3：测试主要导入"""
    print("\n=== 步骤3：测试主要导入 ===")
    
    try:
        from wxauto import WeChat, Chat, WxParam
        print("✓ 主要类导入成功")
        
        print(f"WeChat 类: {WeChat}")
        print(f"Chat 类: {Chat}")
        print(f"WxParam 类: {WxParam}")
        
    except Exception as e:
        print(f"✗ 主要类导入失败: {e}")
        import traceback
        traceback.print_exc()

def step4_check_wechat_process():
    """步骤4：检查微信进程"""
    print("\n=== 步骤4：检查微信进程 ===")
    
    try:
        import psutil
        
        wechat_processes = []
        for proc in psutil.process_iter(['pid', 'name', 'exe']):
            try:
                if 'wechat' in proc.info['name'].lower():
                    wechat_processes.append(proc.info)
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass
        
        if wechat_processes:
            print(f"✓ 找到 {len(wechat_processes)} 个微信进程:")
            for proc in wechat_processes:
                print(f"  PID: {proc['pid']}, 名称: {proc['name']}")
        else:
            print("✗ 未找到微信进程，请启动微信客户端")
            
    except Exception as e:
        print(f"检查微信进程失败: {e}")

def main():
    """主函数"""
    step1_check_dependencies()
    step2_check_wxauto_modules()
    step3_test_main_import()
    step4_check_wechat_process()
    
    print("\n=== 调试完成 ===")

if __name__ == "__main__":
    main()