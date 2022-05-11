from django.db import models

class User(models.Model):
    # id = models.UUIDField(primary_key=TRUE,default=uuid.uuid4,editable=False)
    username = models.CharField(max_length=255, null=True,default="")
    email = models.EmailField(max_length=255, null=True,default="")
    password = models.CharField(max_length=50)
    ifLogged = models.BooleanField(default=False)
    token = models.CharField(max_length=500, null=True, default="")

    def str(self):
        return "{} -{}".format(self.username, self.email)


class Child(models.Model):
 
    cname = models.CharField(max_length=255, null=False)
    password = models.CharField(max_length=8)
    user_id = models.ForeignKey(User,on_delete = models.DO_NOTHING,null=True,default="")
    def str(self):
        return "{} ".format(self.cname)



class Image(models.Model):
  image1 = models.CharField(max_length=100)
  voice = models.CharField(max_length=100)
  user_id = models.ForeignKey(User,on_delete = models.DO_NOTHING,null=True,default="")

  def str(self):
        return "{} ".format(self.image1)

class Game(models.Model):
  name = models.CharField(max_length=255, null=False)
  score = models.CharField(max_length=100)
  child_id = models.ForeignKey(Child,on_delete = models.DO_NOTHING)
  date=models.DateField(null=True,blank=True)

  def str(self):
        return "{} ".format(self.name)
