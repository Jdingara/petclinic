from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Owner, Pet, Vet
from .forms import OwnerForm, PetForm, VisitForm


def home(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return render(request, 'clinic/home.html')


@login_required
def owner_list(request):
    query = request.GET.get('q', '')
    owners = Owner.objects.all()
    if query:
        owners = owners.filter(
            Q(first_name__icontains=query) | Q(last_name__icontains=query)
        )
    return render(request, 'clinic/owner_list.html', {'owners': owners, 'query': query})


@login_required
def owner_detail(request, pk):
    owner = get_object_or_404(Owner, pk=pk)
    return render(request, 'clinic/owner_detail.html', {'owner': owner})


@login_required
def owner_create(request):
    if request.method == 'POST':
        form = OwnerForm(request.POST)
        if form.is_valid():
            owner = form.save()
            return redirect('owner_detail', pk=owner.pk)
    else:
        form = OwnerForm()
    return render(request, 'clinic/owner_form.html', {'form': form, 'title': 'Add Owner'})


@login_required
def owner_edit(request, pk):
    owner = get_object_or_404(Owner, pk=pk)
    if request.method == 'POST':
        form = OwnerForm(request.POST, instance=owner)
        if form.is_valid():
            form.save()
            return redirect('owner_detail', pk=owner.pk)
    else:
        form = OwnerForm(instance=owner)
    return render(request, 'clinic/owner_form.html', {'form': form, 'title': 'Edit Owner'})


@login_required
def pet_create(request, owner_pk):
    owner = get_object_or_404(Owner, pk=owner_pk)
    if request.method == 'POST':
        form = PetForm(request.POST)
        if form.is_valid():
            pet = form.save(commit=False)
            pet.owner = owner
            pet.save()
            return redirect('owner_detail', pk=owner.pk)
    else:
        form = PetForm()
    return render(request, 'clinic/pet_form.html', {'form': form, 'owner': owner})


@login_required
def visit_create(request, pet_pk):
    pet = get_object_or_404(Pet, pk=pet_pk)
    if request.method == 'POST':
        form = VisitForm(request.POST)
        if form.is_valid():
            visit = form.save(commit=False)
            visit.pet = pet
            visit.save()
            return redirect('owner_detail', pk=pet.owner.pk)
    else:
        form = VisitForm()
    return render(request, 'clinic/visit_form.html', {'form': form, 'pet': pet})


def vet_list(request):
    vets = Vet.objects.prefetch_related('specialties').all()
    return render(request, 'clinic/vet_list.html', {'vets': vets})
