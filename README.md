# Flask Behave Template

This is a template where there is a very simple [Flask](https://flask.palletsprojects.com/en/2.2.x/) application built using BDD with [Behave](https://github.com/behave/behave) tool.

### Setup & Run

```sh
# Create a virtual environment
$ python -m venv env 

# activate the environment
$ source env/bin/activate

# install requirements
(env) $ python -m pip install -r requirements.txt
```

```sh
# init flask server
(env) $ python app/application.py

# Run the test suite
(env) $ behave
```


## BDD

Behaviour-driven development allows you to describe how your application should behave, and drive the development of features by adding new tests and making them pass. By clearly describing how your application behaves in different scenarios, you can be confident that the product delivered at the end meets the requirements you set out to deliver. Following BDD lets you build up your application piece by piece, and also provides you with living documentation of your entire system.

Usually to describe your application behaviour you use the Gherkin language, used by frameworks like Cucumber to define test cases in the BDD-style. Under the hood, the scenario drives a series of automated tests that ensure that the specification is followed.

More on this https://github.com/cucumber/gherkin-python


### Assignment

Write new gherkin scenarios, as we did in [user.feature](https://github.com/proyecto-unrc-2022/flask-behave-template/blob/master/features/user.feature), with its corresponding [steps](https://github.com/proyecto-unrc-2022/flask-behave-template/blob/master/features/steps/user.py), to implement the following endpoints:

* Support POST operation to add a new user.
* Support PUT operations to update a user from the USERS data store.
* Support DELETE operations to remove a user from the USERS data store.
* Support GET operation to list all system users

This repository has a [workflow](https://github.com/proyecto-unrc-2022/flask-fbrusatti/blob/master/.github/workflows/behave.yml) enabled, which run behave on push master branch in CI, so assignment will be passed when all above endpoints are implemented and CI is green.
