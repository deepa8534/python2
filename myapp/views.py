from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def hello(request):
	# return render(request, "index.html", {})
    return HttpResponse("""<h1>welcome to first application</h1> 
			First name: <input type = "text" name = "first_name" />
			<br>
			Last name: <input type = "text" name = "Last_name" />
			<br>
			Email-id:<input type="text" name="email"/>
			<br>
			<select>
			<option value="course">course</option>
			<option value="iot">iot</option>
			<option value="blockchain">Blockchain</option>
			<option value="digital marketing">digital marketing</option>
			</select>
			<br>
			<input type="button" value="submit">
			""")
def home(request):
	return HttpResponse("""<h1>welcome to home page</h1>""")
# def hello(request):
#    # today = datetime.datetime.now().date()
#    return render(request, "index.html",{})