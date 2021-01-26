from bs4 import BeautifulSoup

from celery import shared_task

from django.core.mail import send_mail as django_send_mail
from databases.models import Quotes, QuotesAuthor

import requests

# @shared_task
# def scraping_task():
#     django_send_mail('subject', str(datetime.now()), 'noreply@test.com', ['admin@example.com'])
SITE = 'https://quotes.toscrape.com'
BASE_DIR_NAME = 'scraping test'


@shared_task
def scraping_task():
    saved_quotes = 0
    last_page = False
    page_id = 1

    r = requests.get(SITE)
    while last_page is False:
        PAGE_URL = f'{SITE}/page/{page_id}'
        r = requests.get(PAGE_URL)
        soup = BeautifulSoup(r.text, 'html.parser')
        text = soup.find_all('div', {'class': 'quote'})  # find quotes by 'quote' class
        quotes_on_page = len(text)
        for i in text:
            if saved_quotes > 4:  # if 5 quotes already saved
                break
            else:
                quote: str = i.select('.text')[0].contents[0]
                if Quotes.objects.filter(quote=quote):  # Check duplicates in DB
                    continue
                else:
                    author: str = i.select('.author')[0].contents[0]
                    if QuotesAuthor.objects.filter(author=author):
                        author_record = QuotesAuthor.objects.get(author=author)
                    else:
                        author_record: QuotesAuthor = QuotesAuthor(author=author)
                        author_record.save()
                    quote_record: Quotes = Quotes(quote=quote, author=author_record)
                    quote_record.save()
                    saved_quotes += 1
        if saved_quotes < 5:  # if not enough unique quotes on current page
            if soup.find('li', {'class': 'next'}) is None:  # No "Next" button on current page
                last_page = True
            else:
                page_id += 1
        else:
            django_send_mail('Quotes', 'Still in progress', 'noreply@test.com', ['admin@example.com'])
            break
    if last_page is True:
        django_send_mail('Quotes', 'All quotes added!', 'noreply@test.com', ['admin@example.com'])
