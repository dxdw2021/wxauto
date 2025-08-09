#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
wxauto 功能演示脚本
"""

from wxauto import WeChat
import time

def demo_basic_info(wx):
    """演示基本信息获取"""
    print("=== 基本信息 ===")
    print(f"当前用户: {wx.nickname}")
    
    # 获取聊天信息
    chat_info = wx.ChatInfo()
    print(f"当前聊天: {chat_info.get('chat_name', '未知')}")
    print(f"聊天类型: {chat_info.get('chat_type', '未知')}")
    if chat_info.get('chat_type') == 'group':
        print(f"群成员数: {chat_info.get('group_member_count', 0)}")

def demo_sessions(wx):
    """演示会话列表"""
    print("\n=== 会话列表 ===")
    sessions = wx.GetSession()
    print(f"共有 {len(sessions)} 个会话")
    
    # 获取会话详细信息
    for i, session in enumerate(sessions[:5]):
        try:
            # 尝试获取会话名称（需要查看SessionElement的属性）
            print(f"  {i+1}. 会话对象: {type(session).__name__}")
        except Exception as e:
            print(f"  {i+1}. 获取会话信息失败: {e}")

def demo_messages(wx):
    """演示消息获取"""
    print("\n=== 消息获取 ===")
    
    try:
        messages = wx.GetAllMessage()
        print(f"当前聊天共有 {len(messages)} 条消息")
        
        if messages:
            print("\n最近10条消息:")
            for i, msg in enumerate(messages[-10:]):
                # 限制消息内容长度
                content = str(msg.content)[:30] + "..." if len(str(msg.content)) > 30 else str(msg.content)
                print(f"  {i+1}. [{msg.type}] {content}")
                
    except Exception as e:
        print(f"获取消息失败: {e}")

def demo_send_message(wx):
    """演示发送消息（谨慎使用）"""
    print("\n=== 发送消息演示 ===")
    print("注意：这将实际发送消息，请谨慎使用！")
    
    # 获取当前聊天信息
    chat_info = wx.ChatInfo()
    current_chat = chat_info.get('chat_name', '未知聊天')
    
    confirm = input(f"是否向 '{current_chat}' 发送测试消息？(y/N): ").strip().lower()
    
    if confirm == 'y':
        test_msg = "这是一条来自 wxauto 的测试消息 🤖"
        try:
            result = wx.SendMsg(test_msg)
            if result.success:
                print("✓ 消息发送成功")
            else:
                print(f"✗ 消息发送失败: {result.message}")
        except Exception as e:
            print(f"✗ 发送消息时出错: {e}")
    else:
        print("已取消发送消息")

def demo_group_members(wx):
    """演示获取群成员"""
    print("\n=== 群成员获取 ===")
    
    chat_info = wx.ChatInfo()
    if chat_info.get('chat_type') == 'group':
        try:
            members = wx.GetGroupMembers()
            print(f"群成员共 {len(members)} 人:")
            for i, member in enumerate(members[:10]):  # 只显示前10个
                print(f"  {i+1}. {member}")
            if len(members) > 10:
                print(f"  ... 还有 {len(members) - 10} 个成员")
        except Exception as e:
            print(f"获取群成员失败: {e}")
    else:
        print("当前不是群聊，无法获取群成员")

def demo_new_messages(wx):
    """演示获取新消息"""
    print("\n=== 新消息监听演示 ===")
    print("将监听5秒钟的新消息...")
    
    # 记录开始时间
    start_time = time.time()
    
    while time.time() - start_time < 5:
        try:
            new_msgs = wx.GetNewMessage()
            if new_msgs:
                for msg in new_msgs:
                    content = str(msg.content)[:50] + "..." if len(str(msg.content)) > 50 else str(msg.content)
                    print(f"新消息: [{msg.type}] {content}")
        except Exception as e:
            print(f"获取新消息失败: {e}")
        
        time.sleep(1)
    
    print("新消息监听结束")

def main():
    """主演示函数"""
    print("=== wxauto 功能演示 ===\n")
    
    try:
        # 初始化微信
        print("正在连接微信...")
        wx = WeChat()
        print("✓ 微信连接成功\n")
        
        # 演示各种功能
        demo_basic_info(wx)
        demo_sessions(wx)
        demo_messages(wx)
        demo_group_members(wx)
        
        # 可选的发送消息演示
        demo_send_message(wx)
        
        # 新消息监听演示
        demo_new_messages(wx)
        
        print("\n=== 演示完成 ===")
        
    except Exception as e:
        print(f"演示过程中出错: {e}")
        import traceback
        traceback.print_exc()
    
    finally:
        # 清理资源
        try:
            if 'wx' in locals():
                wx.StopListening()
                print("已停止监听")
        except:
            pass

if __name__ == "__main__":
    main()