from django.shortcuts import render, redirect
from .models import Donor
from .forms import DonorForm
from django.db.models import Q

def register_donor(request):
    if request.method == 'POST':
        form = DonorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('match_donor')
    else:
        form = DonorForm()
    return render(request, 'register_donor.html', {'form': form})

def match_donor(request):
    hla_a = request.GET.get('hla_a', '')
    hla_b = request.GET.get('hla_b', '')
    hla_c = request.GET.get('hla_c', '')
    hla_drb1 = request.GET.get('hla_drb1', '')
    
    if hla_a and hla_b and hla_c and hla_drb1:
        # Filtering for exact matches or partial matches based on HLA types
        matches = Donor.objects.filter(
            Q(hla_a=hla_a) & 
            Q(hla_b=hla_b) &
            Q(hla_c=hla_c) &
            Q(hla_drb1=hla_drb1)
        )
    else:
        matches = None

    return render(request, 'match_donor.html', {'matches': matches})
