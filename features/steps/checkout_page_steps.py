from behave import given, when, then





@when('Fill out Checkout information')
def checkout_info(context):
    context.app.checkout_page.checkout_info()

@when('Click Continue button')
def continue_btn(context):
    context.app.checkout_page.continue_btn()

@when('Click Finished button')
def finish_btn(context):
    context.app.checkout_page.finish_btn()

@then('Verify Checkout Complete')
def verify_checkout_complete(context):
    context.app.checkout_page.verify_checkout_complete()
