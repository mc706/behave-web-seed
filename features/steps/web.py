"""
This file is a prebuilt library to wrap splinter. It goes with the environments.py
You can use it to quickly setup tests using only feature files

It is lovingly shared and free to use and modify by Ryan McDevitt (mc706.com)
"""
from behave import *
import time

@given('I am on the page with url "{url}"')
def step_impl(context, url):
    context.browser.visit(url)

@when('I put "{value}" in the field with name "{key}"')
def step_impl(context, value, key):
    context.browser.fill(key, value)

@when('I click the button with name "{name}"')
def step_impl(context, name):
    button = context.browser.find_by_name(name)
    button.click()

@when('I click the button with id "{id}"')
def step_impl(context, id):
    button = context.browser.find_by_id(id)
    button.click()

@when('I click the button with css selector "{css}"')
def step_impl(context, css):
    button = context.browser.find_by_css_selector(css)
    button.click()

@then('I should be on the page with url "{url}"')
def step_impl(context, url):
    time.sleep(1) #wait 1 second to make sure things resolve
    assert context.browser.url == url

@then('I should see the text "{text}"')
def step_impl(context, text):
    assert context.browser.is_text_present(text)

@then('I should not see the text "{text}"')
def step_impl(context, text):
    assert not context.browser.is_text_present(text)

@then('I should see the following text')
def step_impl(context):
    assert context.browser.is_text_present(context.text)

@then('I should not see the following text')
def step_impl(context):
    assert not context.browser.is_text_present(context.text)

@when('I wait {x} seconds')
def step_impl(context, x):
    time.sleep(float(x))