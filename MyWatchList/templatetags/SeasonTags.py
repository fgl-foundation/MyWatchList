from django import template

from MyWatchList.models import WatchList, SeriesList
from Profile.models import Friendlist

register = template.Library()

@register.inclusion_tag("Serials/blocks/Friends.html")
def friendListS(profile,season):
    return {
        'friends': WatchList.objects.filter(
            user__in=Friendlist.friends.get_friends(profile),
            season=season
        ).order_by('user__first_name')
    }

@register.inclusion_tag("Serials/blocks/SeriesList.html")
def serieslist(season):
    return {
        'episodes': SeriesList.objects.filter(season=season)
            .order_by('date')
    }