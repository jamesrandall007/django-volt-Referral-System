# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    signup_date = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Referral System(models.Model):

    #__Referral System_FIELDS__
    id_clinic = models.IntegerField(null=True, blank=True)
    clinic_name = models.TextField(max_length=255, null=True, blank=True)
    clinic_address = models.TextField(max_length=255, null=True, blank=True)
    clinic_phone = models.TextField(max_length=255, null=True, blank=True)

    #__Referral System_FIELDS__END

    class Meta:
        verbose_name        = _("Referral System")
        verbose_name_plural = _("Referral System")


class Physician(models.Model):

    #__Physician_FIELDS__
    id_physician = models.IntegerField(null=True, blank=True)
    physician_name = models.TextField(max_length=255, null=True, blank=True)
    physican_image_link = models.TextField(max_length=255, null=True, blank=True)
    physician_clinic_id = models.ForeignKey(Clinic, on_delete=models.CASCADE)

    #__Physician_FIELDS__END

    class Meta:
        verbose_name        = _("Physician")
        verbose_name_plural = _("Physician")


class Clinic(models.Model):

    #__Clinic_FIELDS__
    clinic_address = models.TextField(max_length=255, null=True, blank=True)
    clinic_phone = models.TextField(max_length=255, null=True, blank=True)

    #__Clinic_FIELDS__END

    class Meta:
        verbose_name        = _("Clinic")
        verbose_name_plural = _("Clinic")



#__MODELS__END
