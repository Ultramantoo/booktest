# from django.http import HttpResponse
# from django.template import loader, RequestContext
from django.shortcuts import render


# def index(request):
#     # 1.获取模板
#     template = loader.get_template('booktest/index.html')
#     # 2.定义上下文
#     context = {'title': '图书列表', 'list': range(10)}
#     # 3.渲染模板
#     return HttpResponse(template.render(context, request))

def index(request):
    context = {'title': '图书列表', 'list': range(10)}
    return render(request, 'booktest/index.html', context)
