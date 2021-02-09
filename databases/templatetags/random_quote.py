from django import template

from databases.models import Quotes


register = template.Library()


@register.simple_tag
def random_quote_generator():
    random_quote = Quotes.objects.order_by('?').first()
    random_quote_author = random_quote.author
    return random_quote.quote, random_quote_author.author