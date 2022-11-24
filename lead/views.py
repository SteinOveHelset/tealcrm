from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .forms import AddLeadForm
from .models import Lead

from client.models import Client

@login_required
def leads_list(request):
    leads = Lead.objects.filter(created_by=request.user, converted_to_client=False)

    return render(request, 'lead/leads_list.html', {
        'leads': leads
    })

@login_required
def leads_detail(request, pk):
    lead = get_object_or_404(Lead, created_by=request.user, pk=pk)

    return render(request, 'lead/leads_detail.html', {
        'lead': lead
    })

@login_required
def leads_delete(request, pk):
    lead = get_object_or_404(Lead, created_by=request.user, pk=pk)
    lead.delete()

    messages.success(request, 'The lead was deleted.')

    return redirect('leads_list')

@login_required
def leads_edit(request, pk):
    lead = get_object_or_404(Lead, created_by=request.user, pk=pk)

    if request.method == 'POST':
        form = AddLeadForm(request.POST, instance=lead)

        if form.is_valid():
            form.save()

            messages.success(request, 'The changes was saved.')

            return redirect('leads_list')
    else:
        form = AddLeadForm(instance=lead)
    
    return render(request, 'lead/leads_edit.html', {
        'form': form
    })

@login_required
def add_lead(request):
    if request.method == 'POST':
        form = AddLeadForm(request.POST)

        if form.is_valid():
            lead = form.save(commit=False)
            lead.created_by = request.user
            lead.save()

            messages.success(request, 'The lead was created.')

            return redirect('leads_list')
    else:
        form = AddLeadForm()

    return render(request, 'lead/add_lead.html', {
        'form': form
    })

@login_required
def convert_to_client(request, pk):
    lead = get_object_or_404(Lead, created_by=request.user, pk=pk)

    client = Client.objects.create(
        name=lead.name,
        email=lead.email,
        description=lead.description,
        created_by=request.user,
    )

    lead.converted_to_client = True
    lead.save()

    messages.success(request, 'The lead was converted to a client.')

    return redirect('leads_list')