from django.shortcuts import render,redirect

# Create your views here.

from .models import *

from django import forms
from django.forms import widgets



from django.forms import ModelForm

'''
class BookForm(forms.Form):

        email=forms.EmailField()
		title = forms.CharField(max_length=32,label="书籍名称")
		price = forms.DecimalField(max_digits=8, decimal_places=2,label="价格")  # 999999.99
		date = forms.DateField(label="日期",
			widget=widgets.TextInput(attrs={"type":"date"})
		)
		#gender=forms.ChoiceField(choices=((1,"男"),(2,"女"),(3,"其他")))
		#publish=forms.ChoiceField(choices=Publish.objects.all().values_list("pk","title"))
		publish=forms.ModelChoiceField(queryset=Publish.objects.all())
		authors=forms.ModelMultipleChoiceField(queryset=Author.objects.all())
'''

from django.forms import widgets as wid
class BookForm(ModelForm):
    class Meta:
        model=Book
        fields="__all__"
        labels={"title":"书籍名称", "price":"价格"}
        widgets={
            "title":wid.TextInput(attrs={"class":"form-control"}),
            "price":wid.TextInput(attrs={"class":"form-control"}),
            "date":wid.TextInput(attrs={"class":"form-control","type":"date"}),
            "publish":wid.Select(attrs={"class":"form-control"}),
            "authors":wid.SelectMultiple(attrs={"class":"form-control"}),
        }
        error_messages={
            "title":{"required":"不能为空"}
        }


def books(request):
    book_list=Book.objects.all()
    return render(request,"books.html",locals())


def addbook(request):
    if request.method=="POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()    # form.model.objects.create(request.POST)
            return redirect("/books/")
        else:
            return render(request, "add.html", locals())
    form=BookForm()
    return render(request,"add.html",locals())


def editbook(request,edit_book_id):
    edit_book = Book.objects.filter(pk=edit_book_id).first()
    if request.method=="POST":
        form = BookForm(request.POST,instance=edit_book)
        if form.is_valid():
            form.save()  # edit_book.update(request.POST)
            return redirect("/books/")

    form=BookForm(instance=edit_book)
    return render(request,"edit.html",locals())