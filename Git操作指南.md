# Git 版本控制操作指南

## 📋 操作概述

本文档详细说明了如何执行完整的Git版本控制操作，包括分支管理、代码合并和推送等步骤。

## 🎯 操作目标

1. 在dev分支上基于当前版本创建一个新的工作分支
2. 将本地修改推送到个人的远程代码仓库
3. 将上游仓库的特定提交（203f5b92b987436bbf4575a65648302ccfc25883）合并到当前分支
4. 处理可能出现的代码冲突
5. 将合并后的代码推送到个人仓库

## 🔧 详细操作步骤

### 步骤1：检查当前Git状态

```bash
# 检查当前分支和状态
git status
git branch -a
git remote -v
```

**预期输出**：
- 当前分支：main 或其他
- 远程仓库：origin（个人仓库）、upstream（上游仓库）

### 步骤2：配置远程仓库

```bash
# 添加个人远程仓库（如果未配置）
git remote add origin https://4f81a011067e9b1719913c041dac439c@github.com/dxdw2021/wxauto.git

# 添加上游仓库
git remote add upstream https://github.com/cluic/wxauto.git

# 验证远程仓库配置
git remote -v
```

### 步骤3：获取最新代码

```bash
# 获取上游仓库最新代码
git fetch upstream

# 获取个人仓库最新代码
git fetch origin
```

### 步骤4：创建dev分支（基于当前版本）

```bash
# 基于当前版本创建dev分支
git checkout -b dev

# 或者如果dev分支已存在，切换到dev分支
git checkout dev
```

### 步骤5：创建工作分支

```bash
# 基于dev分支创建新的工作分支
git checkout -b feature/wxauto-enhancement-$(date +%Y%m%d)
```

### 步骤6：添加本地修改

```bash
# 查看未跟踪的文件
git status

# 添加所有新文件
git add .

# 或者选择性添加文件
git add debug_step_by_step.py
git add test_wxauto.py
git add wechat_test.py
git add wxauto_demo.py
git add message_listener.py
git add 项目总结.md
```

### 步骤7：提交本地修改

```bash
git commit -m "feat: 添加wxauto测试脚本和功能演示

- 添加debug_step_by_step.py逐步调试脚本
- 添加test_wxauto.py基础测试脚本  
- 添加wechat_test.py微信功能测试脚本
- 添加wxauto_demo.py功能演示脚本
- 添加message_listener.py消息监听示例
- 添加项目总结.md文档
- 修复API方法名称问题
- 完善错误处理和用户交互"
```

### 步骤8：推送到个人远程仓库

```bash
# 推送当前分支到个人仓库
git push -u origin feature/wxauto-enhancement-$(date +%Y%m%d)

# 或者推送到已存在的分支
git push origin HEAD
```

### 步骤9：合并上游特定提交

```bash
# 获取特定提交信息
git show 203f5b92b987436bbf4575a65648302ccfc25883

# 方法1：使用cherry-pick合并特定提交
git cherry-pick 203f5b92b987436bbf4575a65648302ccfc25883

# 方法2：使用merge合并（如果需要合并整个分支）
git merge upstream/main
```

### 步骤10：处理冲突（如果有）

如果出现冲突，执行以下步骤：

```bash
# 查看冲突文件
git status

# 手动编辑冲突文件，解决冲突标记
# <<<<<<< HEAD
# 你的代码
# =======
# 上游代码
# >>>>>>> 203f5b9

# 标记冲突已解决
git add <冲突文件名>

# 完成合并
git commit -m "resolve: 解决与上游提交203f5b9的冲突"
```

### 步骤11：最终推送

```bash
# 推送合并后的代码到个人仓库
git push origin HEAD
```

## 🚨 常见问题和解决方案

### 问题1：fatal: not a git repository

**解决方案**：
```bash
# 重新初始化Git仓库
git init
git remote add origin <你的仓库地址>
git remote add upstream <上游仓库地址>
```

### 问题2：分支已存在

**解决方案**：
```bash
# 删除已存在的分支
git branch -D <分支名>

# 或者切换到已存在的分支
git checkout <分支名>
```

### 问题3：推送失败

**解决方案**：
```bash
# 强制推送（谨慎使用）
git push -f origin <分支名>

# 或者先拉取再推送
git pull origin <分支名>
git push origin <分支名>
```

### 问题4：找不到特定提交

**解决方案**：
```bash
# 确保已获取上游仓库
git fetch upstream

# 查找提交
git log --oneline | grep 203f5b9
```

## 📝 操作验证

完成所有步骤后，验证操作结果：

```bash
# 检查当前分支
git branch

# 检查提交历史
git log --oneline -10

# 检查远程分支
git branch -r

# 验证文件状态
git status
```

## 🎉 操作完成标志

- ✅ 工作分支创建成功
- ✅ 本地修改已提交
- ✅ 代码已推送到个人仓库
- ✅ 上游提交已合并
- ✅ 冲突已解决（如果有）
- ✅ 最终代码已推送

## 📚 相关命令参考

```bash
# 查看Git配置
git config --list

# 查看提交历史
git log --graph --oneline --all

# 查看文件差异
git diff

# 撤销操作
git reset --hard HEAD~1  # 撤销最后一次提交
git checkout -- <文件名>  # 撤销文件修改
```

---

**注意**：执行Git操作时请确保网络连接稳定，并备份重要代码。