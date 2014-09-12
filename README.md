behave-web-seed
===============

A Seed project for starting a behave testing suite for the web

###example

This base setup tests an application named "example". Copy the everything in the `/features` folder with "example"  
and replace example with your feature names to create additional feature sets.


###Requirements

The setup for this project's dependencies is the requirements.txt file. to use this file simply:

```
pip install -r requirements.txt
```

###Features
`.feature` files are the files that describe the features you want to test in near plain english. Each feature is
mapped to a step, which executes in the features context when that step is referenced.

Features have 4 keywords, `Given` , `When` , `Then` and `And` .

`Given` is used for page setup. This is typicaly the start of the test. They do no checking. Examples would be going to a url,
or setting up a login

`When` are actions. When I click a button, or when i fill out a field

`Then` are tests. They check for state, and return true or false. False will fail the test and take a screenshot

`And` is an english placeholder. It takes the form of whatever the previous step was. If it follows a given, it acts as a given...

###Steps
Steps are tiny bits of reusable functionality that can be run in the context of a feature. They are defined inside of the
`/steps` folder

Steps are shared globally, so even if you create your own steps file, you can still use the web library or steps defined in other
step files. Be careful, you cannot define the same step twice.

You can define steps that execute other steps. For example, you can consolidate a login script:  
```
Given I am on the page with url "http://www.example.com"
When I put "test" in the field with name "username"
And I put password in the field with name "password"
And I click the button with text "Login"
```
to the single Given statement:
```
Given I am logged into example.com
```
by adding your own step that looks like
```
@given('I am logged into example.com')
def step_impl(context):
    context.execute_steps('''
        Given I am on the page with url "http://www.example.com"
        When I put "test" in the field with name "username"
        And I put password in the field with name "password"
        And I click the button with text "Login"
    ''')
```

###Running
In order to run the test suite, open this directory in your terminal, install the requirements, then run 

``` 
behave
```

The framework will do the rest.

To Run a particlar feature run the feature name as an argument

```
behave <feature_name>
```
for example
```
behave example
```
will only run the example feature, and not the websample feature

### Web Library
I wrote a simple step library to wrap the functionality of splinter, here is a list of available commands.
Replace the <*> with whatever you want
```
Given I am on the page with url "<*>"
When I put "<*>" in the field with name "<*>"
When I put "<*>" in the field with id "<*>"
When I put "<*>" in the field with css "<*>"
When I put "<*>" in the field with xpath "<*>"
When I click the button with name "<*>"
When I click the button with id "<*>"
When I click the button with css "<*>"
When I click the button with xpath "<*>"
When I choose the "<*>" option from the radio buttons with name "<*>" 
When I wait <*> seconds
Then I should be on the page with url "<*>"
Then I should see the text "<*>"
Then I should not see the text "<*>"
Then I should see the following text 
    """
    <*>
    """
Then I should not see the following text
    """
    <*>
    """
```
