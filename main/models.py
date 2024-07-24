from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


# Create your models here.
class Education(models.Model):
    degree = models.CharField(max_length=100, verbose_name=_('Degree'))
    school = models.CharField(max_length=100, verbose_name=_('School'))
    start_date = models.DateField(verbose_name=_('Start Date'))
    end_date = models.DateField(verbose_name=_('End Date'))
    description = models.TextField(verbose_name=_('Description'))

    def __str__(self):
        return self.degree

    class Meta:
        verbose_name = _('Education')
        verbose_name_plural = _('Educations')


################################################################################################
class Experience(models.Model):
    title = models.CharField(max_length=100, verbose_name=_('Title'))
    company = models.CharField(max_length=100, verbose_name=_('Company'))
    start_date = models.DateField(verbose_name=_('Start Date'))
    end_date = models.DateField(verbose_name=_('End Date'))
    description = models.TextField(verbose_name=_('Description'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Experience')
        verbose_name_plural = _('Experiences')


################################################################################################
class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name=_('Project Title'))
    description = models.TextField(verbose_name=_('Project Description'))
    image = models.ImageField(upload_to='projects/', blank=True, many=True, null=True, verbose_name=_('Project Image'))
    url = models.URLField(blank=True, verbose_name=_('Project URL'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created At'))
    languages = models.CharField(max_length=200, verbose_name=_('Languages'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Project')
        verbose_name_plural = _('Projects')


################################################################################################
class Skill(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('Skill Name'))
    # GenericForeignKey setup for Skill model to be able to link to any other model
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Skill')
        verbose_name_plural = _('Skills')
