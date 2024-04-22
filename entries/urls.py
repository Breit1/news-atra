from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("", views.EntryListView.as_view(), name="entry-list"),
    path("entry/<int:pk>/", views.EntryDetailView.as_view(), name="entry-detail"),
    path("entry/create/", views.EntryCreateView.as_view(), name="entry-create"),
    path("entries/base_template/", views.base_template, name="base_template"),
    path("entry_detail_anal/<int:pk>/", views.EntryDetailAnalView.as_view(), name="entry_detail_anal"),
    path("stockanalytics/", views.stockanalytics, name="stockanalytics"),
    path("entries/base_template/", views.base_template, name="base_template"), 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

