from behave import *

use_step_matcher("parse")

@when('I list restaurants')
def step_impl(context):
    context.browser.visit(context.get_url('myrestaurants:restaurant_list'))

@then('I\'m viewing a list containing')
def step_impl(context):
    restaurant_links = context.browser.find_by_css('div#content ul li a')
    for i, row in enumerate(context.table):
        assert row['name'] == restaurant_links[i].text

@step('The list contains {count:n} restaurants')
def step_impl(context, count):
    assert count == len(context.browser.find_by_css('div#content ul li a'))
