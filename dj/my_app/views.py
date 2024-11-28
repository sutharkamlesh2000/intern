from django.forms import BaseModelForm
from django.shortcuts import render, HttpResponse
from django.views.generic import ListView,CreateView
from django.views import View
from .models import Student
from .forms import StudentForm
from django.http import JsonResponse
# def index(self):
#     return render(request,'index.html')

class StudentList(ListView):
    model = Student
    template_name = "index.html"
    context_object_name = "students"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['std_form'] = StudentForm()
        return context

class StudentCreate(CreateView):
    model = Student
    form_class = StudentForm
    template_name ="index.html"

    def form_valid(self, form):
        # student = form.save() 
        
        student = Student.objects.create(
            name=form.cleaned_data['name'],
            email=form.cleaned_data['email'],
            age=form.cleaned_data['age']
        )
        response = JsonResponse({'id':student.id,'name':student.name,'email':student.email,'age':student.age})
        return response
    
    def form_invalid(self, form):
        return JsonResponse({'errors': form.errors}, status=400)
    
class StudentDetails(View):
    def get(self,request):
        id = request.GET.get('id')
        student = Student.objects.filter(id=id).first()
        print('student--->',student)
        student_data = {
            'id':student.id,
            'name':student.name,
            'email':student.email,
            'age':student.age
        }
        print('-=------------->student_------------',student_data)
        return JsonResponse({'student':student_data,'status':200})

class DeleteStudent(View):
    def post(self, request, *args, **kwargs):
        id = request.POST.get('id')
        std = Student.objects.filter(id=id).first()

        std.delete()
        students = Student.objects.all().values()
        students = list(students)
        return JsonResponse({'status':200, 'students':students})


class UpdateStudent(View):
    def post(self,request):
        id = request.POST.get('id')
        print('------di------------------',id)
        student = Student.objects.filter(id=id).first()
        student.name = request.POST.get('name')
        student.email = request.POST.get('email')
        student.age = request.POST.get('age')
        student.save()

        response = JsonResponse({'id':student.id,'name':student.name,'email':student.email,'age':student.age})
        return response