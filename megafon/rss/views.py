from django.shortcuts import render
from django import template

register = template.Library()

# -*- coding: UTF-8 -*-

import datetime
import feedparser


def pull_feed(request):
    d = feedparser.parse(r"https://lenta.ru/rss/news")
    e=[]
    for i in range(100):
        e.append({'text':d.entries[i],'link':d.entries[i].links[1].href})
    context = {
        "test": e,
        "feed": d.entries[0].links[1].href
        #"picture":d.entries[2].link
    }
    return render(request,'index.html',context)

# @register.inclusion_tag('templates/ex.html')
# def pull_feed(feed_url, posts_to_show=5):
#     try:
#         feed = feedparser.parse(feed_url)
#         posts = []
#         for i in range(posts_to_show):
#             pub_date = feed['entries'][i].updated_parsed
#             published = datetime.date(pub_date[0], pub_date[1], pub_date[2] )
#             posts.append({
#                           'title': feed['entries'][i].title,
#                           'summary': feed['entries'][i].summary,
#                           'link': feed['entries'][i].link,
#                           'date': published,
#                           })
#     except:
#         pass
#     return {'posts': posts}
# import datetime
# import feedparser
#
# # def show(request):
# #     context={
# #         "test":"Test"
# #     }
# #     return render(request,'index.html',context)
# @register.inclusion_tag('templates/ex.html')
# def pull_feed(feed_url, posts_to_show=5):
#     try:
#         feed = feedparser.parse(feed_url)
#         posts = []
#         for i in range(posts_to_show):
#             pub_date = feed['entries'][i].updated_parsed
#             published = datetime.date(pub_date[0], pub_date[1], pub_date[2] )
#             posts.append({
#                           'title': feed['entries'][i].title,
#                           'summary': feed['entries'][i].summary,
#                           'link': feed['entries'][i].link,
#                           'date': published,
#                           })
#     except:
#         pass
#     return {'posts': posts}
