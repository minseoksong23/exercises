from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms
from . import util

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")

                
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
            "form": form,
            "entries": subst(form.cleaned_data["task"], util.list_entries())
        })
    return render(request, "encyclopedia/index.html", {
        "form": NewTaskForm(),
        " ": entry
    })

def entry(request, name):
    return render(request, "encyclopedia/entry.html", {
        "name": name,
        "content": util.get_entry(name)
    })
