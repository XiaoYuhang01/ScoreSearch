from django.db import models

# Create your models here.

class CourseScore(models.Model):
    # def __str__(self):
        """
            重写__str__方法，这样只要打印这个相关的都会显示课程名
        """
        # return f'记录号:{self.id}--------学号:{self.id_student}--------课程名:{self.name_course}--------授课教师:{self.professor}'
        # return f'{self.id}'

        # id 记录号
        id = models.AutoField(primary_key = True)
        # id_student（主键）学号
        id_student = models.IntegerField()
        # name_course课程名
        name_course = models.TextField()
        # college开课学院
        college = models.TextField()
        # professor授课教师名
        professor = models.TextField()
        # score给分
        score = models.IntegerField()