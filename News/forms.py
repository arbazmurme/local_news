from django import forms
from .models import News

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title','news']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'news' : forms.Textarea(attrs={'class':'form-control', 'rows':'10'}),
        }
        
    