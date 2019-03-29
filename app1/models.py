from django.db import models

# Create your models here.
class customer(models.Model):
	c_id=models.CharField(max_length=50)
	c_name=models.CharField(max_length=50)

	def __str__(self):
		return self.c_id+" "+self.c_name


# >>> from app1.models import customer
# >>> customer.objects.create(c_id="101",c_name="meet")
# <customer: 101 meet>
# >>> customer.objects.create(c_id="102",c_name="ujjawal")
# <customer: 102 ujjawal>
# >>> customer.objects.create(c_id="103",c_name="smit")
# <customer: 103 smit>