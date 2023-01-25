from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError

from faker import Faker


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('user_count', type=int)

    def handle(self, *args, **options):
        fake = Faker()
        user_params = []
        user_count = options['user_count']
        if user_count < 1 or user_count > 10:
            raise CommandError('User count should be between one and ten!')
        for i in range(0, user_count):
            user_params.append({'username': fake.name(),
                                'email': fake.email(),
                                'password': make_password(fake.password())})

        created_records = User.objects.bulk_create([User(**values) for values in user_params], batch_size=1000)
        self.stdout.write(self.style.SUCCESS(
            'Successfully created users {}'.format(list(map(lambda x: x.username, created_records))))
        )
