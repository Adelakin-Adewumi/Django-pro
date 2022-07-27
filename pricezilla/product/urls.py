from .serializers import Comment
def post_detailview(request, id):
       
  if request.method == 'POST':
    cf = Comment(request.CONTENT or None)
    if cf.is_valid():
      content = request.CONTENT.get('content')
      comment = Comment.objects.create(user = request.user, content = content)
      comment.save()
      return (content.get_absolute_url())
    else:
      cf = Comment()
       
    context ={
      'comment_serializers':cf,
      }
    return (request, 'socio / post_detail.html', context)