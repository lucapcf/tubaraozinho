from django.urls import path
from .views import make_investment, invested, accept_investment

app_name = 'investments'

urlpatterns = [
    path('make_investment/<int:idea_id>/', make_investment, name='make_investment'),
    path('invested/', invested, name='invested'),
    path('accept_investment/<int:investment_id>/', accept_investment, name='accept_investment'),
]