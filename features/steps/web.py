"""
This file is a prebuilt library to wrap splinter. It goes with the environments.py
You can use it to quickly setup tests using only feature files

It is lovingly shared and free to use and modify by Ryan McDevitt (mc706.com)

browser.find_by_css('h1')
browser.find_by_xpath('//h1')
browser.find_by_tag('h1')
browser.find_by_name('name')
browser.find_by_id('firstheader')
browser.find_by_value('query')
"""
from behave import *
import time

@given('I am on the page with url "{url}"')
def step_impl(context, url):
    context.browser.visit(url)

@when('I put "{value}" in the field with {selector} "{key}"')
def step_impl(context, value, selector, key):
    if selector == "name":
        context.browser.fill(key, value)
    elif selector == "id":
        context.browser.find_by_id(key).fill(value)
    elif selector == "css":
        context.browser.find_by_css(key).fill(value)
    elif selector == "xpath":
        context.browser.find_by_xpath(key).fill(value)

@when('I click the button with {selector} "{value}"')
def step_impl(context, selector, value):
    if selector == 'name':
        button = context.browser.find_by_name(value)
    elif selector == 'id':
        button = context.browser.find_by_id(value)
    elif selector == 'css':
        button = context.browser.find_by_css(value)
    elif selector == "xpath":
        button = context.browser.find_by_xpath(value)
    button.click()

@when('I choose the "{value}" option from the radio buttons with name "{key}"')
def step_impl(context, value, key):
    context.browser.choose(key, value)

@when('I wait {x} seconds')
def step_impl(context, x):
    time.sleep(float(x))

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
