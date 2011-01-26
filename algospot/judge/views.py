from annoying.decorators import render_to
from models import Problem, Submission, PROBLEM_STATES, SUBMISSION_STATES
from django.core.paginator import Paginator

PROBLEMS_PER_PAGE = 25

@render_to("index.html")
def index(request):
    return {}

@render_to("problem_list.html")
def listproblems(request):
    all = Problem.objects.filter(state=PROBLEM_STATES["PUBLISHED"])
    all = all.order_by("key")

    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        page = 1

    paginator = Paginator(all, PROBLEMS_PER_PAGE)
    return {"page": paginator.page(page)}
