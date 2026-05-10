from django.contrib import admin
from .models import Service, Pricing, Testimonial, ContactMessage

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    # لو حصل خطأ هنا، تأكد من اسم السعر في الـ models (ممكن يكون service_price مثلاً)
    list_display = ('title',)

@admin.register(Pricing)
class PricingAdmin(admin.ModelAdmin):
    # جرب تخليها كده مؤقتاً لحد ما نتأكد من الأسماء
    list_display = ('plan_name',)

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    # الخطأ بيقول إن customer_name مش موجود، جرب نكتب الاسم اللي في الـ models عندك
    # غالباً أنت مسميه name أو client_name
    list_display = ('client_name',)


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    # الخانات اللي هتظهر في الجدول من بره
    list_display = ('name', 'email', 'subject', 'created_at')

    # إضافة شريط بحث
    search_fields = ('name', 'email', 'subject')

    # إضافة فلتر بالوقت
    list_filter = ('created_at',)

    # ترتيب الرسايل (الأحدث أولاً)
    ordering = ('-created_at',)