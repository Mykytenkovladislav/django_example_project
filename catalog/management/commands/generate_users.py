from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User

from faker import Faker


class GenerateUsers(BaseCommand):
    help = 'Creating a custom amount of users'

    def add_arguments(self, parser):
        parser.add_argument('users_amount', nargs='+', type=int)

    def handle(self, *args, **options):
        fake = Faker()

        for _ in options['users_amount']:
            # generated_accounts: list = []
            account: str = fake.name()
            firstname_lastname: list = account.split(' ')
            first_name = firstname_lastname[0]
            last_name = firstname_lastname[1]
            username = password = account.lower().replace(' ', '')
            email = username + '@gmail.com'
            password = username
            generated_user = User.objects.create_user()

        self.stdout.write(self.style.SUCCESS('Users successfully created!'))
