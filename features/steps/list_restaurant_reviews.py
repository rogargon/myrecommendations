from behave import *

use_step_matcher("parse")

@when('I list reviews at restaurant "{restaurant_name}"')
def step_impl(context, restaurant_name):
    from myrestaurants.models import Restaurant
    restaurant = Restaurant.objects.get(name=restaurant_name)
    context.browser.visit(context.get_url(restaurant))

@then('I\'m viewing a restaurant reviews list containing')
def step_impl(context):
    review_par_links = context.browser.find_by_css('div#content ul li p')
    for i, row in enumerate(context.table):
        assert review_par_links[3*i].text.startswith(row['rating'])
        assert row['comment'] == review_par_links[3*i+1].text
        assert review_par_links[3*i+2].text.startswith('Created by '+row['user'])

@step("The list contains {count:n} reviews")
def step_impl(context, count):
    assert count == len(context.browser.find_by_css('div#content ul li p')) / 3



