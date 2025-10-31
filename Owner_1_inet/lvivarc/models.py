from django.db import models

class ArcType(models.Model):
    typeName=models.CharField(max_length=60)

    def __str__(self):
        return self.typeName

class  ArcObj(models.Model):

    """Аргітектурні об'єкти    """
    objName = models.CharField(max_length=100)
    objType = models.ForeignKey(ArcType, on_delete=models.CASCADE, default=1)
    descr = models.TextField()
    image = models.ImageField(upload_to="", blank=True)
    curAddr = models.CharField(max_length=60)

    def __str__(self):
        return self.objName