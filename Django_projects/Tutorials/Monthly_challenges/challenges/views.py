from calendar import month_name
from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string


monthly_challenges = {
    "january":"Eat no meat for the entire month!",
    "february":"Walk for at least 20 mins every day!",
    "march":"Learn Django for at least 20 mins every day!",
    "april":"Play Fifa24 twice a week",
    "may":"Walk for at least 20 mins every day!",
    "june":"Visit your parents house",
    "july":"Learn Django for at least 20 mins every day!",
    "august": None,
    "september":"Walk for at least 20 mins every day!",
    "october":"Have Fun and lot of sex",
    "november":"Learn Django for at least 20 mins every day!",
    "december": None
}

# Create your views here.
def index(request):
    months = list(monthly_challenges.keys())
    return render(request, "challenges/index.html", {
        "months": months
    })

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid Month")

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month]) # challenge/january
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        month_name = month.capitalize()
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month_name": month_name
        }) 
    except:
        raise Http404()
        # response_data = render_to_string("404.html")
        # return HttpResponseNotFound(response_data)