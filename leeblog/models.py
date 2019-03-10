from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

class Maker(models.Model):
    maker_name = models.CharField(max_length=200)
    brand_name = models.CharField(max_length=200)

    # tj_r = models.CharField(max_length=200)
    # tj_t = models.CharField(max_length=200)

    def __str__(self):
        return self.maker_name+'-'+self.brand_name

    def get_absolute_url(self):
        return reverse('lee:label_index', kwargs={'pk': self.pk})
        # return reverse('lee:post_detail', args=[self.id])

class Label(models.Model):
    maker = models.ForeignKey(Maker, on_delete=models.CASCADE)
    sw_version = models.CharField(max_length=200)
    os_version = models.CharField(max_length=200)
    # mr_number = models.CharField(max_length=200)
    upload_date = models.DateField(auto_now_add=True)
    test_date = models.DateField(null=True)
    # label_file = models.ImageField(upload_to='label/%Y/%m/%d')

    #
    # telec = models.CharField(max_length=200, null=True)
    # fcc = models.CharField(max_length=200, null=True)

    # def get_absolute_url(self):
    #     return reverse_lazy('lee:label_detail', kwargs={'pk': self.pk})

    # class Meta:
    #     ordering = ['-id']

class MultiFileLabel(models.Model):
    label = models.ForeignKey(Label, on_delete=models.CASCADE)
    label_file = models.ImageField(upload_to='label/%Y/%m/%d')






class Recipe(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()


class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)


class Instruction(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    number = models.PositiveSmallIntegerField()
    description = models.TextField()
