from functools import reduce

from behave import *
import operator
from django.db.models import Q
import os

from myrecommendations.settings import BASE_DIR

use_step_matcher("parse")

@given('Exists dish at restaurant "{restaurant_name}" by "{username}"')
def step_impl(context, restaurant_name, username):
    from django.contrib.auth.models import User
    user = User.objects.get(username=username)
    from myrestaurants.models import Restaurant
    restaurant = Restaurant.objects.get(name=restaurant_name)
    from myrestaurants.models import Dish
    for row in context.table:
        dish = Dish(restaurant=restaurant, user=user)
        for heading in row.headings:
            setattr(dish, heading, row[heading])
        dish.save()

@when('I register dish at restaurant "{restaurant_name}"')
def step_impl(context, restaurant_name):
    from myrestaurants.models import Restaurant
    restaurant = Restaurant.objects.get(name=restaurant_name)
    for row in context.table:
        context.browser.visit(context.get_url('myrestaurants:dish_create', restaurant.pk))
        if context.browser.url == context.get_url('myrestaurants:dish_create', restaurant.pk):
            form = context.browser.find_by_tag('form').first
            for heading in row.headings:
                if heading == 'image':
                    filePath = os.path.join(BASE_DIR, row[heading])
                    context.browser.fill(heading, filePath)
                else:
                    context.browser.fill(heading, row[heading])
            form.find_by_value('Submit').first.click()

@then('I\'m viewing the details page for dish at restaurant "{restaurant_name}" by "{username}"')
def step_impl(context, restaurant_name, username):
    q_list = [Q((attribute, context.table.rows[0][attribute])) for attribute in context.table.headings]
    from django.contrib.auth.models import User
    q_list.append(Q(('user', User.objects.get(username=username))))
    from myrestaurants.models import Restaurant
    q_list.append(Q(('restaurant', Restaurant.objects.get(name=restaurant_name))))
    from myrestaurants.models import Dish
    dish = Dish.objects.filter(reduce(operator.and_, q_list)).get()
    assert context.browser.url == context.get_url(dish)
    if dish.image:
        dish.image.delete()

@then('There are {count:n} dishes')
def step_impl(context, count):
    from myrestaurants.models import Dish
    assert count == Dish.objects.count()

@when('I edit the current dish')
def step_impl(context):
    context.browser.find_link_by_text('edit').click()
    # TODO: Test also using direct edit view link
    # context.browser.visit(context.get_url('myrestaurants:dish_edit', dish.pk))
    form = context.browser.find_by_tag('form').first
    for heading in context.table.headings:
        context.browser.fill(heading, context.table[0][heading])
    form.find_by_value('Submit').first.click()
