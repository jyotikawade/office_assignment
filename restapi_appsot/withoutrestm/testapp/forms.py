'''from django import forms
from testapp.models import Employee


 class EmployeeForm(forms.ModelForm):
    def clean_esal(self):
        inputsal = self.cleaned_data['esal']
        if inputsal < 5000:
            raise forms.ValidationError('the mininmum sal should be 500')
        return inputsal

    class Meta:
        model = Employee
        fields = '__all__'

'''



