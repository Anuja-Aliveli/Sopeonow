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
     'time': seconds_to_hhmm(data['cons_done']['time']),
    'count': data['cons_done']['count'],
    'time_color': 'green-color-2'
  },
]
    return keyMetrics