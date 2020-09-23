from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.view_bag, name='view_bag'),
    path('add/<item_id>', views.add_to_bag, name='add_to_bag'),
    path('add_plan/<item_id>', views.add_plan_to_bag, name='add_plan_to_bag'),
    path('adjust/<item_id>/', views.adjust_bag, name='adjust_bag'),
    path('remove/<item_id>/', views.remove_from_bag, name='remove_from_bag'),
    path('remove_plan/<item_id>/', views.remove_plan_from_bag,
         name='remove_plan_from_bag'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
