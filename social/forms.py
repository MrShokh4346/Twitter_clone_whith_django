from django import forms
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class PostForm(forms.ModelForm):
    body = forms.CharField(required=True, 
        widget=forms.widgets.Textarea(
            attrs={
            'placeholder':"Enter Your Post",
            'class':'form-control',
            
            }
        ),
        label="",
    )
    class Meta:
        model = Post
        exclude = ('user',)



class SignUpForm(UserCreationForm):
	email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
	first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ism'}))
	last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Familiya'}))

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['username'].widget.attrs['placeholder'] = 'username'
		self.fields['username'].label = ''
		self.fields['username'].help_text = '<span class="form-text text-muted"><small>Majburiy. 150 belgidan ko\'p bo\'masligi kerak. Harflar, raqamlatr va @/./+/-/_  belgilar.</small></span>'

		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['placeholder'] = 'Parol'
		self.fields['password1'].label = ''
		self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Sizning parolingiz sizning ma\'lumotlaringiz bilan bir xil bo\'lmasligi kerak.</li><li>Sizning parolingiz kamida 8 ta belgidan kam bo\'lmasligi kerak.</li><li>Sizning parolingiz oddiy bo\'lmasligi kerak.</li><li>Sizning parolingiz faqat raqamdan iborat bulmasligi kerak.</li></ul>'

		self.fields['password2'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['placeholder'] = 'Parolni takrorlang'
		self.fields['password2'].label = ''
		self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Tekshirish uchun parolingizni qayta kiriting.</small></span>'