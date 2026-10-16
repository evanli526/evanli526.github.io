# 如何更新日志

## 新建日志

1. 登录 GitHub，打开[日志文件夹](https://github.com/evanli526/evanli526.github.io/tree/main/content/journal)。
2. 点击 **Add file → Create new file**。文件名使用未重复的英文或数字，例如 `20261016-first.md`，以 `.md` 结尾。不要修改 `_index.md`。
3. 复制下面的完整内容，再改成自己的标题和正文：

```markdown
---
title: "我的第一篇日志"
date: 2026-10-16
slug: 20261016-first
categories: []
draft: false
---

今天想记录的内容。

## 一个小标题

继续写正文，可以使用 **加粗**、列表和链接。
```

- `title`：日志标题，保留两侧英文双引号。
- `date`：日志日期，格式为 `年-月-日`。示例是 2026 年 10 月 16 日，请改为当天或过去的日期；未来日期不会发布。
- `slug`：网址短名，改为与文件名相同的英文或数字（不带 `.md`），每篇保持唯一；发布后不要修改。
- `categories`：可不填，保留 `[]` 即可。填写 `['生活']` 或 `['生活', '阅读']` 后，会显示在文章卡片左下角。
- `draft`：`false` 表示发布；`true` 不显示在博客，但公开仓库里的文件仍然可见。
- 上下两行 `---` 都要保留，正文写在第二行 `---` 之后。

4. 点击 **Commit changes…**，填写简短说明，例如“新增第一篇日志”，选择直接提交到 **main**（Commit directly to the main branch），再点击 **Commit changes**。
5. 打开仓库的 [Actions](https://github.com/evanli526/evanli526.github.io/actions)，等待本次更新显示绿色勾号，然后打开[博客](https://evanli526.github.io/)确认。若显示红叉，先打开失败记录查看原因，修正后重新提交。

## 修改已有日志

进入 [content/journal](https://github.com/evanli526/evanli526.github.io/tree/main/content/journal)，打开对应的 `.md` 文件，点击铅笔 **Edit this file**，修改后按上面的第 4、5 步提交和确认。保留原文件名；如果文件已有 `slug`，也保留原值，以免旧链接失效。

## 添加图片（需要时）

1. 打开 [static/images](https://github.com/evanli526/evanli526.github.io/tree/main/static/images)，点击 **Add file → Upload files**，上传可以公开使用的图片，再点击 **Commit changes**。建议使用不重复的英文或数字文件名，例如 `20261016-photo.jpg`。
2. 在日志正文加入 `![图片说明](/images/20261016-photo.jpg)`。文件名和扩展名必须与上传的一致，引用路径不带 `static`。
3. 提交日志，等待 Actions 成功，再打开博客检查图片。
