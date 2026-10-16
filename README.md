# senyang · Markdown 静态博客

目标地址：https://evanli526.github.io/ ，仓库 evanli526/evanli526.github.io 。

使用固定 Hugo 0.147.9，从content/中的Markdown生成网站。保留深灰布纹、白字、本地Noto字体；公式构建为MathML，代码由Hugo生成，无读者侧外部CDN依赖。原Halo项目独立保留，此站不连接Halo数据库或后台。

## 本地

在本目录运行 `./scripts/preview.sh`，打开 http://127.0.0.1:8787/ 。Control+C停止。`./scripts/build.sh`生成public/，不要把public/提交仓库。

Mac专用Hugo已放runtime/并通过官方SHA256验证；runtime/不提交。换电脑可从Hugo官方0.147.9发布下载对应程序放runtime/hugo，无需Node或npm。

## 写文章

在GitHub打开仓库，进入content/notes/或content/journal/，点Add file → Create new file，新建英文文件名，例如first-note.md。复制以下内容后改写：

```yaml
---
title: "我的文章标题"
date: 2026-10-16T00:00:00Z
slug: first-note
description: "一句话摘要"
categories: ["大模型", "数据结构与算法"]
draft: false
toc: true
---
```

接着写Markdown正文。笔记放notes，日志放journal；文件所在目录决定栏目；学科分类另用categories填写。日期不能晚于实际发布时刻，否则默认不构建。slug保持稳定以免旧链接失效。

`categories`填写学科或主题，独立于笔记/日志栏目。例如 `categories: ["大模型"]` 是单分类，`categories: ["大模型", "数据结构与算法"]` 是多分类，`categories: []` 或省略此行就不显示分类。分类只在文章卡片左下角展示，点名称可查看同分类文章。上面的分类是填写示例，不会自动应用于现有文章。`slug`仅决定网址短名，不用于分类；编辑分类时保留已有slug和文件路径，旧网址不变。

现有文章：打开对应.md文件 → 铅笔Edit → 修改 → Commit changes到main。Actions完成后网站更新。关于介绍改content/about.md。

图片：进入static/images/，Add file → Upload files，上传你有权公开的图片，再提交。正文使用 `![图片说明](/images/example.jpg)`。路径会自动兼容项目站子目录。也支持把文章建成content/notes/my-note/index.md，并把图片放同一目录，以 `![说明](photo.jpg)` 引用。

公式：推荐行内 `\(E=mc^2\)`；独立公式前后各一行 `$$`。代码使用三个反引号包围并写语言名；表格使用Markdown竖线格式。构建错误时查看Actions日志后修正文法。

**公开仓库中的文件及提交历史本身公开。draft:true只是不输出到网站，不是私密保护。私人草稿请留在本机，不要提交到此仓库。** 删掉公开文件也不会抹去Git历史。

## 发布

`.github/workflows/pages.yml`在main提交后构建并发布GitHub Pages，Hugo版本与LinuxSHA256固定。仓库Settings → Pages → Source需要选择GitHub Actions。工作流从configure-pages读取实际base_url；根站与项目站均兼容。当前hugo.toml已设根站地址；若将来改用项目站，同步改baseURL为https://账号.github.io/仓库名/。

## 内容与素材

只包含两篇明确演示文章、关于占位介绍、导航/模板/构建脚本、独立生成的布纹和水岸演示图、本地Noto字体与OFL声明。没有导出任何Halo账号、数据库、草稿、附件库或其他研究仓库内容。图片沿用获准演示素材；个人介绍待填写。

本地构建和发布记录见docs/验收记录.md。源码MIT许可；字体遵守static/assets/*OFL.txt。

官方参考：
- https://gohugo.io/host-and-deploy/deploy-to-github-pages/
- https://gohugo.io/functions/transform/tomath/
