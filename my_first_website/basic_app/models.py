from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

class Pricing(models.Model):
    plan_name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    features = models.TextField()

    def __str__(self):
        return self.plan_name

class Testimonial(models.Model):
    client_name = models.CharField(max_length=100)
    message = models.TextField() # ضيف السطر ده هنا عشان النص يظهر فوق

    def __str__(self):
        return self.client_name

class ContactMessage(models.Model):
    name = models.CharField(max_length=100, verbose_name="Name") # رجعه name هنا
    email = models.EmailField(verbose_name="Email")
    subject = models.CharField(max_length=200, verbose_name="Subject")
    message = models.TextField(verbose_name="Message")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name