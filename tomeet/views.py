from django.shortcuts import render, HttpResponse, redirect
from .models import ToMeet


def homepage(request):
    return render(request, "index.html")


def test(request):
    tomeet_list = ToMeet.objects.all()
    return render(request, "test.html", {"todo_list": todo_list})

def test(request):
    todo_list = ToMeet.objects.all()
    return render(request, "to_meet.html", {"tomeet_list": tomeet_list})


def add_tomeet(request):
    form = request.POST
    person = form["tomeet_person"]
    to_meet = ToMeet(person=person)
    to_meet.save()
    return redirect(to_meet)


def delete_tomeet(request, id):
    tomeet = ToMeet.objects.get(id=id)
    tomeet.delete()
    return redirect(test)


def mark_tomeet(request, id):
    tomeet = ToMeet.objects.get(id=id)
    tomeet.is_favorite = True
    tomeet.save()
    return redirect(test)


def close_tomeet(request, id):
    tomeet = ToMeet.objects.get(id=id)
    tomeet.is_closed = not tomeet.is_closed
    tomeet.save()
    return redirect(test)