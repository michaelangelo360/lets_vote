from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save 

# Create your models here.



class Candidate(models.Model):
    nominee_candidate = models.ForeignKey("Nominee",on_delete=models.CASCADE , null= True ,default = None )
    num_of_votes = models.IntegerField(default=0)  # Field to store the vote count

    def __str__(self):
        if self.nominee_candidate:
            return self.nominee_candidate.name
        else:
            return "No nominee"

    

    def update_vote_count(self):
        # Calculate the number of votes and save
        self.num_of_votes = Vote.objects.filter(candidate=self).count()
        self.save()


class Nominee (models.Model):
    name = models.CharField( max_length=50)
    bio = models.CharField( max_length=1024)
    age = models.IntegerField()
    email =models.CharField(max_length=200)
    phone_number = models.CharField(max_length=15)
    image = models.ImageField(upload_to='images/')

    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    awards_category =models.ForeignKey("Category", on_delete=models.CASCADE , related_name = 'nominee')
    #vote_id = models.ForeignKey("Vote", on_delete=models.CASCADE,  related_name = 'vote')


class Event (models.Model):
    name = models.CharField(max_length=200)



    def __str__(self):
        return self.name



class Category (models.Model):

    name = models.CharField(max_length= 200)
    event = models.ForeignKey('Event',on_delete= models.CASCADE)


    def __str__(self):
        return self.name


class Vote(models.Model):
    #nominee = models.OneToOneField(Nominee, on_delete=models.CASCADE, related_name='vote' , default= None , null= True)
    #nominee = models.ManyToManyField("Nominee")



    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE ,null=True, default=None)
    

  
        
    def __str__(self):
        return self.name

 


class Statistic (models.Model):

    total_number = models.IntegerField()
    name_of_stat = models.CharField(max_length = 200)

    def __str__(self):
        return self.name_of_stat



@receiver(post_save, sender=Candidate)
def create_vote(sender, instance, created, **kwargs):
    if created:
        Vote.objects.create(candidate=instance)
