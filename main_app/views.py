from django.shortcuts import render


def index(request):
    user = request.user
    if request.user.is_authenticated:

        if user.groups.filter(name='Brand Manager').exists():
            template = 'managers/manager_index.html'
            context = {"user": user}

        else:
            template = 'creators/creator_index.html'
            context = {"user": user}

    else:
        template = 'main_app/visitor_index.html'
        context = {"user": user}

    return render(request, template, context)

