from behave import given, when, then







@when('Click Checkout button')
def checkout_btn(context):
    context.app.cart_page.checkout_btn()