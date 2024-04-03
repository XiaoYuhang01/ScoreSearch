from django.urls import path,include
import Score_Search.views

urlpatterns = [
    path('', Score_Search.views.Home),
    path('Query_Condition', Score_Search.views.Query_Condition),
    path('Query_Detail/课程查询/<str:course_name>', Score_Search.views.Query_Detail_Course),
    path('Query_Detail/教师查询/<str:professor>', Score_Search.views.Query_Detail_Professor),
    path('Query_Detail/默认查询/<str:course_name>/<str:professor>', Score_Search.views.Query_Detail_Both),
    path('<str:page>', Score_Search.views.IndexPage),
]