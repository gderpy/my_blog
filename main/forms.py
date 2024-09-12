from django import forms
from .models import Article, Category


class AddPostForm(forms.ModelForm):
    title = forms.CharField(max_length=255, label="Название статьи", 
                            widget=forms.TextInput(attrs={"class": "form-control mt-2", "placeholder": "Укажите название статьи", "id": "article-title"}))
    
    # content = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control mt-2", "rows": 3, "id": "exampleFormControlTextarea1"}), 
    #                           required=True, label="Содержание статьи")
    
    content = forms.CharField(widget=forms.HiddenInput(), label="Текст поля")

    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        label="Выберите категорию",
        empty_label="Не выбрано",
        required=True,
        widget=forms.RadioSelect)  

    class Meta:
        model = Article
        fields = ("title", "content", "category")


class TrixEditorWidget(forms.Textarea):
    class Media:
        css = {
            "all": ("https://unpkg.com/trix@2.0.8/dist/trix.css",)
        }
        js = ("https://unpkg.com/trix@2.0.8/dist/trix.umd.min.js",)


    def build_attrs(self, base_attrs, extra_attrs=None):
        attrs = super().build_attrs(base_attrs, extra_attrs)
        attrs.update({"class": "trix-content"})
        return attrs
