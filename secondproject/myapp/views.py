from django.shortcuts import render
from django.http import HttpResponse
from .models import Register

# Create your views here.
def index(request):
	return render(request,'index.html')
def register(request):
	if request.method=='POST':
		post=Register()
		post.name=request.POST.get('first_name')
		post.mobile=request.POST.get('mobile')
		post.email=request.POST.get('email')
		post.course=request.POST.get('course')
		post.source=request.POST.get('source')
		post.date=request.POST.get('date')
		post.status=request.POST.get('status')
		post.counsler=request.POST.get('counsler')
		post.remark=request.POST.get('remark')
		post.save()
		return HttpResponse("success")
	else:
		return render(request,'index2.html')
def walkin(request):
	# form= Register.objects.all('id')
	form= Register.objects.order_by('id')
	# form= Register.objects.filter(id=10)
	# form= Register.objects.annotate(Count('id'))
	return render(request,'index3.html', {"form":form})
def calling(request):
	form=Register.objects.filter(status='Demo')
	return render(request,'index3.html', {"form":form})
def counselling(request):
	form=Register.objects.filter(date__range=["2018-06-19", "2018-06-21"])
	return render(request,'index3.html',{"form":form})
def joining(request):
	form=Register.objects.filter(date__range=["2018-06-19", "2018-06-21"])
	return render(request,'index4.html',{"form":form})
def currentstatus(request):
	form=Register.objects.all()
	return render(request,'index3.html',{"form":form})
