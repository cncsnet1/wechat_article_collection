
# 📚 微信公众号文章提取脚本使用教程

> 一个用于自动提取微信公众号历史文章链接的小工具，基于 `requests` 实现分页获取，支持本地保存归档整理。

---

## 🚀 快速开始

### ✅ 安装依赖
运行以下命令安装依赖库：

- `pip install requests`

---

## 🔧 使用步骤

### 1️⃣ 修改脚本配置参数

- **`fakeid`**：公众号唯一 ID（登录后抓包获取）
- **`token`**：接口访问令牌（登录微信公众平台后抓包获取）
- **`Cookie`**：完整 Cookie 信息（在浏览器开发者工具中复制）

示例代码片段中对应替换内容如下：

```
headers = {
  "Cookie": "👉 替换为你的 Cookie 信息",
  "User-Agent": "Apifox/1.0.0 (https://apifox.com)",
  ...
}
```

### 2️⃣ 运行脚本

- 在终端执行：

`python fetch_articles.py`

---

## 📁 输出说明

运行后将自动生成一个 `articles.txt` 文件，内容为抓取到的文章链接列表：

```
https://mp.weixin.qq.com/s/xxxxxxxx
https://mp.weixin.qq.com/s/yyyyyyyy
https://mp.weixin.qq.com/s/zzzzzzzz
```

---

## 🗂 项目结构

```
wechat-article-fetcher/
├── fetch_articles.py     主程序脚本
├── articles.txt          输出结果（文章链接列表）
└── README.md             使用文档说明
```

---

## ✨ 示例代码片段

```
for article in data.get('app_msg_list', []):
    articles.append({
        'title': article.get('title'),
        'link': article.get('link')
    })
```

---

## 🛠 技术说明

- 编程语言：Python 3.x
- 核心库：`requests`
- 输出格式：纯文本（支持扩展为 Markdown / CSV / JSON）
- 可扩展功能：关键词筛选、文章标题保存、分页自定义

---

## ⚠ 注意事项

- Cookie 和 Token 有有效期，需定期更新
- 请求频率请适度控制，防止触发平台风控
- 本脚本仅供技术学习交流使用，严禁商用

---
> **“愿每一行代码都通向未来，每一次交流都激发灵感。”**
