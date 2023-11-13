from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class CourseList(models.Model):
    title = models.CharField(max_length=128)
    change_date = models.DateTimeField()
    info = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Course(models.Model):
    title = models.CharField(max_length=256)
    subscribers = models.IntegerField()
    info = models.TextField()
    img = models.ImageField(upload_to='courses/', null=True, blank=True)
    list = models.ForeignKey(CourseList, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Lesson(models.Model):
    title = models.CharField(max_length=256)
    info = models.TextField()
    img = models.ImageField(upload_to='lessons/', null=True, blank=True)
    complete_percent = models.IntegerField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)


class LessonTask(models.Model):
    task = models.CharField(max_length=256)
    is_complete = models.BooleanField(default=False)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)


class LessonPart(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)


class LessonLink(models.Model):
    link = models.URLField() 
    part = models.ForeignKey(LessonPart, on_delete=models.CASCADE)


class LessonVideo(models.Model):
    video_url = models.URLField()
    part = models.ForeignKey(LessonPart, on_delete=models.CASCADE)


class LessonArticle(models.Model):
    article = models.TextField()
    part = models.ForeignKey(LessonPart, on_delete=models.CASCADE)


class LessonTest(models.Model):
    title = models.CharField(max_length=256)
    is_completed = models.BooleanField(default=False)
    complete_percent = models.IntegerField()
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class TestQuestion(models.Model):
    question = models.CharField(max_length=1024)
    is_complete = models.BooleanField(default=False)
    test = models.ForeignKey(LessonTest, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class TestAnswer(models.Model):
    answer = models.CharField(max_length=1024)
    is_correct = models.BooleanField(default=False)
    question = models.ForeignKey(TestQuestion, on_delete=models.CASCADE)



