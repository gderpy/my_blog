from django import forms
from .models import Article, Category


class AddPostForm(forms.ModelForm):
    title = forms.CharField(max_length=255, label="Название статьи", 
                            widget=forms.TextInput(attrs={"class": "form-control mt-2", "placeholder": "Укажите название статьи", "id": "article-title"}))
    content = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control mt-2", "rows": 3, "id": "exampleFormControlTextarea1"}), 
                              required=True, label="Содержание статьи")
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        label="Выберите категорию",
        empty_label="Не выбрано",
        required=True,
        widget=forms.RadioSelect)  

    class Meta:
        model = Article
        fields = ("title", "content", "category")
