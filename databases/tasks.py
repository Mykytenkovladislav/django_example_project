from bs4 import BeautifulSoup

from celery import shared_task

from databases.models import Quotes, QuotesAuthor

from django.core.mail import send_mail as django_send_mail

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
        for i in text:
            if saved_quotes > 4:  # if 5 quotes already saved
                break
            quote: str = i.select('.text')[0].contents[0]
            if Quotes.objects.filter(quote=quote):  # Check duplicates in DB for quotes
                continue
            else:
                author: str = i.select('.author')[0].contents[0]
                if QuotesAuthor.objects.filter(author=author):  # if author already in DB
                    author_record = QuotesAuthor.objects.get(author=author)
                else:  # if not then add to DB
                    author_about_link = SITE + i.find_all('a')[0].get('href')  # take link part to author about
                    r = requests.get(author_about_link)
                    # parse author details page
                    soup = BeautifulSoup(r.text, 'html.parser')
                    born_date = soup.find('span', {'class': 'author-born-date'}).contents[0]
                    born_location = soup.find('span', {'class': 'author-born-location'}).contents[0]
                    author_description = soup.find('div', {'class': 'author-description'}).contents[0].replace(
                        '\n', ''
                    )
                    #  add Author to DB
                    author_record = QuotesAuthor.objects.create(
                        author=author,
                        date_of_birth=born_date,
                        born_in=born_location,
                        description=author_description
                    )
                Quotes.objects.create(quote=quote, author=author_record)
                saved_quotes += 1
        if saved_quotes < 5:  # if not enough unique quotes on current page
            if soup.find('li', {'class': 'next'}) is None:  # If no "Next" button on current page
                last_page = True
            else:
                page_id += 1
        else:  # If it was the last page break process and send mail
            break
    if last_page is True:  # send finish mail
        django_send_mail('Quotes', 'All quotes added!', 'noreply@test.com', ['admin@example.com'])
