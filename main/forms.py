from django import forms
from .models import Article, Category


class CategoryButtonWidget(forms.widgets.CheckboxSelectMultiple):
    template_name = 'widgets/category_buttons.html'


class AddPostForm(forms.ModelForm):
    title = forms.CharField(max_length=255, label="Название статьи", 
                            widget=forms.TextInput(attrs={"class": "form-control mt-2", "placeholder": "Укажите название статьи", "id": "article-title"}))
    content = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control mt-2", "rows": 3, "id": "exampleFormControlTextarea1"}), 
                              required=False, label="Содержание статьи")
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        label="Выберите категорию",
        empty_label="Не выбрано",
        required=True,
        widget=forms.RadioSelect)  

    # category = forms.ModelChoiceField(queryset=Category.objects.all(), label="Выберите категорию", empty_label="Не выбрано",
    #                                   widget=forms.Select(attrs={"class": "form-select mt-2", "id": "choose_category"}))

    class Meta:
        model = Article
        fields = ("title", "content", "category")


class MyForm(forms.Form):
    category = forms.ModelChoiceField(queryset=Category.objects.filter(parent_id__isnull=True),
                                      label="Выберите категорию",
                                      empty_label="Не выбрано",
                                      widget=forms.RadioSelect)  