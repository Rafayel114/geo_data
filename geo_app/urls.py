from django.urls import path
from .views import UploadFileView, JSONDataView, HTMLDataView


urlpatterns = [
    path('upload/', UploadFileView.as_view(), name='upload'),
    path('data/json/', JSONDataView.as_view(), name='json-data'),
    path('data/html/', HTMLDataView.as_view(), name='html-data'),
]