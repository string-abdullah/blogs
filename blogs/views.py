from django.contrib import messages
from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post,Comment
from .forms import PostForm#,CommentForm

# Create your views here.

def post_create(request):
	form=PostForm(request.POST or None,request.FILES or None)
	if form.is_valid():
		instance=form.save(commit=False)
		instance.save()
		#messages.success(request,"successfully created")
		#return HttpResponseRedirect(instance.get_absolute_url())
	context={
		"form": form
	}
	return render(request, "post_form.html", context)

def post_list(request):
	
	queryset=Post.objects.all()#.order_by('timestamp')#[:5]

	context = {"obj_list":queryset,
	"title": "Posts"}
	return render(request, "post_list.html", context)

def  post_detail(request, id=None):
	user_id=request.user.id
	post_id=id
	comment=request.POST.get('comment')
	print user_id,post_id,comment
	form=Comment(post_id=str(id),user_id=str(user_id),comment=str(comment))
	if request.method=='POST':
		form.save()
	queryset=Comment.objects.filter(post_id=id).order_by('-timestamp')	
	
	instance= get_object_or_404(Post,id=id)
	context = {
		"title": instance.title,
		"instance":instance,
		"obj_list":queryset
		#"form":form


	}
	return render(request, "post_detail.html",context)
