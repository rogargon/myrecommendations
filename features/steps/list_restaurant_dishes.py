from behave import *

use_step_matcher("parse")

@when('I list dishes at restaurant "{restaurant_name}"')
def step_impl(context, restaurant_name):
    from myrestaurants.models import Restaurant
    restaurant = Restaurant.objects.get(name=restaurant_name)
    context.browser.visit(context.get_url(restaurant))


@then("I'm viewing a restaurant dishes list containing")
def step_impl(context):
    dish_links = context.browser.find_by_css('div#content ul li a')
    for i, row in enumerate(context.table):
        assert row['name'] == dish_links[i].text


@step("The list contains {count:n} dishes")
def step_impl(context, count):
    assert count == len(context.browser.find_by_css('div#content ul li a'))
