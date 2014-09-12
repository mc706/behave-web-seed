from behave import *

@given('i visit the page')
def step_impl(context):
    pass

@when('i click an elelment')
def step_impl(context):
    assert True is not False

@then('i should be on page')
def step_impl(context):
    assert context.failed is False

