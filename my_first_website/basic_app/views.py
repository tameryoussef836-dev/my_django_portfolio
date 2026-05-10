from django.shortcuts import render
from django.http import JsonResponse
from .models import Service, Pricing, Testimonial
from .forms import ContactForm  # استدعاء الفورم الجديدة


def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # ديجانجو هيسيف الداتا في سطر واحد!
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors})

    # جلب البيانات للعرض في الصفحة
    services = Service.objects.all()
    prices = Pricing.objects.all()
    reviews = Testimonial.objects.all()

    context = {
        'services': services,
        'prices': prices,
        'reviews': reviews,
    }
    return render(request, 'index.html', context)