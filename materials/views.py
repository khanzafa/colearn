from django.shortcuts import render
from .models import Material

# Create your views here.
def materi(request):
    materials = Material.objects.all()
    return render(request, 'materi.html', {
        'materials': materials
    })

def detailMateri(request):
    # material_id = request.GET.get('material_id')
    material_id = 1
    material = Material.objects.get(pk=material_id)
    return render(request, 'detail-materi.html', {
        'material': material
    })
