from django import forms

def validate_comma(value):
    if ',' in value:
        raise forms.ValidationError("comma is not allowed")
    return value

my_default_errors = {
    'required': 'This field is required',
    'invalid': 'Enter a valid Number'
}

class RegistrationForm(forms.Form):
    
    name = forms.CharField(max_length=100, validators=[validate_comma])
    roll_no = forms.CharField(max_length=100, validators=[validate_comma], widget=forms.TextInput(attrs={'placeholder': 'eg: 1604-21-735-000'}))
    dob = forms.DateField(widget=forms.TextInput(attrs={'placeholder': 'eg: 27/10/2003'}))
    email = forms.EmailField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'eg: example@gmail.com'}))
    gender = forms.CharField(max_length=15, validators=[validate_comma])
    religion = forms.CharField(max_length=15, validators=[validate_comma])
    blood_group = forms.CharField(max_length=10, validators=[validate_comma])
    father_name = forms.CharField(max_length=100, validators=[validate_comma])
    mother_name = forms.CharField(max_length=100, validators=[validate_comma])
    address = forms.CharField(max_length=200)
    image = forms.ImageField(required=False)
    phone_number = forms.CharField(max_length=12)

    sem1_sgpa = forms.FloatField(max_value=10, min_value=0, widget=forms.TextInput(attrs={'placeholder': 'eg: 4.04'}), error_messages=my_default_errors)

    sem2_sgpa = forms.FloatField(max_value=10, min_value=0, widget=forms.TextInput(attrs={'placeholder': 'eg: 4.04'}), error_messages=my_default_errors)

    sem3_sgpa = forms.FloatField(max_value=10, min_value=0, widget=forms.TextInput(attrs={'placeholder': 'eg: 4.04'}), error_messages=my_default_errors)

    sem4_sgpa = forms.FloatField(max_value=10, min_value=0, widget=forms.TextInput(attrs={'placeholder': 'eg: 4.04'}), error_messages=my_default_errors)

    sem5_sgpa = forms.FloatField(max_value=10, min_value=0, widget=forms.TextInput(attrs={'placeholder': 'eg: 4.04'}), error_messages=my_default_errors)

    sem6_sgpa = forms.FloatField(max_value=10, min_value=0, widget=forms.TextInput(attrs={'placeholder': 'eg: 4.04'}), error_messages=my_default_errors)

    sem7_sgpa = forms.FloatField(max_value=10, min_value=0, widget=forms.TextInput(attrs={'placeholder': 'eg: 4.04'}), error_messages=my_default_errors)

    sem8_sgpa = forms.FloatField(max_value=10, min_value=0, widget=forms.TextInput(attrs={'placeholder': 'eg: 4.04'}), error_messages=my_default_errors)