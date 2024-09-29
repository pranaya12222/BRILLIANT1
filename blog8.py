# blog/views.py
@login_required
def delete_post(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.user == post.author:
        post.delete()
    return redirect('home')
