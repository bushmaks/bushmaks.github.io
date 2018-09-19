from django.shortcuts import render
from django.utils import timezone
from django.views.generic import list, detail
from creators.models import SocialPlatform, Quote, CreatorProfile
from managers.models import Brand, Campaign


def index(request):
    user = request.user
    if request.user.is_authenticated:

        if user.groups.filter(name="BrandManager").exists():
            manager = request.user.brandmanagerprofile
            template = 'managers/manager_index.html'
            brands = manager.brand_set.all()
            context = {"user": user, "brands": brands, "manager": manager}

        elif user.groups.filter(name="Creator"):
            creator = request.user.creatorprofile
            niches = creator.niches.all()
            platforms = SocialPlatform.objects.filter(creator=creator)
            quotes = Quote.objects.filter(creator=creator)
            template = 'creators/creator_index.html'
            context = {"user": user, "platforms": platforms, "creator": creator, "quotes": quotes, "niches": niches, "Profile":creator }
        else:
            template = 'main_app/visitor_index.html'
            campaigns = Campaign.objects.filter(posted__lte=timezone.now()).order_by('posted')[:5]
            context = {"user": user, "campaigns": campaigns}

    else:
        template = 'main_app/visitor_index.html'
        campaigns = Campaign.objects.filter(posted__lte=timezone.now()).order_by('posted')[:5]
        context = {"user": user, "campaigns": campaigns}

    return render(request, template, context)

def pricing(request):
    user = request.user
    template = 'main_app/pricing.html'
    context = {"user": user}
    return render(request, template, context)


class CampaignListView(list.ListView):
    template_name = 'main_app/campaign_list.html'
    model = Campaign
    paginate_by = 10
    title = 'Campaigns'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class CampaignDetailView(detail.DetailView):
    template_name = 'main_app/campaign_detail.html'
    model = Campaign
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

      
def influencer_view(request):

    influencers=CreatorProfile.user
    creator = request.user.creatorprofile
    
    return render(request, 'main_app/creatorprofile.html', {"Profile": creator})
