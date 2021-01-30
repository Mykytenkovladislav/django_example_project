from databases.models import Quotes, QuotesAuthor

from django.core.management.base import BaseCommand, CommandError

from faker import Faker


class Command(BaseCommand):
    help = 'Creating a custom amount of authors and  their quotes'  # noqa: A003

    def add_arguments(self, parser):
        parser.add_argument('authors_amount', nargs='+', type=int)

    def handle(self, *args, **options):
        fake = Faker()
        authors_amount = options['authors_amount']
        if authors_amount[0] < 1:
            raise CommandError('Value can\'t be less then 1')
        elif authors_amount[0] > 1000:
            raise CommandError('Value can\'t be greater then 1000')
        for _ in range(authors_amount[0]):
            author: str = fake.name()
            if QuotesAuthor.objects.filter(author=author):
                author_record = QuotesAuthor.objects.get(author=author)
            else:
                born_location = fake.address()
                born_date = fake.date()
                author_description = fake.text()
                author_record = QuotesAuthor.objects.create(
                    author=author,
                    date_of_birth=born_date,
                    born_in=born_location,
                    description=author_description
                )
            quote_1 = fake.text()
            quote_2 = fake.text()
            Quotes.objects.create(quote=quote_1, author=author_record)
            Quotes.objects.create(quote=quote_2, author=author_record)
            self.stdout.write(f'Quote for {author} successfully added!')
        self.stdout.write(self.style.SUCCESS('Authors and their quotes generated!'))
