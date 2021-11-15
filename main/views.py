from django.shortcuts import render, HttpResponse, redirect
from .models import ToDo, ToMeet, Habits


def test(request):
    return render(request, "test.html")


def homepage(request):
    todo_list = ToDo.objects.all()
    return render(request, "index.html", {"todo_list": todo_list})

def tomeet(request):
    tomeet_list = ToMeet.objects.all()
    return render(request, "to_meet.html", {"tomeet_list": tomeet_list})

def habits(request):
    habits_list = Habits.objects.all()
    return render(request, "habits.html", {"habits_list": habits_list})



def second(request):
    return HttpResponse("test 2 page")


def add_todo(request):
    form = request.POST
    text = form["todo_text"]
    todo = ToDo(text=text)
    todo.save()
    return redirect(homepage)

def add_tomeet(request):
    form = request.POST
    person = form["tomeet_person"]
    to_meet = ToMeet(person=person)
    to_meet.save()
    return redirect(tomeet)

def add_habits(request):
    form = request.POST
    name = form["habits_name"]
    habits_name = Habits(name=name)
    habits_name.save()
    return redirect(habits)

 


def delete_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.delete()
    return redirect(homepage)

def delete_tomeet(request, id):
    to_meet = ToMeet.objects.get(id=id)
    to_meet.delete()
    return redirect(tomeet)

def delete_habits(request, id):
    to_habits = Habits.objects.get(id=id)
    to_habits.delete()
    return redirect(habits)


def mark_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_favorite = True
    todo.save()
    return redirect(homepage)

def mark_tomeet(request, id):
    to_meet = ToMeet.objects.get(id=id)
    to_meet.is_favorite = True
    to_meet.save()
    return redirect(tomeet)

def mark_habits(request, id):
    to_habits = Habits.objects.get(id=id)
    to_habits.important = True
    to_habits.save()
    return redirect(habits)

def unmark_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_favorite = False
    todo.save()
    return redirect(homepage)

def unmark_tomeet(request, id):
    to_meet = ToMeet.objects.get(id=id)
    to_meet.is_favorite = False
    to_meet.save()
    return redirect(tomeet)

def unmark_habits(request, id):
    to_habits = Habits.objects.get(id=id)
    to_habits.important = False
    to_habits.save()
    return redirect(habits)


def close_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_closed = not todo.is_closed
    todo.save()
    return redirect(homepage)

def close_tomeet(request, id):
    to_meet = ToMeet.objects.get(id=id)
    to_meet.is_closed = not to_meet.is_closed
    to_meet.save()
    return redirect(tomeet)

def close_habits(request, id):
    to_habits = Habits.objects.get(id=id)
    to_habits.done_for_today = not to_habits.done_for_today
    to_habits.save()
    return redirect(habits)










    # form = request.POST
    # person = form["tomeet_person"]
    # to_meet = ToMeet(person=person)
    # to_meet.save()
    # return redirect(to_meet)