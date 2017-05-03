from behave import *
import operator
from django.db.models import Q

use_step_matcher("parse")


@when(u'I register restaurant')
def step_impl(context):
    for row in context.table:
        context.browser.visit(context.get_url('myrestaurants:restaurant_create'))
        form = context.browser.find_by_tag('form').first
        for heading in row.headings:
            context.browser.fill(heading, row[heading])
        form.find_by_value('Submit').first.click()


@then(u'I\'m viewing the details page for restaurant')
def step_impl(context):
    q_list = [Q((attribute, context.table.rows[0][attribute])) for attribute in context.table.headings]
    from myrestaurants.models import Restaurant
    restaurant = Restaurant.objects.filter(reduce(operator.and_, q_list)).get()
    assert context.browser.url == context.get_url(restaurant)


@then(u'There are {count:n} restaurants')
def step_impl(context, count):
    from myrestaurants.models import Restaurant
    assert count == Restaurant.objects.count()
