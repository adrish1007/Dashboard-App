from django.shortcuts import render
from . models import db_collections

# Create your views here.

# q stands for query

def index(request):
    q1 = db_collections.find({"$and": [{"start_year": {"$nin": ["", None]}},
                                       {"end_year": {"$nin": ["", None]}}]})

    q2 = db_collections.find()[:5]

    q3 = db_collections.find()

    q4 = db_collections.find()[:20]

    topic_occurrences = []

    for insight in q4:
        topic = insight['topic']
        if topic not in [item['topic'] for item in topic_occurrences] and topic != "":
            topic_occurrences.append({'topic': topic, 'count': 1})
        else:
            for item in topic_occurrences:
                if item['topic'] == topic:
                    item['count'] += 1

    q5 = db_collections.find()

    q6 = db_collections.find()

    context = {
        "q1": q1,
        "q2": q2,
        "q3": q3,
        "q4": topic_occurrences,
        "q5": q5,
        "q6": q6
    }

    return render(request, 'chartapp/index.html', context)
