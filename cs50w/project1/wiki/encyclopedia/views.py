from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms
from . import util
import random
import markdown2

class CreateForm(forms.Form):
    title = forms.CharField(label="title", required=False)
    content = forms.CharField(label="content", required=False)

class SearchForm(forms.Form):
    search = forms.CharField(label="search", required=False)

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
        form = SearchForm(request.POST)
        if form.is_valid():
            if form.cleaned_data["search"] in util.list_entries():
                return HttpResponseRedirect(reverse("encyclopedia:entry", args=[form.cleaned_data['search']]))
            return render(request, "encyclopedia/index.html", {
                "entries":subst(form.cleaned_data['search'], util.list_entries())
             })
    return render(request, "encyclopedia/index.html", {
            "entries":util.list_entries()
    })

def entry(request, name):
    if request.method=="POST":
        request.session["flag"]=True
        return render(request, "encyclopedia/create.html", {
            "name" : name,
            "content" : util.get_entry(name)
        })
    return render(request, "encyclopedia/entry.html", {
        "name": name,
        "content": util.get_entry(name)
    })

def create(request):
    if request.method == "POST":
        form = CreateForm(request.POST)
        if form.is_valid():
            if form.cleaned_data["title"] not in util.list_entries():
                util.save_entry(form.cleaned_data["title"], markdown2.markdown(form.cleaned_data["content"]))
                return HttpResponseRedirect(reverse("encyclopedia:entry", args=[form.cleaned_data["title"]]))
            else: 
                if request.session.pop("flag", False):
                    return render(request, "encyclopedia/entry.html", {
                        "name": form.cleaned_data["title"],
                        "content": markdown2.markdown(form.cleaned_data["content"])
                    })
                else:
                    return HttpResponse("error")
        else:
            return render(request, "encyclopedia/create.html", {
            })
    return render(request, "encyclopedia/create.html", {
    })

def rand(request):
    entries = util.list_entries()
    random_title = random.choice(entries)
    return HttpResponseRedirect(reverse("encyclopedia:entry", 
                args=[random_title]))

