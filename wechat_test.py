#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
微信实际操作测试脚本
"""

from wxauto import WeChat
import time

def test_wechat_connection():
    """测试微信连接"""
    print("=== 微信连接测试 ===")
    
    try:
        # 初始化微信实例
        print("正在连接微信...")
        wx = WeChat()
        print("✓ 微信连接成功")
        
        # 获取用户昵称
        print(f"当前用户: {wx.nickname}")
        
        # 获取聊天信息
        chat_info = wx.ChatInfo()
        print(f"当前聊天信息: {chat_info}")
        
        return wx
        
    except Exception as e:
        print(f"✗ 微信连接失败: {e}")
        print("请确保：")
        print("1. 微信客户端已启动并登录")
        print("2. 微信窗口可见（不要最小化）")
        return None

def test_get_chats(wx):
    """测试获取聊天列表"""
    if not wx:
        return
        
    print("\n=== 获取会话列表 ===")
    
    try:
        sessions = wx.GetSession()
        print(f"✓ 找到 {len(sessions)} 个会话")
        
        print("前10个会话:")
        for i, session in enumerate(sessions[:10]):
            print(f"  {i+1}. {session}")
            
        return sessions
        
    except Exception as e:
        print(f"✗ 获取会话列表失败: {e}")
        return []

def test_get_messages(wx):
    """测试获取消息"""
    if not wx:
        return
        
    print("\n=== 获取当前聊天消息 ===")
    
    try:
        messages = wx.GetAllMessage()
        print(f"✓ 获取到 {len(messages)} 条消息")
        
        if messages:
            print("最近5条消息:")
            for i, msg in enumerate(messages[-5:]):
                print(f"  {i+1}. [{msg.type}] {msg.content[:50]}...")
                
    except Exception as e:
        print(f"✗ 获取消息失败: {e}")

def interactive_test(wx):
    """交互式测试"""
    if not wx:
        return
        
    print("\n=== 交互式测试 ===")
    print("可用命令:")
    print("1. 输入 'chats' - 显示聊天列表")
    print("2. 输入 'msgs' - 显示当前聊天消息")
    print("3. 输入 'send:联系人:消息' - 发送消息")
    print("4. 输入 'quit' - 退出")
    
    while True:
        try:
            cmd = input("\n请输入命令: ").strip()
            
            if cmd == 'quit':
                break
            elif cmd == 'chats':
                sessions = wx.GetSession()
                for i, session in enumerate(sessions[:20]):
                    print(f"  {i+1}. {session}")
            elif cmd == 'msgs':
                messages = wx.GetAllMessage()
                for msg in messages[-10:]:
                    print(f"  [{msg.type}] {msg.content}")
            elif cmd.startswith('send:'):
                parts = cmd.split(':', 2)
                if len(parts) == 3:
                    _, contact, message = parts
                    wx.SendMsg(message, who=contact)
                    print(f"✓ 消息已发送给 {contact}")
                else:
                    print("格式错误，请使用: send:联系人:消息")
            else:
                print("未知命令")
                
        except KeyboardInterrupt:
            print("\n退出交互模式")
            break
        except Exception as e:
            print(f"命令执行错误: {e}")

def main():
    """主函数"""
    print("=== wxauto 微信操作测试 ===\n")
    
    # 测试连接
    wx = test_wechat_connection()
    
    if wx:
        # 测试基本功能
        test_get_chats(wx)
        test_get_messages(wx)
        
        # 交互式测试
        interactive_test(wx)
    
    print("\n=== 测试完成 ===")

if __name__ == "__main__":
    main()