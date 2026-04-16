from django.urls import path
from . import views

urlpatterns = [
    path('prompts/', views.list_prompts),
    path('prompts/<uuid:id>/', views.get_prompt),
    path('prompts/create/', views.create_prompt),
]


from django.urls import path, include

urlpatterns = [
    path('', include('prompts.urls')),
]