import json
import os
import re

from databases.models import Quotes

from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

dir_path = os.path.dirname(os.path.realpath("badwords.json"))


@register.simple_tag
def random_quote_generator():
    random_quote = Quotes.objects.order_by('?').first()
    random_quote_author = random_quote.author
    return random_quote.quote, random_quote_author.author


@register.filter
@stringfilter
def censorship_filter(string):
    with open(dir_path + '/' + 'badwords.json', 'r') as f:
        data = json.load(f)
        for item in data:
            censored_item = re.sub(r'\b' + item + r'\b', '****', string)
            string = censored_item
        return string
