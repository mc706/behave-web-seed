"""
This file is a prebuilt library to wrap splinter. It goes with the environments.py
You can use it to quickly setup tests using only feature files. For more splinter documentation
visit their site at http://splinter.cobrateam.info/
The browser object you would use in splinter is available via context.browser

It is lovingly shared and free to use and modify by Ryan McDevitt (http://mc706.com)
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
        context.browser.find_by_name(value).click()
    elif selector == 'id':
        context.browser.find_by_id(value).click()
    elif selector == 'css':
        context.browser.find_by_css(value).click()
    elif selector == "xpath":
        context.browser.find_by_xpath(value).click()

@when('I click the link with {selector} "{value}"')
def step_impl(context, selector, value):
    if selector == "id":
        context.browser.find_by_id(value).click()
    elif selector == "text":
        context.browser.click_link_by_text(value)
    elif selector == "href":
        context.browser.click_link_by_href(value)

@when('I choose the "{value}" option from the radio buttons with name "{key}"')
def step_impl(context, value, key):
    context.browser.choose(key, value)


@when('I choose the "{value}" option from the dropdown with name "{key}"')
def step_impl(context, value, key):
    context.browser.select(key, value)

@when('I {bool} the checkbox with name "{key}"')
def step_impl(context, bool, key):
    if bool == "check":
        context.browser.check(key)
    elif bool == "uncheck":
        context.browser.uncheck(key)

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
