
from django.urls import path

from searchapi.views import RecordListView


record_list = RecordListView.as_view({
    'get':'list',
    'post':'create'
})

urlpatterns = [
    path('records/', record_list, name="Record List"),
]
