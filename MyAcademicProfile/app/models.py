from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_no = models.CharField(max_length=100)
    dob = models.DateField(max_length=10)
    email = models.EmailField(null=True)
    gender = models.CharField(max_length=15,null=True)
    religion = models.CharField(max_length=15, null=True)
    blood_group = models.CharField(max_length=10)
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=12)
    image = models.ImageField(upload_to='images')
    sem1_sgpa = models.FloatField(null=True)
    sem2_sgpa = models.FloatField(null=True)
    sem3_sgpa = models.FloatField(null=True)
    sem4_sgpa = models.FloatField(null=True)
    sem5_sgpa = models.FloatField(null=True)
    sem6_sgpa = models.FloatField(null=True)
    sem7_sgpa = models.FloatField(null=True)
    sem8_sgpa = models.FloatField(null=True)
    avg_sgpa = models.FloatField(null=True)

    def save(self, *args, **kwargs):
            student_sgpa_list = [x for x in [self.sem1_sgpa, self.sem2_sgpa, self.sem3_sgpa, self.sem4_sgpa, self.sem5_sgpa, self.sem6_sgpa, self.sem7_sgpa, self.sem8_sgpa] if x!=0.0 or 0]
            student_avg_sgpa = sum(student_sgpa_list)/len(student_sgpa_list) 
            print(student_avg_sgpa) 
            self.avg_sgpa = student_avg_sgpa
            return super(Student, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.roll_no}"
