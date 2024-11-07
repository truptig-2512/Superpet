from django.shortcuts import render,HttpResponse
from django.views import View

# Create your views here.

#function based view

def about(request):
    return HttpResponse("about page")

def home(request):
    return HttpResponse("home page")

def index(request):
    return HttpResponse("index page")

def main(request):
    return HttpResponse("main page")

def courses(request):
    return render(request,"courses.html",{})

def student(request):
    return render(request,"student.html",{})

def index(request):
    return render(request,"index.html",{})


def students(request):
    print("********************")
    print(request.method)
    print("********************")
    context={"id":None,"name":"Trupti","subjects":["Maths","Science","English","Social Science"]}
    return render(request,"students.html",context)

def teacher(request):
    context={"id":1,"name":"Priyanka","courses":["Full stack web development","Data Science","Graphics Design"]}
    return render(request,"teacher.html",context)

def book(request):
    print(request.GET.get("bookname"))
    print(request.GET.get("price"))
    
    context={"bookname":request.GET.get("bookname"),
             "price":request.GET.get("price")
             }
    return render(request,"book.html",context)

def product(request):
    print(request.GET.get("productName"))
    print(request.GET.get("price"))
    
    context={"productName":request.GET.get("productName"),
             "price":request.GET.get("price")
             }
    return render(request,"product.html",context)

def employee(request):
    return render(request,"employee.html")

def employee(request):
    if request.method=='GET':
        return render(request,"employee.html")
    if request.method=='POST':
        employeeName=request.POST.get("employeeName")
        return render(request,"employee.html",{"empname": employeeName})
    
    
    
class MyView(View):
    
    def get(self,request):
        return render(request,"my_view.html")
    
    def post(self,request):
        return render(request,"success.html")
    
    
def learnFilters(request):
    return render(request,"template_filters.html",{"data":"dJANGO"})
    
    
    
    