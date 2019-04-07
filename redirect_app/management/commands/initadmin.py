from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        username = 'admin'
        email = 'admin@admin.com'
        password = 'admin'
        print('Creating account for %s (%s)' % (username, email))
        admin = User.objects.create_superuser(email=email, username=username, password=password)
        admin.is_active = True
        admin.is_admin = True
        admin.save()
