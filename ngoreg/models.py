from django.db import models

class Ngo(models.Model):
    STATUS_CHOICES=(('pending','Pending'),('approved','Approved'))
    STATES=(('mp','mp'),('up','mp'),('rj','rj'),('cg','cg'))
    SPECIALIZATION_CHOICES=(('animal welfare','Animal Welfare'),('arts & culture','Arts & Culture'),('children','Children'),('development','Development'),('disability','Disability'),('education','Education'),('elderly','Elderly'),('environment','Environment'),('governance','Governance'),('health','Health'),('women','Women'),('livelihood','Livelihood'))

    reg_no = models.CharField(max_length=250,unique=True)
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100,choices=SPECIALIZATION_CHOICES)
    location = models.CharField(max_length=100)
    state = models.CharField(max_length=30,choices=STATES)
    city = models.CharField(max_length=30)
    ngo_logo = models.ImageField(upload_to='pics')
    status = models.CharField(max_length=100,choices=STATUS_CHOICES,default='pending')
    address = models.TextField()
    mobile=models.CharField(max_length=15)
    description = models.TextField()
    website=models.CharField(max_length=100)

    def __str__(self):
        return self.reg_no
    
class Review(models.Model):
    ngo = models.ForeignKey(Ngo,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()    
    rating = models.IntegerField()
    comment=models.TextField()
    
class Doner(models.Model):
    ngo=models.ForeignKey(Ngo,on_delete=models.CASCADE)
    dname=models.CharField(max_length=50)
    daddress=models.TextField()
    def __str__(self):
        return self.dname