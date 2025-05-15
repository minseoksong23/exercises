from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms
from . import util

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task", required=False)

                
def subst(word,lst):
    ls = []
    len_word=len(word)
    len_lst=len(lst)
    for i in range(len_lst):
        for j in range(len(lst[i])-len_word+1):
            for k in range(len_word):
                if word[k] != lst[i][j+k]:
                    break
                if k == len_word-1:
                    ls += [lst[i]]
    return ls

def index(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            if form.cleaned_data["task"] in util.list_entries():
                return HttpResponseRedirect(reverse("encyclopedia:entry", args=[form.cleaned_data['task']]))
        return render(request, "encyclopedia/index.html", {
            "entries":subst(form.cleaned_data['task'], util.list_entries())
        })
    return render(request, "encyclopedia/index.html", {
            "entries":util.list_entries()
    })

def entry(request, name):
    return render(request, "encyclopedia/entry.html", {
        "name": name,
        "content": util.get_entry(name)
    })

def create(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        if title.is_valid() and content.is_valid():
            if title.cleaned_data["task"] not in util.list_entries():
                util.save_entry(title.clean_data["task"], content.clean_data["task"])
                return HttpResponseRedirect(reverse("encyclopedia:title", args=[title.clean_data["task"]]))
            else: 
                return HttpResponse("error")
        else:
            return render(request, "encyclopedia/create.html", {
            })
    return render(request, "encyclopedia/create.html", {
    })
