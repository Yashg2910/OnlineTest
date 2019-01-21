from django.db import models

# Create your models here.

class CourseModel(models.Model):
    id = models.CharField(max_length=10, primary_key=True, verbose_name="Course ID")
    name = models.CharField(max_length=100, unique=True, verbose_name="Course Name")
    content = models.CharField(max_length=255, verbose_name="Course Content")

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"

    def __str__(self):
        return self.name

class QuestionModel(models.Model):
    id = models.CharField(max_length=10, primary_key=True, verbose_name="Question ID")
    course = models.ForeignKey(CourseModel, on_delete=models.CASCADE)
    opt_a = models.CharField(max_length=255, blank=False, verbose_name="Option A")
    opt_b = models.CharField(max_length=255, blank=False, verbose_name="Option B")
    opt_c = models.CharField(max_length=255, blank=False, verbose_name="Option C")
    opt_d = models.CharField(max_length=255, blank=False, verbose_name="Option D")
    correct_opt = models.CharField(max_length=255, blank=False, verbose_name="Correct Option")

    class Meta:
        verbose_name = "Question"
        verbose_name_plural = "Questions"