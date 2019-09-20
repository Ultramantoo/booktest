from django.shortcuts import render
from booktest.models import BookInfo


# 首页，展示所有图书
def index(request):
    # 查询所有图书
    booklist = BookInfo.objects.all()
    # 将图书列表传递到模板中，然后渲染模板
    return render(request, 'booktest/index.html', {'booklist': booklist})


# 详细页，接收图书的编号，根据编号查询，再通过关系找到本图书的所有英雄并展示
def detail(request, bid):
    # 根据图书编号对应图书
    book = BookInfo.objects.get(id=int(bid))
    # 查找book图书中的所有英雄信息
    heros = book.heroinfo_set.all()
    # 将图书信息传递到模板中，然后渲染模板
    return render(request, 'booktest/detail.html', {'book': book, 'heros': heros})
