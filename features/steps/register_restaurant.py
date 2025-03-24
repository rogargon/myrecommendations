from functools import reduce

from behave import *
import operator
from django.db.models import Q

use_step_matcher("parse")

@given('Exists restaurant registered by "{username}"')
def step_impl(context, username):
    from django.contrib.auth.models import User
    user = User.objects.get(username=username)
    from myrestaurants.models import Restaurant
    for row in context.table:
        restaurant = Restaurant(user=user)
        for heading in row.headings:
            setattr(restaurant, heading, row[heading])
        restaurant.save()

@when('I register restaurant')
def step_impl(context):
    for row in context.table:
        context.browser.visit(context.get_url('myrestaurants:restaurant_create'))
        if context.browser.url == context.get_url('myrestaurants:restaurant_create'):
            form = context.browser.find_by_id('input-form')
            for heading in row.headings:
                context.browser.fill(heading, row[heading])
            form.find_by_value('Submit').first.click()

@then('There are {count:n} restaurants')
def step_impl(context, count):
    from myrestaurants.models import Restaurant
    assert count == Restaurant.objects.count()

@then('I\'m viewing the details page for restaurant by "{username}"')
def step_impl(context, username):
    context.browser.is_text_present(username)
    for row in context.table:
        for heading in row.headings:
           expected = row[heading]
           context.browser.is_text_present(expected)

@when('I edit the restaurant with name "{name}"')
def step_impl(context, name):
    from myrestaurants.models import Restaurant
    restaurant = Restaurant.objects.get(name=name)
    context.browser.visit(context.get_url('myrestaurants:restaurant_edit', restaurant.pk))
    if context.browser.url == context.get_url('myrestaurants:restaurant_edit', restaurant.pk)\
            and context.browser.find_by_id('input-form'):
        form = context.browser.find_by_id('input-form')
        for heading in context.table.headings:
            context.browser.fill(heading, context.table[0][heading])
        form.find_by_value('Submit').first.click()
