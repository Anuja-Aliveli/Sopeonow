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
            'color': '#8B4367',
            'timer': 'green-color-1'
        },
        {
            'icon': 'fa-wallet',
            'name': 'Self Pay',
            'count': data['Payor']['Self_Pay']['count'],
            'time': seconds_to_hhmm(data['Payor']['Self_Pay']['time']),
            'bg': '#DDD7E033',
            'color': '#543864',
            'timer': 'red-color-1'
        },
        {
            'icon': 'fa-earth-oceania',
            'name': 'International',
            'count': data['Residency']['International']['count'],
            'time': seconds_to_hhmm(data['Residency']['International']['time']),
            'bg' : '#F8F8FF80',
            'color': '#343571',
            'timer': 'red-color-1'
        },
        {
            'icon': 'fa-location-dot',
            'name': 'Local',
            'count': data['Residency']['Local']['count'],
            'time': seconds_to_hhmm(data['Residency']['Local']['time']),
            'bg': '#EEEEEE80',
            'color': '#555555',
            'timer': 'green-color-2'
        }
    ]
    return completedData

def getZoneData(data):
    zoneData = {
            'zone_stats': [
                {
                    'icon': 'fa-users',
                    'name': 'Total Visits',
                },
                {
                    'icon': 'fa-timeline',
                    'name': 'Active',
                },{
                    'icon': 'fa-suitcase-rolling',
                    'name': 'Discharged',
                },{
                    'icon': 'fa-stopwatch',
                    'name': 'Average Triage Time',
                },{
                    'icon': 'fa-stopwatch-20',
                    'name': 'Average Hold time',
                },{
                    'icon': 'fa-user-clock',
                    'name': 'Average Visit Time',
                }
                ],
            'green_zone': [
                {'key': 'total_visits_count', 'count': data['green']['total_visits_count'], 'color': ''},
                {'key': 'active_count', 'count': data['green']['active_count'], 'color': ''},
                {'key': 'discharge_count', 'count': data['green']['discharge_count'], 'color': ''},
                {'key': 'avg_triage_tm', 'count': seconds_to_hhmm(data['green']['avg_triage_tm']), 'color': 'green-color-2'},
                {'key': 'avg_visit_tm', 'count': seconds_to_hhmm(data['green']['avg_visit_tm']), 'color': 'red-color-2'},
                {'key': 'avg_cons_tm', 'count': seconds_to_hhmm(data['green']['avg_cons_tm']), 'color': 'green-color-2'}
                ],
            'yellow_zone': [
                {'key': 'total_visits_count', 'count': data['yellow']['total_visits_count'], 'color': ''},
                {'key': 'active_count', 'count': data['yellow']['active_count'], 'color': ''},
                {'key': 'discharge_count', 'count': data['yellow']['discharge_count'], 'color': ''},
                {'key': 'avg_triage_tm', 'count': seconds_to_hhmm(data['yellow']['avg_triage_tm']), 'color': 'red-color-1'},
                {'key': 'avg_visit_tm', 'count': seconds_to_hhmm(data['yellow']['avg_visit_tm']), 'color': 'red-color-2'},
                {'key': 'avg_cons_tm', 'count': seconds_to_hhmm(data['yellow']['avg_cons_tm']), 'color': 'green-color-1'}
                ],
            'red_zone': [
                {'key': 'total_visits_count', 'count': data['red']['total_visits_count'], 'color': ''},
                {'key': 'active_count', 'count': data['red']['active_count'], 'color': ''},
                {'key': 'discharge_count', 'count': data['red']['discharge_count'], 'color': ''},
                {'key': 'avg_triage_tm', 'count': seconds_to_hhmm(data['red']['avg_triage_tm']), 'color': 'red-color-1'},
                {'key': 'avg_visit_tm', 'count': seconds_to_hhmm(data['red']['avg_visit_tm']), 'color': 'green-color-1'},
                {'key': 'avg_cons_tm', 'count': seconds_to_hhmm(data['red']['avg_cons_tm']), 'color': 'green-color-2'}
            ]

        }
    return zoneData

def doctor_chart_config(data):
    doctor_data = data['barline-1']
    
    chart_options = {
        "chart": {
            "type": "line",
            "height": 250
        },
        "series": [
            {
                "name": series["name"],
                "type": series["type"],
                "data": series["data"]
            }
            for series in doctor_data["y"]
        ],
        "stroke": {
            "width": [4 if series["type"] == "line" else 0 for series in doctor_data["y"]]
        },
        "title": {
            "text": doctor_data["title"]
        },
        "xaxis": {
            "categories": doctor_data["x"]
        },
        "yaxis": [
            {
                "title": {
                    "text": series["name"]
                },
                "opposite": index != 0
            }
            for index, series in enumerate(doctor_data["y"])
        ]
    }
    
    return chart_options

def zone_charts_config(data):
    zone_data = data['barpie-1']
    
    config = {
        "chart": {
            "type": 'line',
            "height": 250
        },
        "series": [
            {
                "name": series["name"],
                "type": series["type"],
                "data": series["data"]
            }
            for series in zone_data["bar"]["y"]
        ] + [{
            "name": "Donut",
            "type": "donut",
            "data": zone_data["pie"]["y"]
        }],
        "labels": zone_data["pie"]["x"],
        "stroke": {
            "width": [0, 4, 0] 
        },
        "title": {
            "text": zone_data["title"]
        },
        "xaxis": {
            "categories": zone_data["bar"]["x"]
        },
        "yaxis": [
            {
                "title": {
                    "text": "Total Patients"
                }
            },
            {
                "opposite": True,
                "title": {
                    "text": "Average Time"
                }
            }
        ],
        "plotOptions": {
            "bar": {
                "columnWidth": "50%"
            },
            "pie": {
                "donut": {
                    "size": "65%",
                    "labels": {
                        "show": True,
                        "name": {
                            "show": True
                        },
                        "value": {
                            "show": True
                        }
                    }
                }
            }
        },
        "tooltip": {
            "y": {
                "formatter": "function (value, { series, seriesIndex, dataPointIndex, w }) { "
                             "var time = " + str(zone_data['pie']['time']) + ";"
                             "if (seriesIndex === 2) { "  
                             "    return value + ' (' + time[dataPointIndex] + ' mins)'; "
                             "} "
                             "return value; "
                             "}"
            }
        }
    }
    
    return config


def triage_chart_config(data):
    triage_data = data['comparison-1']
    
    config = {
        "chart": {
            "type": 'line',
            "height": 350
        },
        "series": [
            {
                "name": series["name"] + " (Count)",
                "type": series["type"],
                "data": series["data"]
            }
            for series in triage_data["y"]
        ],
        "stroke": {
            "width": [0, 4, 0, 4],  # 0 for columns, 4 for lines
            "curve": 'smooth'
        },
        "title": {
            "text": triage_data["title"]
        },
        "xaxis": {
            "categories": triage_data["x"]
        },
        "yaxis": [
            {
                "title": {
                    "text": "Count"
                }
            },
            {
                "opposite": True,
                "title": {
                    "text": "Time (minutes)"
                }
            }
        ],
        "colors": ['#008FFB', '#00E396', '#FEB019', '#FF4560'],
        "dataLabels": {
            "enabled": False
        },
        "markers": {
            "size": 5
        },
        "legend": {
            "position": 'top'
        },
        "tooltip": {
            "shared": True,
            "intersect": False,
            "y": {
                "formatter": "function (y, { series, seriesIndex, dataPointIndex, w }) { "
                             "if (seriesIndex % 2 === 0) { "
                             "    return y.toFixed(0) + ' patients'; "
                             "} else { "
                             "    return y.toFixed(0) + ' minutes'; "
                             "} "
                             "}"
            }
        }
    }
    
    return config
