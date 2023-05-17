from django import forms

from .models import Client, Comment, ClientFile

class AddClientForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "w-full py-4 px-6 rounded-xl bg-gray-100"})
    )
    email = forms.CharField(
        widget=forms.TextInput(attrs={"class": "w-full py-4 px-6 rounded-xl bg-gray-100"})
    )
    description = forms.CharField(
        widget=forms.Textarea(attrs={"rows":"5", "class": "w-full bg-gray-100 rounded-xl"})
    )

    class Meta:
        model = Client
        fields = ('name', 'email', 'description',)

class AddCommentForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.Textarea(attrs={"rows":"5", "class": "w-full bg-gray-100 rounded-xl"})
    )

    class Meta:
        model = Comment
        fields = ('content',)

class AddFileForm(forms.ModelForm):
    class Meta:
        model = ClientFile
        fields = ('file',)