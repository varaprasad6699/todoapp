from django.urls import path
from todo.views import addData,UpdateData,DeleteData,userdata
urlpatterns = [
    path('adddata/',addData),
    path('userdata/',userdata),
    path('updatedata/<pk>',UpdateData.as_view(),name='update'),
    path('deletedata/<pk>',DeleteData.as_view(),name='delete')
]
    