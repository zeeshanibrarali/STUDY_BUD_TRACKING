from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True)

    avatar = models.ImageField(null=True, default="avatar.svg")
    REQUIRED_FIELDS = []


class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    participants = models.ManyToManyField(User, related_name='participants', blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.name


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.body[0:50]


class Role(models.Model):
    role_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class UserRole(models.Model):
    user_role_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)


class Administrator(models.Model):
    admin_id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)


class Trainer(models.Model):
    trainer_id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    expertise_area = models.CharField(max_length=200)


class Organization(models.Model):
    org_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Habit(models.Model):
    habit_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name


class UserHabit(models.Model):
    user_habit_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()


class Goal(models.Model):
    goal_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    target_date = models.DateField()
    is_completed = models.BooleanField(default=False)


class EducationalResource(models.Model):
    resource_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    file_url = models.URLField()


class CommunityInteraction(models.Model):
    interaction_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    interaction_date = models.DateTimeField()


class ActivityCategory(models.Model):
    activity_category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class ActivityLog(models.Model):
    activity_log_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_category = models.ForeignKey(ActivityCategory, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    additional_info = models.TextField()

    def __str__(self):
        return self.activity_category


class MetricName(models.Model):
    metric_name_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class ActivityMetrics(models.Model):
    activity_metrics_id = models.AutoField(primary_key=True)
    activity_log = models.ForeignKey(ActivityLog, on_delete=models.CASCADE)
    metric_name = models.ForeignKey(MetricName, on_delete=models.CASCADE)
    metric_value = models.FloatField()
