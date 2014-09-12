from behave import *

@given('I am on the page with url "{url}"')
def step_impl(context, url):
    context.browser.visit(url)

@when('I put "{value}" in field with name "{key}"')
def step_impl(context, value, key):
    context.browser.fill(key, value)

@when('I click the button with name "{name}"')
def step_impl(context, name):
    button = context.browser.find_by_name(name)
    button.click()

@then('I should be on page with url "{url}"')
def step_impl(context, url):
    assert context.browser.url == url

@then('I should see the text "{text}"')
def step_impl(context, text):
    assert context.browser.is_text_present(text)