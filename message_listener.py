#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
微信消息监听示例
"""

from wxauto import WeChat
import time

def message_handler(msg, chat):
    """消息处理函数"""
    print(f"\n收到新消息:")
    print(f"  聊天: {chat.who}")
    print(f"  类型: {msg.type}")
    print(f"  内容: {msg.content}")
    print(f"  时间: {time.strftime('%H:%M:%S')}")
    
    # 如果是文本消息，可以进行自动回复（谨慎使用）
    if msg.type == 'text' and '测试' in str(msg.content):
        print("  -> 检测到测试消息，准备回复...")
        # chat.SendMsg("收到你的测试消息！")  # 取消注释以启用自动回复

def main():
    """主函数"""
    print("=== 微信消息监听器 ===\n")
    
    try:
        # 初始化微信
        wx = WeChat()
        print(f"✓ 微信连接成功，当前用户: {wx.nickname}")
        
        # 获取会话列表
        sessions = wx.GetSession()
        print(f"✓ 找到 {len(sessions)} 个会话")
        
        # 选择要监听的聊天
        print("\n请选择要监听的聊天:")
        print("1. 监听当前聊天窗口")
        print("2. 手动输入聊天名称")
        
        choice = input("请选择 (1/2): ").strip()
        
        if choice == '1':
            # 监听当前聊天
            chat_info = wx.ChatInfo()
            chat_name = chat_info.get('chat_name', '未知聊天')
            print(f"将监听当前聊天: {chat_name}")
            
            # 添加监听
            result = wx.AddListenChat(chat_name, message_handler)
            if hasattr(result, 'success') and not result.success:
                print(f"添加监听失败: {result.message}")
                return
            
        elif choice == '2':
            # 手动输入聊天名称
            chat_name = input("请输入要监听的聊天名称: ").strip()
            if not chat_name:
                print("聊天名称不能为空")
                return
            
            print(f"将监听聊天: {chat_name}")
            
            # 添加监听
            result = wx.AddListenChat(chat_name, message_handler)
            if hasattr(result, 'success') and not result.success:
                print(f"添加监听失败: {result.message}")
                return
        
        else:
            print("无效选择")
            return
        
        print("✓ 监听已启动")
        print("按 Ctrl+C 停止监听\n")
        
        # 保持运行
        wx.KeepRunning()
        
    except KeyboardInterrupt:
        print("\n正在停止监听...")
    except Exception as e:
        print(f"监听过程中出错: {e}")
        import traceback
        traceback.print_exc()
    
    finally:
        # 清理资源
        try:
            if 'wx' in locals():
                wx.StopListening()
                print("✓ 监听已停止")
        except:
            pass

if __name__ == "__main__":
    main()