from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Workout

# comment

def home(request):
    total_workouts = Workout.objects.all().count()
    context = {
        'total_workouts': total_workouts
    }
    return render(request, 'workouts/home.html', context)


def overview(request):
    return render(request, 'workouts/overview.html', {'title': 'Overview'})


def search(request):
    target = ''
    results = ''
    total = ''
    workouts = Workout.objects.all()

    if 'search' in request.GET:
        query = request.GET.get('search')
        queryset = workouts.filter(Q(name__icontains=query))
        results = queryset

    if request.GET.get('Chest'):
        results = queryset.filter(Q(target__name__icontains='Chest'))
        target = 'Chest'
    elif request.GET.get('Back'):
        results = queryset.filter(Q(target__name__icontains='Back'))
        target = 'Back'
    elif request.GET.get('Legs'):
        results = queryset.filter(Q(target__name__icontains='Legs'))
        target = 'Legs'
    elif request.GET.get('Shoulders'):
        results = queryset.filter(Q(target__name__icontains='Shoulders'))
        target = 'Shoulders'
    elif request.GET.get('Triceps'):
        results = queryset.filter(Q(target__name__icontains='Triceps'))
        target = 'Triceps'
    elif request.GET.get('Biceps'):
        results = queryset.filter(Q(target__name__icontains='Biceps'))
        target = 'Biceps'
    elif request.GET.get('Full'):
        results = queryset.filter(Q(target__name__icontains='Full'))
        target = 'Full'
    elif request.GET.get('Warmups'):
        results = queryset.filter(Q(target__name__icontains='Warmups'))
        target = 'Warmups'

    total = results.count()

    paginator = Paginator(results, 6)
    page = request.GET.get("page")
    try:
        results = paginator.page(page)
    except PageNotAnInteger:
        results = paginator.page(1)
    except EmptyPage:
        results = paginator.page(paginator.num_pages)

    context = {
        'target': target,
        'results': results,
        'query': query,
        'total': total,
    }

    return render(request, 'workouts/search.html', context)


def detail(request, slug):
    workout = get_object_or_404(Workout, slug=slug)
    target = workout.target.name
    context = {
        'workout': workout,
        'target': target,
    }
    return render(request, 'workouts/detail.html', context)
