#!/usr/bin/env python3
# ─────────────────────────────────────────────────────────────────────────────
#  build.py — regenerates thoughts.html and the posts/ pages from posts_data.py
#
#  Usage:   python3 build.py
#
#  It reuses the styling and navigation from index.html, so the blog always
#  matches the main page. Posts are sorted by their date, newest first.
# ─────────────────────────────────────────────────────────────────────────────
import os, re, sys
from collections import Counter

BASE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE)
from posts_data import POSTS

with open(os.path.join(BASE, "index.html"), encoding="utf-8") as f:
    index_html = f.read()
# Shared "head content" = everything from <title> through </style> in index.html
_start = index_html.index("<title>")
HEAD_INNER = index_html[_start: index_html.index("</style>") + len("</style>")]

SUN = '<circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/>'
MONTHS = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
CATEGORY_ORDER = ["Research", "Essays", "Film", "Life & Society", "Notes"]

def fmt_date(iso):
    try:
        y, m, d = iso.split("-")
        return MONTHS[int(m) - 1] + " " + str(int(d)) + ", " + y
    except Exception:
        return iso

def strip_tags(s):
    return re.sub(r"<[^>]+>", "", s).strip()

def split_paras(body):
    return [b.strip() for b in body.strip().split("\n\n") if b.strip()]

def render_block(b):
    b = b.strip()
    if re.match(r'^<(h[1-6]|ul|ol|li|figure|img|blockquote|pre|table|div)\b', b, re.I):
        return b  # already a block-level element (subheading, list, image…)
    return "<p>" + b.replace("\n", " ") + "</p>"

def page(title, body, extra_head=""):
    head = HEAD_INNER.replace("<title>Vahid S. Bokharaie</title>", "<title>" + title + "</title>", 1)
    return ('<!doctype html>\n<html lang="en">\n<head>\n'
            '<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
            + head + (("\n" + extra_head) if extra_head else "")
            + '\n</head>\n<body>\n' + body + '\n</body>\n</html>\n')

def nav(active, prefix=""):
    def hl(name):
        return ' style="color:var(--accent)"' if name == active else ""
    return (
'<header class="nav">\n'
'  <div class="wrap nav-inner">\n'
'    <a class="brand" href="' + prefix + 'index.html" style="text-decoration:none">vahid<span class="dot">.</span>sb</a>\n'
'    <nav class="nav-links" aria-label="Primary">\n'
'      <a href="' + prefix + 'index.html#about">about</a>\n'
'      <a href="' + prefix + 'index.html#research">research</a>\n'
'      <a href="' + prefix + 'index.html#software">software</a>\n'
'      <a href="' + prefix + 'index.html#experience">experience</a>\n'
'      <a href="' + prefix + 'index.html#publications">publications</a>\n'
'      <a href="' + prefix + 'thoughts.html" class="nav-cta"' + hl("thoughts") + '>thoughts</a>\n'
'      <a href="' + prefix + 'index.html#contact">contact</a>\n'
'    </nav>\n'
'    <button class="theme-btn" id="themeBtn" aria-label="Toggle color theme">\n'
'      <svg id="themeIcon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">' + SUN + '</svg>\n'
'      <span id="themeLabel">theme</span>\n'
'    </button>\n'
'  </div>\n'
'</header>')

def footer(prefix=""):
    return (
'<footer>\n'
'  <div class="wrap foot-inner">\n'
'    <span class="mono">© 2026 Vahid S. Bokharaie</span>\n'
'    <span class="mono">Control Engineer · Neuroscientist — <a href="' + prefix + 'index.html">home ↑</a></span>\n'
'  </div>\n'
'</footer>')

THEME_JS = (
'<script>\n'
'(function(){"use strict";\n'
'  var root=document.documentElement,btn=document.getElementById("themeBtn"),\n'
'      label=document.getElementById("themeLabel"),icon=document.getElementById("themeIcon");\n'
'  var SUN=\'' + SUN + '\',MOON=\'<path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/>\';\n'
'  function sysDark(){return window.matchMedia&&window.matchMedia("(prefers-color-scheme: dark)").matches;}\n'
'  function eff(){var t=root.getAttribute("data-theme");if(t==="dark")return true;if(t==="light")return false;return sysDark();}\n'
'  function paint(){var d=eff();if(icon)icon.innerHTML=d?SUN:MOON;if(label)label.textContent=d?"light":"dark";}\n'
'  var stored=null;try{stored=localStorage.getItem("vsb-theme");}catch(e){}\n'
'  if(stored==="dark"||stored==="light")root.setAttribute("data-theme",stored);\n'
'  paint();\n'
'  if(btn)btn.addEventListener("click",function(){var n=eff()?"light":"dark";root.setAttribute("data-theme",n);try{localStorage.setItem("vsb-theme",n);}catch(e){}paint();});\n'
'  if(window.matchMedia){var mq=window.matchMedia("(prefers-color-scheme: dark)");var oc=function(){if(!root.getAttribute("data-theme"))paint();};if(mq.addEventListener)mq.addEventListener("change",oc);else if(mq.addListener)mq.addListener(oc);}\n'
'})();\n'
'</script>')

BLOG_CSS = (
'<style>\n'
'  .filters-label{font-family:var(--mono);font-size:.72rem;letter-spacing:.1em;text-transform:uppercase;color:var(--faint);margin:0 0 .8rem}\n'
'  .filters{display:flex;flex-wrap:wrap;gap:.5rem;margin-bottom:2.4rem}\n'
'  .chip-btn{font-family:var(--mono);font-size:.8rem;letter-spacing:.02em;color:var(--muted);background:var(--surface);border:1px solid var(--border);padding:.45rem .9rem;border-radius:40px;cursor:pointer}\n'
'  .chip-btn:hover{color:var(--text);border-color:var(--border-strong)}\n'
'  .chip-btn.active{color:#14100a;background:var(--accent);border-color:var(--accent);font-weight:600}\n'
'  .chip-btn .cnt{opacity:.55;margin-left:.35rem}\n'
'  .postlist{display:flex;flex-direction:column}\n'
'  .post-row{display:block;padding:1.6rem 0;border-top:1px solid var(--border);text-decoration:none;color:var(--text)}\n'
'  .post-row:first-child{border-top:none}\n'
'  .post-row:hover{text-decoration:none}\n'
'  .post-row:hover .post-title{color:var(--accent)}\n'
'  .post-meta{display:flex;align-items:center;gap:.8rem;margin-bottom:.5rem}\n'
'  .post-meta .cat{font-family:var(--mono);font-size:.7rem;letter-spacing:.06em;text-transform:uppercase;color:var(--accent-2);border:1px solid color-mix(in srgb,var(--accent-2) 30%,transparent);padding:.18rem .5rem;border-radius:5px}\n'
'  .post-meta .pdate{font-family:var(--mono);font-size:.78rem;color:var(--faint)}\n'
'  .post-title{margin:0 0 .45rem;font-size:1.32rem;font-weight:600;letter-spacing:-0.01em;line-height:1.2;color:var(--text)}\n'
'  .post-excerpt{margin:0;color:var(--muted);max-width:72ch;line-height:1.6}\n'
'  .postbody{color:var(--text);font-size:1.06rem;line-height:1.75;max-width:68ch}\n'
'  .postbody p{margin:0 0 1.2rem}\n'
'  .empty-note{font-family:var(--mono);font-size:.85rem;color:var(--faint);padding:2rem 0}\n'
'</style>')

FILTER_JS = (
'<script>\n'
'(function(){\n'
'  var chips=document.querySelectorAll(".chip-btn"),rows=document.querySelectorAll(".post-row"),empty=document.getElementById("emptyNote");\n'
'  function apply(f){var shown=0;rows.forEach(function(r){var ok=(f==="all"||r.getAttribute("data-cat")===f);r.hidden=!ok;if(ok)shown++;});if(empty)empty.hidden=(shown>0);}\n'
'  chips.forEach(function(c){c.addEventListener("click",function(){chips.forEach(function(x){x.classList.remove("active");});c.classList.add("active");apply(c.getAttribute("data-filter"));});});\n'
'})();\n'
'</script>')

# ── sort newest first ────────────────────────────────────────────────────────
posts = sorted(POSTS, key=lambda p: p["date"], reverse=True)

# ── individual post pages ────────────────────────────────────────────────────
os.makedirs(os.path.join(BASE, "posts"), exist_ok=True)
for p in posts:
    body_html = "\n".join(render_block(x) for x in split_paras(p["body"]))
    body = nav("thoughts", "../") + (
'\n<main>\n'
'<article class="block" style="padding-top:clamp(2.5rem,6vw,4.5rem)">\n'
'  <div class="wrap" style="max-width:820px">\n'
'    <a href="../thoughts.html" style="font-family:var(--mono);font-size:.8rem">&#8592; All posts</a>\n'
'    <p class="eyebrow" style="margin-top:1.4rem">' + p["category"] + ' &middot; ' + fmt_date(p["date"]) + '</p>\n'
'    <h1 style="font-family:var(--sans);font-weight:600;font-size:clamp(1.7rem,4.5vw,2.5rem);line-height:1.12;letter-spacing:-0.01em;margin:.2rem 0 1.6rem;color:var(--text);text-wrap:balance">' + p["title"] + '</h1>\n'
'    <div class="postbody">\n' + body_html + '\n    </div>\n'
'    <p class="note" style="margin-top:2.4rem">&#8212; Vahid</p>\n'
'    <p style="margin-top:1.2rem"><a href="../thoughts.html" style="font-family:var(--mono);font-size:.8rem">&#8592; Back to all posts</a></p>\n'
'  </div>\n'
'</article>\n</main>\n') + footer("../") + "\n" + THEME_JS
    html = page(p["title"] + " — Vahid S. Bokharaie", body)
    with open(os.path.join(BASE, "posts", p["slug"] + ".html"), "w", encoding="utf-8") as f:
        f.write(html)

# ── the Thoughts & Past Work index ───────────────────────────────────────────
counts = Counter(p["category"] for p in posts)
cats = [c for c in CATEGORY_ORDER if counts.get(c)] + [c for c in counts if c not in CATEGORY_ORDER]

chips = '<button class="chip-btn active" data-filter="all">All <span class="cnt">' + str(len(posts)) + '</span></button>\n'
for c in cats:
    chips += '      <button class="chip-btn" data-filter="' + c + '">' + c + ' <span class="cnt">' + str(counts[c]) + '</span></button>\n'

rows = ""
for p in posts:
    excerpt = strip_tags(split_paras(p["body"])[0])
    rows += (
'      <a class="post-row" href="posts/' + p["slug"] + '.html" data-cat="' + p["category"] + '">\n'
'        <div class="post-meta"><span class="cat">' + p["category"] + '</span><span class="pdate">' + fmt_date(p["date"]) + '</span></div>\n'
'        <h3 class="post-title">' + p["title"] + '</h3>\n'
'        <p class="post-excerpt">' + excerpt + '</p>\n'
'      </a>\n')

thoughts_body = nav("thoughts") + (
'\n<section class="block" style="padding-top:clamp(3rem,7vw,5rem);padding-bottom:clamp(1.5rem,3vw,2.5rem)">\n'
'  <div class="wrap">\n'
'    <p class="eyebrow">Thoughts &amp; Past Work</p>\n'
'    <h1 style="font-family:var(--mono);font-weight:600;font-size:clamp(1.9rem,5.5vw,3rem);letter-spacing:-0.01em;line-height:1.05;margin:.2rem 0 1rem;color:var(--text)">Thoughts &amp; Past Work</h1>\n'
'    <p class="prose" style="font-size:1.06rem;color:var(--muted)">My own scientific work and research notes, alongside essays, film, and thoughts on life and society. Filter to what you\'re after.</p>\n'
'  </div>\n'
'</section>\n'
'<main>\n'
'<section class="block" style="border-bottom:none;padding-top:0">\n'
'  <div class="wrap">\n'
'    <p class="filters-label">Filter</p>\n'
'    <div class="filters">\n      ' + chips + '    </div>\n'
'    <div class="postlist">\n' + rows + '    </div>\n'
'    <p class="empty-note" id="emptyNote" hidden>No posts in this category yet.</p>\n'
'  </div>\n'
'</section>\n</main>\n') + footer() + "\n" + FILTER_JS + "\n" + THEME_JS

with open(os.path.join(BASE, "thoughts.html"), "w", encoding="utf-8") as f:
    f.write(page("Thoughts & Past Work — Vahid S. Bokharaie", thoughts_body, BLOG_CSS))

print("Built thoughts.html and " + str(len(posts)) + " post page(s):")
for p in posts:
    print("  " + p["date"] + "  [" + p["category"] + "]  posts/" + p["slug"] + ".html")
