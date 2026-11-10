from django.urls import path
from .views import*

urlpatterns=[
    path('',home,name='home'),
    path('booking/',booking,name='booking'),
    path('history/',history,name='history'),
    path('support/',support,name='support'),
    path('about/',about,name='about'),
    path('book/<int:id>',book,name='book'),
    path('update_/<int:kd>',update_,name='update_'),
    path('delete/<int:pd>/',delete,name='delete')
]