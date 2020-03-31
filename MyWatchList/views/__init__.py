from . import film,series,list

from . import addmovie


from django.shortcuts import render
from Profile.models import Friendlist
from django.db.models import Q
from List.views.feed import getFeed

def index(request):
    data={

    }

    if request.user.is_authenticated:
        profile=request.user.profile
        myfriends=Friendlist.objects.filter(Q(accepter=profile) | Q(sender=profile))
        data.update({
            "friends":{
                "friends":myfriends.filter(status=1).count(),
                "requests":myfriends.filter(status=0).count()
            }
        })

        feed=[profile]
        for freind in myfriends.filter(status=1):
            freindprofile=freind.getnotMyprofile(profile)
            if freindprofile:
                feed.append(freindprofile)

        data.update({"feed":getFeed(feed)})

    return render(request, "Main/index.html", data)
