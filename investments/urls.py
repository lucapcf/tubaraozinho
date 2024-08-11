from django.urls import path
from .views import make_investment, invested, edit_investment

app_name = 'investments'

urlpatterns = [
    path('make_investment/<int:idea_id>/', make_investment, name='make_investment'),
    path('invested/', invested, name='invested'),
    path('edit_investment/<int:investment_id>/', edit_investment, name='edit_investment'),
]