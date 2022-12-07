from django.shortcuts import render, redirect
from .forms import SinfForm, DarsForm
from .models import  Sinf, Dars


def main_index(request):
    return render(request, 'main/index.html', {
        "sinflar": Sinf.objects.order_by('id').all()
    })


def main_add_sinf(request):
    form = SinfForm()
    if request.method == 'POST':
        form = SinfForm(data=request.POST)
        if form.is_valid():
            form.save()

            return redirect("main_index")
    return render(request, 'main/sinf.html', {
        "form": form
    })


def main_add_dars(request):
    form = DarsForm()
    if request.method == 'POST':
        form = DarsForm(data=request.POST)
        if form.is_valid():
            form.save()

            return redirect("main_index")
    return render(request, 'main/dars.html',{
        'form': form
    })




def main_dars_jadval(request, sinf_id):
    sinf = Sinf.objects.get(id=sinf_id)

    darslar = Dars.objects.filter(sinf_id=sinf_id).all()

    kunlar = [
        [],
        [],
        [],
        [],
        [],
        [],
        []
    ]

    for dars in darslar:
        kunlar[dars.hafta_kuni -1].append(dars)

    for i in range(len(kunlar)):
        kunlar[i].sort(key=lambda r: r.soat)


    return render(request, 'main/dars_jadval.html', {
        'sinf': sinf,
        'kunlar': kunlar
    })