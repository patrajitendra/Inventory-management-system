from django.db import models



class Devices(models.Model):

    type=models.CharField(max_length=100,blank=False)
    price=models.IntegerField()

    choices={
        ('AVAILABLE',"Item ready to be Purchaged"),
        ("SOLD","Item sold"),
        ("RESTOCKING","Item restocking in few days")
    }

    status=models.CharField(max_length=100,choices=choices,default="SOLD")
    issues=models.CharField(max_length=100,default="No Issues")

    class Meta():
        abstract=True #for hidden the child class Model rest of shows


    def __str__(self):

        return 'Type:{0} Price:{1}'.format(self.type,self.price)


class Laptop(Devices):
    pass


class Mobiles(Devices):

    pass


class Desktop(Devices):
    pass


