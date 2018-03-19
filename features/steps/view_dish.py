from behave import *

use_step_matcher("parse")

@when('I view the details for dish "{dish_name}"')
def step_impl(context, dish_name):
    from myrestaurants.models import Dish
    dish = Dish.objects.get(name=dish_name)
    context.browser.visit(context.get_url(dish))

@then("I'm viewing dish details including")
def step_impl(context):
    for heading in context.table.headings:
        context.browser.is_text_present(context.table[0][heading])
