from django.shortcuts import render
from django.core.serializers import serialize
from django.http import HttpResponse
from .models import CourseScore
import json
# Create your views here.

# Home视图
def Home(request):
    return render(request, 'Cover/index.html',
                  {
                      'Page': "Home",
                  })

# 主视图及切换
def IndexPage(request, page):
    return render(request, 'Cover/index.html',
                  {
                      'Page': page
                  })

# 查询视图
def Query_Condition(request):
    return render(request, 'Query/QueryCondition.html',{})

# 查询结果视图_以课程名做关键字
def Query_Detail_Course(request, course_name):
    print("跑了课程名测试")
    # 使用一个空列表存储符合课程名的课程记录
    course_list = []
    # 如果记录符合课程名，则添加到列表中
    for course_record in CourseScore.objects.all():
        if course_record.name_course == course_name:
            course_list.append(course_record)

    # 从列表中选取出教师，构建一个教师字典，{教师名：[课程记录]},初始时只有键没有值，值默认为空列表
    professor_dict = {}
    for course_record_new_p in course_list:
        if course_record_new_p.professor not in professor_dict:
            professor_dict[course_record_new_p.professor] = []

    # 以教师字典里的教师名为索引构建每个教师的该课程给分列表
    for professor in professor_dict:
        for course_record_p in course_list:
            if course_record_p.professor == professor:
                professor_dict[professor].append(course_record_p)

    for course_professor in professor_dict:
        for score_record in professor_dict[course_professor]:
            print(score_record.score)

    print(professor_dict)
    return render(request, 'Query/QueryDetail.html',
                  {
                      'QueryType': 'default',
                      'Dict': professor_dict,
                  })

# 查询结果视图_以教师名做关键字
def Query_Detail_Professor(request, professor):
    print(2)
    # 使用一个空列表存储符合教师名的课程记录
    course_list = []
    # 如果记录符合教师名，则添加到列表中
    for course_record in CourseScore.objects.all():
        if course_record.professor == professor:
            course_list.append(course_record)

    # 从列表中选取出课程，构建一个课程字典，{课程名：[课程记录]},初始时只有键没有值，值默认为空列表
    course_dict = {}
    for course_record_new_c in course_list:
        if course_record_new_c.name_course not in course_dict:
            course_dict[course_record_new_c.name_course] = []

    # 以课程字典里的课程名为索引构建每个课程的该教师给分列表
    for course in course_dict:
        for course_record_c in course_list:
            if course_record_c.name_course == course:
                course_dict[course].append(course_record_c)

    print(course_dict)

    return render(request, 'Query/QueryDetail.html',
                  {
                      'QueryType': 'professor',
                      'Dict': course_dict,
                  })

# 查询结果视图_双关键字
def Query_Detail_Both(request, course_name, professor):
    # 使用一个空列表存储符合课程名与教师名的课程记录
    course_list = []
    # 如果记录符合课程名与教师名，则添加到列表中
    for course_record in CourseScore.objects.all():
        if course_record.name_course == course_name and course_record.professor == professor:
            course_list.append(course_record)
    # 构建一个教师字典
    professor_dict = {}
    # 教师字典只有一项，key是教师名，value是教师对应课程的课程记录列表
    professor_dict[professor] = course_list

    return render(request, 'Query/QueryDetail.html',
                  {
                      'QueryType': 'default',
                      'Dict': professor_dict,
                  })


