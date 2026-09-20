#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
KriptoAdım — 自动同步作者页「Emre Kaya'nın Son Yazıları」列表。

用法：
    python3 update-author-page.py

行为：
    扫描站点所有 index.html，找出 @type=Article / HowTo 且作者为 Emre Kaya
    的文章，按 dateModified（缺省 datePublished）降序取最新 8 篇，
    重写 yazar/emre-kaya/index.html 里的「Son Yazıları」<ul> 列表。

    脚本幂等：文章日期/标题不变时，重复运行结果一致。
"""
import html
import os
import re
import sys

SITE_ROOT = os.path.dirname(os.path.abspath(__file__))
AUTHOR_PAGE = os.path.join(SITE_ROOT, "yazar", "emre-kaya", "index.html")
MAX_ITEMS = 8


def find_articles():
    articles = []
    for dirpath, _dirnames, filenames in os.walk(SITE_ROOT):
        if "index.html" not in filenames:
            continue
        rel = os.path.relpath(dirpath, SITE_ROOT)
        # 跳过隐藏目录（.git 等）与 assets 之类无文章目录
        if rel != "." and any(p.startswith(".") or p in ("assets",) for p in rel.split(os.sep)):
            continue
        path = os.path.join(dirpath, "index.html")
        with open(path, encoding="utf-8") as f:
            text = f.read()

        # 必须是 Emre Kaya 署名的 Article / HowTo
        if not re.search(r'"@type":\s*"(Article|HowTo)"', text):
            continue
        if not re.search(r'"name":\s*"Emre Kaya"', text):
            continue

        headline = None
        m = re.search(r'"headline":\s*"([^"]+)"', text)
        if m:
            headline = m.group(1)
        else:
            m2 = re.search(r"<title>([^<]+)</title>", text)
            if m2:
                headline = m2.group(1).strip()
        if not headline:
            continue

        dm = re.search(r'"dateModified":\s*"([0-9-]+)"', text)
        dp = re.search(r'"datePublished":\s*"([0-9-]+)"', text)
        date = dm.group(1) if dm else (dp.group(1) if dp else "0000-00-00")

        slug = rel
        url = "/" + slug + "/" if slug else "/"

        articles.append({"headline": headline, "date": date, "url": url})

    # 先按标题正序（稳定），再按日期倒序；同一天内保持标题字母序，结果幂等
    articles.sort(key=lambda a: a["headline"])
    articles.sort(key=lambda a: a["date"], reverse=True)
    return articles


def update_author_page(articles):
    items = articles[:MAX_ITEMS]
    li_lines = [
        '            <li><a href="%s">%s</a></li>'
        % (a["url"], html.escape(a["headline"], quote=False))
        for a in items
    ]
    new_ul = "<ul>\n" + "\n".join(li_lines) + "\n          </ul>"

    with open(AUTHOR_PAGE, encoding="utf-8") as f:
        text = f.read()

    pattern = re.compile(r"(<h2>[^<]*Son Yazıları</h2>\s*)<ul>.*?</ul>", re.DOTALL)
    new_text, n = pattern.subn(lambda m: m.group(1) + new_ul, text)
    if n != 1:
        print("错误：作者页里没有匹配到「Son Yazıları」列表块", file=sys.stderr)
        sys.exit(1)

    with open(AUTHOR_PAGE, "w", encoding="utf-8") as f:
        f.write(new_text)
    return items


def main():
    articles = find_articles()
    if not articles:
        print("没有找到 Emre Kaya 署名的文章", file=sys.stderr)
        sys.exit(1)

    items = update_author_page(articles)
    print(f"共找到 {len(articles)} 篇 Emre Kaya 署名文章，已把最新 {len(items)} 篇写入作者页：")
    for a in items:
        print(f"  {a['date']}  {a['url']}  {a['headline']}")


if __name__ == "__main__":
    main()
