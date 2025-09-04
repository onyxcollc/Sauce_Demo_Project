from behave import given, when, then





@given('Open sauce demo webpage')
def login_page(context):
    context.app.login_page.login_page()


@when('Enter Username {name}')
def user_name(context, name):
    context.app.login_page.user_name(name)


@when('Enter Password {password}')
def password_text(context,password):
    context.app.login_page.password_text(password)


@when("Click Login button")
def login_btn(context):
    context.app.login_page.login_btn()



@then('Verify error message')
def error_message(context):
    context.app.login_page.error_message()