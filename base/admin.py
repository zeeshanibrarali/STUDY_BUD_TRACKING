from django.contrib import admin

# Register your models here.

from .models import *
admin.site.register(User)
admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Message)
admin.site.register(Role)
admin.site.register(UserRole)
admin.site.register(Administrator)
admin.site.register(Trainer)
admin.site.register(Organization)
admin.site.register(Habit)
admin.site.register(UserHabit)
admin.site.register(Goal)
admin.site.register(EducationalResource)
admin.site.register(CommunityInteraction)
admin.site.register(ActivityCategory)
admin.site.register(ActivityLog)
admin.site.register(MetricName)
admin.site.register(ActivityMetrics)

