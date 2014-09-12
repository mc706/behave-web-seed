from behave import *

@given('we have behave installed')
def step_impl(context):
    pass

@when('we implement a test')
def step_impl(context):
    assert True is not False

@then('behave will test it for us!')
def step_impl(context):
    assert context.failed is False

@given(u'I put Red Tree Frog in a blender,')
def step_impl(context):
    pass

@when(u'I switch the blender on')
def step_impl(context):
    assert True is not False

@then(u'it should transform into mush')
def step_impl(context):
    assert context.failed is False

@given(u'I put iPhone in a blender,')
def step_impl(context):
    pass

@then(u'it should transform into toxic waste')
def step_impl(context):
    assert context.failed is False

@given(u'I put Galaxy Nexus in a blender,')
def step_impl(context):
    pass

@given(u'a sample text loaded into the frobulator')
def step_impl(context):
    pass

@when(u'we activate the frobulator')
def step_impl(context):
    assert True is not False

@then(u'we will find it similar to English')
def step_impl(context):
    assert context.failed is False

@given('a set of specific users')
def step_impl(context):
    for row in context.table:
        pass

@when(u'we count the number of people in each department')
def step_impl(context):
    assert True is not False

@then(u'we will find two people in "Silly Walks"')
def step_impl(context):
    assert context.failed is False

@then(u'we will find one person in "Beer Cans"')
def step_impl(context):
    assert context.failed is False