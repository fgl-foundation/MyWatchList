from django.db import models
from Main.models import UserListF,UserListS
from Profile.models import Profile
from datetime import datetime

class UserFeed(models.Model):
    user=models.ForeignKey(Profile,on_delete=models.CASCADE)
    userlistS=models.ForeignKey(UserListS,on_delete=models.CASCADE,null=True)
    userlistF=models.ForeignKey(UserListF,on_delete=models.CASCADE,null=True)
    @property
    def list(self):
        if self.userlistS:
            return self.userlistS
        else:
            return self.userlistF 

    @property
    def is_lasthour(self):
        from django.utils.timezone import make_aware
        return (make_aware(datetime.now())-self.created).seconds < 3600

    created = models.DateTimeField(auto_now_add=True)

    action = models.TextField()

    typeAction = models.TextField(null=True)