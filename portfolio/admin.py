from django.contrib import admin
from portfolio.models import Education, Experience, Project, Skill


# Register your models here.
@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree', 'school', 'start_date', 'end_date')
    search_fields = ('degree', 'school')
    list_filter = ('degree', 'school')


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'start_date', 'end_date')
    search_fields = ('title', 'company')
    list_filter = ('title', 'company')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'created_at')
    list_filter = ('title', 'created_at')


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'content_type', 'object_id')
    search_fields = ('name', 'content_type', 'object_id')
    list_filter = ('name', 'content_type', 'object_id')
