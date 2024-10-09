from Reporting.templatetags.time_tags import seconds_to_hhmm


def getKeyMetrics(data):
    keyMetrics = [
  {
    'caption': 'Queue to Registration',
    'name': 'Registration Time',
    'time': seconds_to_hhmm(data['registration']['time']),
    'count': data['registration']['count'],
    'time_color': 'red-color-1'
  },
  {
    'caption': 'Registration to Triage',
    'name': 'Time to Triage',
    'time': seconds_to_hhmm(data['triage_done']['time']),
    'count': data['triage_done']['count'],
    'time_color': 'green-color-1'
  },
  {
    'caption': 'Triage to Consult',
    'name': 'Time to Consult',
    'time': seconds_to_hhmm(data['triage_waiting']['time']),
    'count': data['triage_waiting']['count'],
    'time_color': 'green-color-2'
  },
  {
    'caption': 'Triage End to Discharge',
    'name': 'In Zone Time',
     'time': seconds_to_hhmm(data['in_zone']['time']),
    'count': data['in_zone']['count'],
    'time_color': 'red-color-2'
  },
  {
    'caption': 'Consultation to Discharge',
    'name': 'Treatment Time',
     'time': seconds_to_hhmm(data['treatment']['time']),
    'count': data['treatment']['count'],
    'time_color': 'red-color-2'
  },
  {
    'caption': 'Lab Order Request to Processing',
    'name': 'Lab Processing Time',
     'time': seconds_to_hhmm(data['cons_waiting']['time']),
    'count': data['cons_waiting']['count'],
    'time_color': 'red-color-2'
  },
  {
    'caption': 'Radiology Order Request to Processing',
    'name': 'Radiology Processing Time',
     'time': seconds_to_hhmm(data['cons_done']['time']),
    'count': data['cons_done']['count'],
    'time_color': 'red-color-2'
  },
  {
    'caption': 'UCC Discharge to IP Bed Allotment',
    'name': 'IP Transfers',
     'time': seconds_to_hhmm(data['ip_transfers']['completed']['time']),
    'count': data['ip_transfers']['completed']['count'],
    'time_color': 'green-color-2'
  },
]
    return keyMetrics

def getCompletedData(data):
    completedData = [
        {
            'icon': 'fa-umbrella',
            'name': 'Insurance',
            'count': data['Payor']['Insurance']['count'],
            'time': seconds_to_hhmm(data['Payor']['Insurance']['time']),
            'bg': '#E8D9E14D',
            'color': '#8B4367'
        },
        {
            'icon': 'fa-wallet',
            'name': 'Self Pay',
            'count': data['Payor']['Self_Pay']['count'],
            'time': seconds_to_hhmm(data['Payor']['Self_Pay']['time']),
            'bg': '#DDD7E033',
            'color': '#543864'
        },
        {
            'icon': 'fa-earth-oceania',
            'name': 'International',
            'count': data['Residency']['International']['count'],
            'time': seconds_to_hhmm(data['Residency']['International']['time']),
            'bg' : '#F8F8FF80',
            'color': '#343571',
        },
        {
            'icon': 'fa-location-dot',
            'name': 'Local',
            'count': data['Residency']['Local']['count'],
            'time': seconds_to_hhmm(data['Residency']['Local']['time']),
            'bg': '#EEEEEE80',
            'color': '#555555'
        }
    ]
    return completedData