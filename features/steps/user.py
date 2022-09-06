import json
from behave import *
from application import USERS


request_body = {}


# Background
@given('I set the user url of the api')
def step_impl(context):
    global user_url
    user_url = '/users/'


# Scenario: GET


@given("least two user are in the system")
def step_impl(context):
    jasonName = context.table[0]['key']
    age = context.table[0]['age']
    occupation = context.table[0]['occupation']

    lucioName = context.table[1]['key']
    ageLucio = context.table[1]['age']
    occupationLucio = context.table[1]['occupation']

    if jasonName not in USERS:
        USERS[jasonName] = {'age': age, 'occupation': occupation}
    if lucioName not in USERS:
        USERS[lucioName] = {'age': ageLucio, 'occupation': occupationLucio}

    assert len(USERS) >= 2


@when('I receive the users')
def step_impl(context):
    context.page = context.client.get(user_url)
    assert context.page


@then(u"I should get a success response '{status_code:d}'")
def step_impl(context, status_code):
    assert context.page.status_code is status_code


@then('the following users are returned')
def step_impl(context):
    dict = json.loads(context.page.data.decode('utf-8'))

    for row in context.table:
        assert row['key'] in dict
        assert dict[row['key']]['age'] == (row['age'])
        assert dict[row['key']]['occupation'] == row['occupation']

    # Clean userdata
    USERS.clear()


###################################


# Scenario Delete a user:
@when("I delete the user '{name}'")
def step_impl(context, name):
    global user_url
    user_url = user_url + name
    context.page = context.client.delete(user_url)
    assert context.page


@then("'{name}' is not in the system")
def step_impl(context, name):
    assert name not in USERS
    USERS.clear()


# Scenario Create a user:
@given("I not have a user '{name}' in the system")
def step_impl(context, name):
    assert name not in USERS


@when("I create a user '{name}' with the following details")
def step_impl(context, name):
    global user_url
    global request_body
    age = context.table[0]['age']
    occupation = context.table[0]['occupation']
    request_body = {name: {'age': age, 'occupation': occupation}}
    context.page = context.client.post(user_url, data=json.dumps(
        request_body), content_type='application/json')

    assert context.page


@then("I should have a user '{name}' with the following details")
def step_impl(context, name):
    global request_body
    assert name in USERS
    assert USERS[name]['age'] == request_body[name]['age']
    assert USERS[name]['occupation'] == request_body[name]['occupation']
    USERS.clear()


#######################################

# Scenario Update a user:
@given("I have a user '{name}' in the system with the following details")
def step_impl(context, name):
    if name not in USERS:
        USERS[name] = {'age': context.table[0]['age'],
                       'occupation': context.table[0]['occupation']}
    assert name in USERS


@when("I update the user '{name}' with the following details")
def step_impl(context, name):
    global user_url
    global request_body
    user_url = user_url + name
    age = context.table[0]['age']
    occupation = context.table[0]['occupation']

    request_body = {'age': age, 'occupation': occupation}
    context.page = context.client.put(user_url, data=json.dumps(
        request_body), content_type='application/json')
    assert context.page


@then("I should have a user '{name}' like the following")
def step_impl(context, name):
    global request_body
    assert name in USERS
    assert USERS[name]['age'] == request_body['age']
    assert USERS[name]['occupation'] == request_body['occupation']
    USERS.clear()


@given('some users are in the system')
def step_impl(context):
    USERS.update({'jasonb': {'name': 'Jason Bourne'}})
    # [ {},{}..]
    # { 'key': {}, 'key2': {}  }
    # assert len(USERS) > 0


@when(u'I retrieve the customer \'jasonb\'')
def step_impl(context):
    context.page = context.client.get('/users/jasonb')
    assert context.page


@then(u"I should get a '{status:d}' response")
def step_impl(context, status):
    print(context.page.status_code)
    assert context.page.status_code is status


@then(u'the following user details are returned')
def step_impl(context):
    print(context.page)
    assert context.table[0].cells[0] in context.page.text
    USERS.clear()
    # assert "Jason Bourne" in context.page.text


@then(u'I obtain the list of users')
def step_impl(context):
    context.page = context.client.get('/users/')
    assert context.page.status_code == 200
