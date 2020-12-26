from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User

from faker import Faker


class Command(BaseCommand):
    help = 'Creating a custom amount of users'

    def add_arguments(self, parser):
        parser.add_argument('users_amount', nargs='+', type=int)

    def handle(self, *args, **options):
        fake = Faker()
        users_amount = options['users_amount']
        if users_amount[0] < 1:
            raise CommandError('Value can\'t be less then 1')
        elif users_amount[0] > 10:
            raise CommandError('Value can\'t be greater then 10')
        for _ in range(users_amount[0]):
            account: str = fake.name()
            username = account.lower().replace(' ', '')
            email = username + '@gmail.com'
            password = username  # for visualization
            User.objects.create_user(username, email, password)
            self.stdout.write(f'{username} successfully created!')
        self.stdout.write(self.style.SUCCESS('Users successfully generated!'))
