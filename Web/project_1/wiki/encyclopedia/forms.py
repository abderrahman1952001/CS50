from django import forms

class CreateEntryForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField(widget=forms.Textarea(attrs=
                {"placeholder": "Enter the content in Markdown format...",}))
    

class EditEntryForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea)

    
    



