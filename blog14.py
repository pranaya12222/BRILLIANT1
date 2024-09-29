# views.py
def search(request):
    query = request.GET.get('q', '')
    posts = Post.objects.filter(title__icontains=query) | Post.objects.filter(content__icontains=query)
    return render(request, 'search_results.html', {'posts': posts})
