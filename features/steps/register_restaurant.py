from behave import *
import operator
from django.db.models import Q
from django.urls.base import reverse

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
        form = context.browser.find_by_tag('form').first
        for heading in row.headings:
            context.browser.fill(heading, row[heading])
        form.find_by_value('Submit').first.click()

@then('There are {count:n} restaurants')
def step_impl(context, count):
    from myrestaurants.models import Restaurant
    assert count == Restaurant.objects.count()

@then('I\'m viewing the details page for restaurant by "{username}"')
def step_impl(context, username):
    q_list = [Q((attribute, context.table.rows[0][attribute])) for attribute in context.table.headings]
    from django.contrib.auth.models import User
    q_list.append(Q(('user', User.objects.get(username=username))))
    from myrestaurants.models import Restaurant
    restaurant = Restaurant.objects.filter(reduce(operator.and_, q_list)).get()
    assert context.browser.url == context.get_url(restaurant)

@when('I edit the current restaurant')
def step_impl(context):
    context.browser.find_link_by_text('edit').click()
    # TODO: Test also using direct edit view link
    # context.browser.visit(context.get_url('myrestaurants:restaurant_edit', restaurant.pk))
    form = context.browser.find_by_tag('form').first
    for heading in context.table.headings:
        context.browser.fill(heading, context.table[0][heading])
    form.find_by_value('Submit').first.click()
