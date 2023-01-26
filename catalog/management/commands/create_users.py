from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from faker import Faker


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('user_count', type=int, choices=range(1, 11))

    def handle(self, *args, **options):
        fake = Faker()
        user_count = options['user_count']
        user_params = [{'username': fake.name(),
                        'email': fake.email(),
                        'password': make_password(fake.password())} for _ in range(user_count)]

        created_records = User.objects.bulk_create([User(**values) for values in user_params])
        self.stdout.write(self.style.SUCCESS(
            'Successfully created users {}'.format(list(map(lambda x: x.username, created_records))))
        )
