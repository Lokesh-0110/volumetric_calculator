from django.shortcuts import render
from .forms import ParcelForm

def index(request):
    result = None
    if request.method == 'POST':
        form = ParcelForm(request.POST)
        if form.is_valid():
            q = form.cleaned_data['quantity']
            w = form.cleaned_data['weight']
            l = form.cleaned_data['length']
            d = form.cleaned_data['width']
            h = form.cleaned_data['height']
            unit = form.cleaned_data['unit']

            if unit == 'kg/cm':
                volumetric_weight = (l * d * h) / 5000
            else:  # 'lb/in'
                volumetric_weight = (l * d * h) / 166

            result = max(w, volumetric_weight) * q
    else:
        form = ParcelForm()

    return render(request, 'calculator/index.html', {'form': form, 'result': result})
