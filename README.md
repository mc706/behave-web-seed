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


###Steps
Steps are tiny bits of reusable functionality that can be run in the context of a feature. They are defined inside of the
`/steps` folder


###Running
In order to run the test suite, open this directory in your terminal, install the requirements, then run 

``` 
behave
```

The framework will do the rest.