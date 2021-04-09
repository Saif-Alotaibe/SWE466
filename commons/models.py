import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser


class Model(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(_("Date created"), auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(_("Date updated"), auto_now=True, db_index=True)

    class Meta:
        abstract = True


class User(AbstractUser, Model):
	username = models.CharField(null=True, max_length=70, unique=False)
	email = models.EmailField(unique=True, null=True)
	
	REQUIRED_FIELDS = ['username']
	USERNAME_FIELD = 'email'
	
	def __str__(self):
		return self.username or ''
