from behave import *

use_step_matcher("parse")

@when('I view the details for restaurant "{restaurant_name}"')
def step_impl(context, restaurant_name):
    from myrestaurants.models import Restaurant
    restaurant = Restaurant.objects.get(name=restaurant_name)
    context.browser.visit(context.get_url('myrestaurants:restaurant_detail', restaurant.pk))

@then('I\'m viewing a restaurant reviews list containing')
def step_impl(context):
    reviews = context.browser.find_by_css('blockquote.review')
    for i, row in enumerate(context.table):
        assert reviews[i].find_by_css('.rating').first.text.count(u"\u2605") == int(row['rating'])
        if row['comment']:
            assert row['comment'] == reviews[i].find_by_tag('strong').first.text
        assert reviews[i].find_by_tag('footer').first.text.startswith(row['user'])

@then("The list contains {count:n} reviews")
def step_impl(context, count):
    assert count == len(context.browser.find_by_css('blockquote.review'))

@then("I'm viewing a restaurant dishes list containing")
def step_impl(context):
    dish_links = context.browser.find_by_css('a.dish-link')
    for i, row in enumerate(context.table):
        assert row['name'] == dish_links[i].text

@step("The list contains {count:n} dishes")
def step_impl(context, count):
    assert count == len(context.browser.find_by_css('a.dish-link'))

@then("I'm viewing restaurants details including")
def step_impl(context):
    for heading in context.table.headings:
        context.browser.is_text_present(context.table[0][heading])
