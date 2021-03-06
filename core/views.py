from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.db import models
import datetime
from datetime import timedelta
from django.views.generic.list import ListView
from django.utils import timezone
from django.utils import formats
from django.db.models.functions import Lower
from django.db.models import Sum
from django.db.models import Count

from leagues.models import Season
from leagues.models import MatchUp
from leagues.models import Stat
from leagues.models import Roster
from leagues.models import Team_Stat
from leagues.models import Week
from leagues.models import Player
# Create your views here.

def home(request):
    context = {}
    # context["season"] = Season.objects.get(is_current_season=1)
    context["season"] = Season.objects.all()
    context["matchup"]  = MatchUp.objects.filter(week__date__range=(datetime.date.today(), datetime.date.today() + timedelta(days=6)))
    context["one_row"]  = MatchUp.objects.filter(week__date__range=(datetime.date.today(), datetime.date.today() + timedelta(days=6))).order_by('week__date').distinct('week__date')
    return render(request, "core/home.html", context=context)

def leagues(request):
    return render(request, "leagues/index.html")


class MatchUpDetailView(ListView):
    context_object_name = 'matchup_list'

    def get_queryset(self):
        return MatchUp.objects.order_by('time')

    def get_context_data(self, **kwargs):
        context = super(MatchUpDetailView, self).get_context_data(**kwargs)
        context["season"] = Season.objects.all()
        context["roster"] = Roster.objects.order_by(Lower('player__last_name'))
        context["stat"] = Stat.objects.all()

        return context

class TeamStatDetailView(ListView):
    context_object_name = 'team_list'

    def get_queryset(self):
        return Team_Stat.objects.order_by('-win','loss','-tie')

    def get_context_data(self, **kwargs):
        context = super(TeamStatDetailView, self).get_context_data(**kwargs)
        # context["season"] = Season.objects.all()
        # context["roster"] = Roster.objects.order_by(Lower('player__last_name'))
        # context["stat"] = Stat.objects.all()

        return context

class PlayerStatDetailView(ListView):
    context_object_name = 'player_stat_list'

    def get_queryset(self):
        return Stat.objects.order_by('-goals','-assists')

    def get_context_data(self, **kwargs):
        context = super(PlayerStatDetailView, self).get_context_data(**kwargs)
        context["stat"] = Stat.objects.all()
        context["sum_goals"] = Player.objects.annotate(sum_goals=Sum('stat__goals'))
        context["sum_assists"] = Player.objects.annotate(sum_assists=Sum('stat__assists'))

        return context

def schedule(request):
    context = {}
    # context["season"] = Season.objects.get(is_current_season=1)
    context["season"] = Season.objects.all()
    context["matchup"]  = MatchUp.objects.order_by('week__date','time')  
    context["game_days"]  = Week.objects.order_by('date').distinct('date')
    return render(request, "leagues/schedule.html", context=context)
        
