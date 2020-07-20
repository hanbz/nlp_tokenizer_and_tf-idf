import feedparser
import jieba
from bs4 import BeautifulSoup

d = feedparser.parse('news.rss')

stopwords = [line.strip() for line in open('stopwords.txt').readlines()]
stopwords.append(' ')
stopwords.append(' ')

f_desc = open('description.txt', 'w')
f_output = open('output.txt', 'w')

for item in d.entries:
    seg_line = ''
    html = BeautifulSoup(item.description, "html.parser")
    f_desc.write(html.get_text() + "\n")
    segs = jieba.cut(html.get_text())
    for seg in segs:
        if seg not in stopwords:
            seg_line += seg+" , "
    f_output.write(seg_line + "\n")

f_desc.close()
f_output.close()
