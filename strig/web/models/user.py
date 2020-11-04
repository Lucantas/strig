from django.db import models
from django import forms
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.utils.translation import ugettext as _

class UserManager(BaseUserManager):
    def create_user(self, email, date_of_birth, password=None):
        """
        Cria e salva um usuário com o email, data de nascimento e senha informados
        """
        if not email:
            raise ValueError('Usuários precisam ter um e-mail cadastrado')

        user = self.model(
            # email=self.normalize_email(email),
            date_of_birth=date_of_birth,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, date_of_birth, password=None):
        """
        Cria e salva um usuário super com o email, data de nascimento e senha informados
        """
        user = self.create_user(
            email,
            password=password,
            date_of_birth=date_of_birth,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    name = models.CharField(_("Nome"), max_length=100)
    creation_date = models.DateField(_("Data de criação"), auto_now=True)
    last_modified = models.DateField(_("Última modificação"), auto_now_add=False, null=True)
    date_of_birth = models.DateField(_("Data de nascimento"), null=True)
    is_active = models.BooleanField(_("Ativo"), default=True)
    is_admin = models.BooleanField(_("Admin"), default=False)
    email = models.EmailField(_("E-mail"), max_length=254, unique=True, null=True)

    USERNAME_FIELD = 'email'

    objects = UserManager()

    def __str__(self):
        return "{0} <{1}>".format(self.name, self.email)

    def has_perm(self, perm, obj=None):
        # TODO: "Does the user have a specific permission?"
        return True

    def has_module_perms(self, app_label):
        # TODO: "Does the user have permissions to view the app `app_label`?"
        return True

    @property
    def is_staff(self):
        # TODO: "Is the user a member of staff?"
        return self.is_admin
    