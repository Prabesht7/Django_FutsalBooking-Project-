from django.contrib import admin
from .models.tregister import Tournamentregister
from .models.booking import Booking


# Register your models here.
class AdminTournamentregister(admin.ModelAdmin):
    list_display = ['name', 'team_name', 'address', 'number', 'captain_name', 'manager_name', 'one_player',
                    'two_player', 'three_player', 'four_player', 'five_player', 'six_player', 'seven_player'
                    , 'eight_player', 'jersey_color', 'coach_name']

admin.site.register(Tournamentregister , AdminTournamentregister)


class AdminBooking(admin.ModelAdmin):
    list_display = ["fullname"]

admin.site.register(Booking , AdminBooking)
