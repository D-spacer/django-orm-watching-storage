from datacenter.models import Passcard, Visit, get_duration, find_fraud
from django.shortcuts import render
from django.shortcuts import get_object_or_404

def passcard_info_view(request, passcode):
	passcard = get_object_or_404(Passcard, passcode=passcode)
	user_visits = Visit.objects.filter(passcard=passcard)
	this_passcard_visits = []
	for visit in user_visits:
		visit_details = {
			'entered_at': visit.entered_at,
			'duration': get_duration(visit),
			'is_strange': find_fraud(get_duration(visit))
		}
		this_passcard_visits.append(visit_details)
	context = {
			'passcard': passcard,
			'this_passcard_visits': this_passcard_visits
		}
	return render(request, 'passcard_info.html', context)