from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Schedule
from .models import Experience
def home(request):
    return render(request, 'home.html')


def login_page(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect('/dashboard/')

        return render(
            request,
            'login.html',
            {'error': 'Invalid Username or Password'}
        )

    return render(request, 'login.html')


def register_page(request):

    if request.method == "POST":

        username = request.POST.get("username")

        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            return render (
                request,
                'register.html',
                {'error':'Username already exists'}
            )

        User.objects.create_user(
            username=username,
            password=password
        )

        return redirect('/login/')

    return render(request, 'register.html')


@login_required(login_url='/login/')
def dashboard(request):

    schedules = Schedule.objects.filter(
        user=request.user
    )

    experiences = Experience.objects.filter(
        user=request.user
    )

    context = {

        'schedules': schedules,

        'experiences': experiences,

    }

    return render(
        request,
        'dashboard.html',
        context
    )
def logout_page(request):

    logout(request)

    return redirect('/login/')

@login_required(login_url='/login/')
def add_schedule(request):

    if request.method == "POST":

        company_name = request.POST.get("company_name")
        role = request.POST.get("role")
        round_type = request.POST.get("round_type")
        date = request.POST.get("date")
        time = request.POST.get("time")

        Schedule.objects.create(
            user=request.user,
            company_name=company_name,
            role=role,
            round_type=round_type,
            date=date,
            time=time
        )

        return redirect('/dashboard/')

    return render(request, 'add_schedule.html')

@login_required(login_url='/login/')
def publish_experience(request):

    if request.method == "POST":

        company_name = request.POST.get("company_name")

        role = request.POST.get("role")

        round_type = request.POST.get("round_type")

        focus_subject = request.POST.get("focus_subject")

        experience = request.POST.get("experience")

        Experience.objects.create(
            user=request.user,
            company_name=company_name,
            role=role,
            round_type=round_type,
            focus_subject=focus_subject,
            experience=experience
        )

        return redirect('/dashboard/')

    return render(
        request,
        'publish_experience.html'
    )

@login_required(login_url='/login/')
def search_company(request):

    company = request.GET.get('company')

    roles = Experience.objects.filter(
        company_name__icontains=company
    ).values('role').distinct()

    return render(
        request,
        'search_results.html',
        {
            'company': company,
            'roles': roles
        }
    )

@login_required(login_url='/login/')
def role_page(request, role):

    rounds = Experience.objects.filter(
        role=role
    ).values('round_type').distinct()

    return render(
        request,
        'role_page.html',
        {
            'role': role,
            'rounds': rounds
        }
    )

@login_required(login_url='/login/')
def round_page(request, role, round_type):

    experiences = Experience.objects.filter(
        role=role,
        round_type=round_type
    )

    context = {
        'role': role,
        'round_type': round_type,
        'experiences': experiences
    }

    return render(
        request,
        'round_page.html',
        context
    )

@login_required(login_url='/login/')
def experience_page(
    request,
    role,
    round_type,
    focus_subject
):

    experiences = Experience.objects.filter(

        role=role,

        round_type=round_type,

        focus_subject=focus_subject

    )

    context = {

        'role': role,

        'round_type': round_type,

        'focus_subject': focus_subject,

        'experiences': experiences

    }

    return render(
        request,
        'experience_page.html',
        context
    )

@login_required(login_url='/login/')
def edit_experience(request, id):

    experience = Experience.objects.get(
        id=id,
        user=request.user
    )

    if request.method == "POST":

        experience.company_name = request.POST.get('company_name')
        experience.role = request.POST.get('role')
        experience.round_type = request.POST.get('round_type')
        experience.focus_subject = request.POST.get('focus_subject')
        experience.experience = request.POST.get('experience')

        experience.save()

        return redirect('/dashboard/')

    return render(
        request,
        'edit_experience.html',
        {'experience': experience}
    )
@login_required(login_url='/login/')
def delete_experience(request, id):

    experience = Experience.objects.get(
        id=id,
        user=request.user
    )

    experience.delete()

    return redirect('/dashboard/')