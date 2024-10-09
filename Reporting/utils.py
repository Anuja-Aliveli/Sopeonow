def getKeyMetrics(data):
    keyMetrics = [
  {
    'caption': 'Queue to Registration',
    'name': 'Registration Time',
    'time': data['registration']['time'],
    'count': data['registration']['count'],
  },
  {
    'caption': 'Registration to Triage',
    'name': 'Time to Triage',
    'time': data['triage_done']['time'],
    'count': data['triage_done']['count'],
  },
  {
    'caption': 'Triage to Consult',
    'name': 'Time to Consult',
    'time': data['triage_waiting']['time'],
    'count': data['triage_waiting']['count'],
  },
  {
    'caption': 'Triage End to Discharge',
    'name': 'In Zone Time',
     'time': data['in_zone']['time'],
    'count': data['in_zone']['count'],
  },
  {
    'caption': 'Consultation to Discharge',
    'name': 'Treatment Time',
     'time': data['treatment']['time'],
    'count': data['treatment']['count'],
  },
  {
    'caption': 'Lab Order Request to Processing',
    'name': 'Lab Processing Time',
     'time': data['cons_waiting']['time'],
    'count': data['cons_waiting']['count'],
  },
  {
    'caption': 'Radiology Order Request to Processing',
    'name': 'Radiology Processing Time',
     'time': data['cons_done']['time'],
    'count': data['cons_done']['count'],
  },
  {
    'caption': 'UCC Discharge to IP Bed Allotment',
    'name': 'IP Transfers',
     'time': data['cons_done']['time'],
    'count': data['cons_done']['count'],
  },
]
    return keyMetrics