#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
wxauto 测试调试脚本
"""

import sys
import os

def test_import():
    """测试导入功能"""
    try:
        import wxauto
        print("✓ wxauto 导入成功")
        
        # 检查主要类
        from wxauto import WeChat, Chat, WxParam
        print("✓ 主要类导入成功: WeChat, Chat, WxParam")
        
        return True
    except Exception as e:
        print(f"✗ 导入失败: {e}")
        return False

def test_wechat_init():
    """测试微信初始化"""
    try:
        from wxauto import WeChat
        print("\n正在尝试初始化微信实例...")
        
        # 注意：这需要微信客户端运行
        wx = WeChat()
        print("✓ 微信实例初始化成功")
        
        # 获取基本信息
        print(f"当前用户: {wx.CurrentChat()}")
        
        return wx
    except Exception as e:
        print(f"✗ 微信初始化失败: {e}")
        print("提示：请确保微信客户端已启动并登录")
        return None

def test_basic_functions(wx):
    """测试基本功能"""
    if not wx:
        return
        
    try:
        # 获取聊天列表
        print("\n正在获取聊天列表...")
        chats = wx.GetAllChats()
        print(f"✓ 找到 {len(chats)} 个聊天")
        
        # 显示前5个聊天
        for i, chat in enumerate(chats[:5]):
            print(f"  {i+1}. {chat}")
            
    except Exception as e:
        print(f"✗ 获取聊天列表失败: {e}")

def main():
    """主测试函数"""
    print("=== wxauto 调试测试 ===\n")
    
    # 测试导入
    if not test_import():
        return
    
    # 测试微信初始化
    wx = test_wechat_init()
    
    # 测试基本功能
    test_basic_functions(wx)
    
    print("\n=== 测试完成 ===")

if __name__ == "__main__":
    main()