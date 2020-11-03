from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.db import models
from django.db.utils import IntegrityError

from .models import AllStatesDaily, UsaDaily

import json
from datetime import datetime
from pytz import timezone
est = timezone('EST')

def bulk_insert_or_update(Model: models.Model, data: list):
    '''At this point, I cannot find an efficient solution
        to deal with bulk insert_or_update so this is a workaround
    '''
    try:
        Model.objects.bulk_create(data)
    except IntegrityError:
        for d in data:
            if not Model.objects.filter(
                        **d.get_uniques_as_dict()).exists():
                d.save()

@api_view(['GET'])
def get_states(request):
    '''
    Return states data by date or by latest date in db

    param:
    date: YYYY-MM-DD
    today: 0 or 1
    '''
    date = request.GET.get('date','')
    if request.GET.get('today'):
        latest_date = AllStatesDaily.objects.latest('date').date
        #today = datetime.now(est).strftime('%Y-%m-%d')
        return Response(AllStatesDaily.objects.filter(date=latest_date).values())
    return Response(AllStatesDaily.objects.filter(date=date).values())

@api_view(['POST'])
def states_daily(request):
    '''
    Persist states data to mySQL

    param:
    data: [{}]
    '''
    data = [AllStatesDaily(**d) for d in json.loads(request.body)]
    bulk_insert_or_update(AllStatesDaily, data)
    return Response({"SUCCESS": 'persist data'})

@api_view(['GET'])
def get_usa(request):
    '''
    Return usa data by date or by latest date in db

    param:
    date: YYYY-MM-DD
    today: 0 or 1
    '''
    date = request.GET.get('date','')
    if request.GET.get('today'):
        latest_date = UsaDaily.objects.latest('date').date
        #today = datetime.now(est).strftime('%Y-%m-%d')
        return Response(UsaDaily.objects.filter(date=latest_date).values())
    return Response(UsaDaily.objects.filter(date=date).values())

@api_view(['POST'])
def usa_daily(request):
    '''
    Persist usa data to mySQL

    param:
    data: [{}]
    '''
    data = [UsaDaily(**d) for d in json.loads(request.body)]
    bulk_insert_or_update(UsaDaily, data)
    return Response({"SUCCESS": 'persist data'})
