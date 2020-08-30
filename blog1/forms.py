from .models import Post,Comments
from django import forms

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title','text',)

        widgets = {
            'title': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable'}),
        }


class CommentsForm(forms.ModelForm):

    class Meta:
        model = Comments
        fields = ('text',)