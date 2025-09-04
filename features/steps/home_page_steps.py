from behave import given, when, then





@when('Add several items to cart')
def add_items_to_cart(context):
    context.app.home_page.add_items_to_cart()


@when('Click cart icon')
def click_cart_icon(context):
    context.app.home_page.click_cart_icon()


@then('Verify cart badge number updates')
def cart_badge_number_updates(context):
    context.app.home_page.cart_badge_number_updates()

@then('Verify you are logged In')
def verify_user_logged_in(context):
    context.app.home_page.verify_user_logged_in()