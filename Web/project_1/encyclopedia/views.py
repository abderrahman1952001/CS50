from django.shortcuts import render, redirect

from encyclopedia.forms import CreateEntryForm, EditEntryForm

from . import util

from markdown2 import markdown

from random import choice


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    md_content = util.get_entry(title)
    if md_content is None:
        return render(request, "encyclopedia/error.html", {
            "title": title,
            "message": "The requested page was not found"
        })
    html_content = markdown(md_content)
    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "content": html_content
            })

def search(request):
    query = request.GET.get("q", "").strip()
    
    if not query:
        return render(request, "encyclopedia/search.html", {
            "query": query})

    entries = util.list_entries()
    
    for entry in entries:
        if entry.lower() == query.lower():
            return redirect("encyclopedia:entry", title=entry)
    
    results = [entry for entry in entries if query.lower() in entry.lower()]

    return render(request, "encyclopedia/search.html", {
            "query": query,
            "results": results        
            })
        
    
def new(request):
    if request.method == "POST":
        form = CreateEntryForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"].strip()
            content = form.cleaned_data["content"].strip()    
            
            exists = any(entry.lower() == title.lower() for entry in util.list_entries())
            if exists:
                return render(request, "encyclopedia/new.html", 
                            {"form": form,
                            "error": "A page with this title already exists!"
                            })
            util.save_entry(title, content)
            return redirect("encyclopedia:entry", title=title)
        
        return render(request, "encyclopedia/new.html", {
            "form": form,
            "error": "Invalid entries."
        })
    form = CreateEntryForm()
    return render(request, "encyclopedia/new.html", {"form": form})


def edit(request, title):
    existing_content = util.get_entry(title)

    if existing_content is None:
        return render(request, "encyclopedia/error.html", {
            "title": title,
            "message": "The page you want to edit doesnt exist."
        })

    if request.method == "POST": 
        form = EditEntryForm(request.POST)
        if form.is_valid():
            new_content = form.cleaned_data["content"].strip()
            util.save_entry(title, new_content)
            return redirect("encyclopedia:entry", title=title)
        return render(request, "encyclopedia/edit.html", {
                                "title": title,    
                                "form": form})
          
    form = EditEntryForm(initial={"content": existing_content})
    return render(request, "encyclopedia/edit.html", {
                                "title": title,    
                                "form": form
                            })


def random_page(request):
    entries = util.list_entries()
    random_title = choice(entries)
    return redirect("encyclopedia:entry", title=random_title)


    

        
