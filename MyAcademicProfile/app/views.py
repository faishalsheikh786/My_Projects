from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from app.forms import RegistrationForm

from app.models import Student

# Create your views here.

def login(request, roll_no):

        if request.POST:
            roll_no = request.POST['roll_no']
            dob = request.POST['dob']
            mother_name = request.POST['mother_name']

            student = Student.objects.get(roll_no=roll_no)
            
            if dob==str(student.dob) and mother_name==student.mother_name:
                return redirect(reverse('student_detail', args=(roll_no, dob, mother_name)))
            else:
                return redirect(reverse('login',args=(roll_no,)))

        else:
            context = {'roll_no':roll_no}
            return render(request, 'app/login.html',context)
            
        
        

def home(request):
    context = {}
    return render(request, 'app/index.html', context)

def students_list(request):
    students = Student.objects.all().order_by('roll_no')
    context = {'students':students}
    return render(request, 'app/students_list.html', context)

def student_detail(request, roll_no, dob, mother_name):
    student = Student.objects.get(roll_no=roll_no)
    context = {'student':student}
    return render(request, 'app/student_detail.html', context)

def thank_you(request):
    context = {}
    return render(request, 'app/thank_you.html', context)

def data_exist(request):
    context = {}
    return render(request, 'app/data_exist.html', context)





def registration(request, id):

    if id=='fill':
        student = Student
        registration_form = RegistrationForm()

        if request.POST:
            registration_form = RegistrationForm(request.POST, request.FILES)
            print(registration_form.errors)
            if registration_form.is_valid():
                name = registration_form.cleaned_data['name']
                roll_no = registration_form.cleaned_data['roll_no']
                dob = registration_form.cleaned_data['dob']
                email = registration_form.cleaned_data['email']
                gender = registration_form.cleaned_data['gender']
                religion = registration_form.cleaned_data['religion']
                blood_group = registration_form.cleaned_data['blood_group']
                father_name = registration_form.cleaned_data['father_name']
                mother_name = registration_form.cleaned_data['mother_name']
                address = registration_form.cleaned_data['address']
                phone_number = registration_form.cleaned_data['phone_number']
                image = registration_form.cleaned_data['image']
                sem1_sgpa = registration_form.cleaned_data['sem1_sgpa']
                sem2_sgpa = registration_form.cleaned_data['sem2_sgpa']
                sem3_sgpa = registration_form.cleaned_data['sem3_sgpa']
                sem4_sgpa = registration_form.cleaned_data['sem4_sgpa']
                sem5_sgpa = registration_form.cleaned_data['sem5_sgpa']
                sem6_sgpa = registration_form.cleaned_data['sem6_sgpa']
                sem7_sgpa = registration_form.cleaned_data['sem7_sgpa']
                sem8_sgpa = registration_form.cleaned_data['sem8_sgpa']

                if image==None:
                    image='images/default_image.png'

                students = Student.objects.all()
                
                text = '' 
                for student in students:
                    student_roll_no = student.roll_no
                    if roll_no==student_roll_no:
                        text = 'exist'
                        break
                    else:
                        text = 'does not exist'
                print(text)

                if text == 'does not exist' or text=="":        
                    student = Student(name=name, roll_no=roll_no, dob=dob, email=email, gender=gender, religion=religion, blood_group=blood_group, father_name=father_name, mother_name=mother_name, address=address, phone_number=phone_number, image=image, sem1_sgpa=sem1_sgpa, sem2_sgpa=sem2_sgpa, sem3_sgpa=sem3_sgpa, sem4_sgpa=sem4_sgpa, sem5_sgpa=sem5_sgpa, sem6_sgpa=sem6_sgpa, sem7_sgpa=sem7_sgpa, sem8_sgpa=sem8_sgpa)
                    student.save()
                    return redirect(reverse('thank_you',))
                else:
                    return redirect(reverse('data_exist',))
            else:
                print('is not valid')
    else:
        student = Student.objects.get(roll_no=id)
        registration_form = RegistrationForm(initial={
                'name' : student.name,
                'roll_no' : student.roll_no,
                'dob' : student.dob,
                'email' : student.email,
                'gender' : student.gender,
                'religion' : student.religion,
                'blood_group' : student.blood_group,
                'father_name' : student.father_name,
                'mother_name' : student.mother_name,
                'address' : student.address,
                'phone_number' : student.phone_number,
                'sem1_sgpa' : student.sem1_sgpa,
                'sem2_sgpa' : student.sem2_sgpa,
                'sem3_sgpa' : student.sem3_sgpa,
                'sem4_sgpa' : student.sem4_sgpa,
                'sem5_sgpa' : student.sem5_sgpa,
                'sem6_sgpa' : student.sem6_sgpa,
                'sem7_sgpa' : student.sem7_sgpa,
                'sem8_sgpa' : student.sem8_sgpa
        })
        
        if request.POST:
            registration_form = RegistrationForm(request.POST, request.FILES)
            if registration_form.is_valid():
                name = registration_form.cleaned_data['name']
                roll_no = registration_form.cleaned_data['roll_no']
                dob = registration_form.cleaned_data['dob']
                email = registration_form.cleaned_data['email']
                gender = registration_form.cleaned_data['gender']
                religion = registration_form.cleaned_data['religion']
                blood_group = registration_form.cleaned_data['blood_group']
                father_name = registration_form.cleaned_data['father_name']
                mother_name = registration_form.cleaned_data['mother_name']
                address = registration_form.cleaned_data['address']
                phone_number = registration_form.cleaned_data['phone_number']
                image = registration_form.cleaned_data['image']
                sem1_sgpa = registration_form.cleaned_data['sem1_sgpa']
                sem2_sgpa = registration_form.cleaned_data['sem2_sgpa']
                sem3_sgpa = registration_form.cleaned_data['sem3_sgpa']
                sem4_sgpa = registration_form.cleaned_data['sem4_sgpa']
                sem5_sgpa = registration_form.cleaned_data['sem5_sgpa']
                sem6_sgpa = registration_form.cleaned_data['sem6_sgpa']
                sem7_sgpa = registration_form.cleaned_data['sem7_sgpa']
                sem8_sgpa = registration_form.cleaned_data['sem8_sgpa']

                try:
                    student = Student.objects.get(roll_no=roll_no)
                except:
                    student = Student.objects.get(name=name)
                student.name=name
                student.dob = dob
                student.email = email
                student.gender = gender
                student.religion = religion
                student.blood_group = blood_group
                student.father_name = father_name
                student.mother_name = mother_name
                student.address = address
                student.phone_number = phone_number
                print(f'Form image :{image}')
                print(f'Student database image : {student.image}')

                if image!=None:
                    student.image = image

                student.sem1_sgpa = sem1_sgpa
                student.sem2_sgpa = sem2_sgpa
                student.sem3_sgpa = sem3_sgpa
                student.sem4_sgpa = sem4_sgpa
                student.sem5_sgpa = sem5_sgpa
                student.sem6_sgpa = sem6_sgpa
                student.sem7_sgpa = sem7_sgpa
                student.sem8_sgpa = sem8_sgpa
                student.save()
                return redirect(reverse('thank_you',))
            else:
                print('is not valid')
    print(f'last id:{id}')
    context = {'form': registration_form, 'student':student, 'id':id }
    return render(request, 'app/registration.html', context)