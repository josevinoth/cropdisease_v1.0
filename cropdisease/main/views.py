# main/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import UserQuery, DoctorSuggestion
from .forms import UserQueryForm,RegistrationForm

def home(request):

    return render(request, 'home.html')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Change 'home' to your desired home page URL
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

def communication_page(request):
    queries = UserQuery.objects.all()
    suggestions = DoctorSuggestion.objects.all()

    if request.method == 'POST':
        form = UserQueryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('communication_page')
    else:
        form = UserQueryForm()

    return render(request, 'communication_page.html', {'form': form, 'queries': queries, 'suggestions': suggestions})


def edit_query(request, query_id):
    query = get_object_or_404(UserQuery, pk=query_id)

    if request.method == 'POST':
        form = UserQueryForm(request.POST, instance=query)
        if form.is_valid():
            form.save()
            return redirect('communication_page')
    else:
        form = UserQueryForm(instance=query)

    return render(request, 'edit_query.html', {'form': form, 'query': query})


def delete_query(request, query_id):
    query = get_object_or_404(UserQuery, pk=query_id)

    if request.method == 'POST':
        query.delete()
        return redirect('communication_page')

    return render(request, 'delete_query.html', {'query': query})
