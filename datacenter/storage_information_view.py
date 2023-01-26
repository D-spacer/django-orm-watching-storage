from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from datacenter.models import format_duration, get_duration



def storage_information_view(request):
	in_storage = Visit.objects.filter(leaved_at__isnull=True)
	non_closed_visits = []
	for visit in in_storage:
		visit_details = {
			'who_entered': visit.passcard,
			'entered_at': visit.entered_at,
			'duration': format_duration(get_duration(visit))
		}
		non_closed_visits.append(visit_details)
	context = {
		'non_closed_visits': non_closed_visits
	}
	return render(request, 'storage_information.html', context)
