from django.shortcuts import render
import json
import os
from django.conf import settings

from Reporting.templatetags.time_tags import seconds_to_hhmm
from Reporting.utils import getKeyMetrics

def renderHtml(request):
    json_file_path = os.path.join(settings.MEDIA_ROOT, 'management.json')

    with open(json_file_path, 'r') as json_file:
        management_data = json.load(json_file)
        management_data['visits'] = {
            'count' : management_data['key_metrics']['total']['count'],
            'time' : seconds_to_hhmm(management_data['key_metrics']['registration']['time'])
        }
        management_data['key_metrics'] = getKeyMetrics(management_data['key_metrics'])
    return render(request, 'index.html', {'management_data': management_data})