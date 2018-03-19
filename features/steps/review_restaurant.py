from behave import *

use_step_matcher("parse")

@given('Exists review at restaurant "{restaurant_name}" by "{username}"')
def step_impl(context, restaurant_name, username):
    from django.contrib.auth.models import User
    user = User.objects.get(username=username)
    from myrestaurants.models import Restaurant
    restaurant = Restaurant.objects.get(name=restaurant_name)
    from myrestaurants.models import RestaurantReview
    for row in context.table:
        review = RestaurantReview(restaurant=restaurant, user=user)
        for heading in row.headings:
            setattr(review, heading, row[heading])
        review.save()

@when('I register a review at restaurant "{restaurant_name}"')
def step_impl(context, restaurant_name):
    from myrestaurants.models import Restaurant
    restaurant = Restaurant.objects.get(name=restaurant_name)
    for row in context.table:
        context.browser.visit(context.get_url(restaurant))
        form = context.browser.find_by_tag('form').first
        context.browser.choose('rating', row['rating'])
        context.browser.fill('comment', row['comment'])
        form.find_by_value('Review').first.click()

@then('There are {count:n} reviews')
def step_impl(context, count):
    from myrestaurants.models import RestaurantReview
    assert count == RestaurantReview.objects.count()
