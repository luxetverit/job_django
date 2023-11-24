from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import BoardList

# Create your views here.
def home(request):
    return render(request, 'home.html')

def board_list(request):
    page = request.GET.get('page', '1')
    boards = BoardList.objects.all()
    paginator = Paginator(boards, 10)
    page_obj = paginator.get_page(page)
    context = {'boards': page_obj, 'page': page}
    return render(request, 'community/board_list.html', context)

def board_detail(request, pk):
    posts = get_object_or_404(BoardList, pk=pk)
    context = {'posts': posts}
    return render(request, 'community/board_detail.html', context)
