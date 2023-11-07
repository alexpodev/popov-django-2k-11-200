from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class CourseList(models.Model):
    course_list_title = models.CharField(max_length=128)
    change_date = models.DateTimeField()
    course_list_info = models.CharField(max_length=1024)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Course(models.Model):
    course_title = models.CharField(max_length=256)
    subscribers = models.IntegerField()
    course_info = models.CharField(max_length=1024)
    course_img = models.ImageField(upload_to='courses/', null=True, blank=True)
    course_list = models.ForeignKey(CourseList)

class Lesson(models.Model):
    lesson_title = models.CharField(max_length=256)
    lesson_info = models.CharField(max_length=1024)
    lesson_img = models.ImageField(upload_to='lessons/', null=True, blank=True)
    complete_percent = models.IntegerField()
    course = models.ForeignKey(Course)

class LessonTask(models.Model):
    task_info = models.CharField(max_length=256)
    is_completed = models.BooleanField(default=False)
    lesson = models.ForeignKey(Lesson)

class LessonLink(models.Model):
    link = models.URLField() 
    lesson = models.ForeignKey(Lesson)

class LessonVideo(models.Model):
    video_url = models.URLField()
    lesson = models.ForeignKey(Lesson)
    
class LessonArticle(models.Model):
    article = models.CharField(max_length=4096)
    lesson = models.ForeignKey(Lesson)

class LessonTest(models.Model):
    test_title = models.CharField(max_length=256)
    is_completed = models.BooleanField(default=False)
    complete_percent = models.IntegerField(max_length=100)
    lesson = models.ForeignKey(Lesson)

class TestQuestion(models.Model):
    question = models.CharField(max_length=1024)
    is_complete = models.BooleanField(default=False)
    test = models.ForeignKey(LessonTest)

class TestAnswer(models.Model):
    answer = models.CharField(max_length=1024)
    is_true = models.BooleanField(default=False)
    question = models.ForeignKey(TestQuestion)



