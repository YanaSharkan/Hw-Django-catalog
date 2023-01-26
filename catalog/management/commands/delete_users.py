from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('user_ids', nargs='+', type=int)

    def handle(self, *args, **options):
        user_ids = options['user_ids']
        users = User.objects.filter(id__in=user_ids)
        if users.filter(is_superuser=True).exists():
            raise CommandError('Can not delete admin user!')
        deleted_users = users.delete()
        self.stdout.write(self.style.SUCCESS('Successfully deleted users {}'.format(list(deleted_users)[0])))
