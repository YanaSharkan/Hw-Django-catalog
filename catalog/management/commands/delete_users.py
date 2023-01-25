from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('user_ids', nargs='+', type=int)

    def handle(self, *args, **options):
        user_ids = options['user_ids']
        admin_user = User.objects.filter(is_superuser=True)
        admin_user_id = admin_user.get().id
        if admin_user_id in user_ids:
            raise CommandError('Can not delete admin user!')
        deleted_users = User.objects.filter(id__in=user_ids).delete()
        self.stdout.write(self.style.SUCCESS('Successfully deleted users {}'.format(list(deleted_users)[0])))
