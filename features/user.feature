Feature: Handle storing, retrieving and deleting customer details # test/features/user.feature:1

  Background:
    Given I set the user url of the api

  Scenario: Retrieve a customers details
    Given some users are in the system
    When I retrieve the customer 'jasonb'
    Then I should get a '200' response
    And the following user details are returned:
      | name         |
      | Jason Bourne |

  Scenario: Get all users
    Given least two user are in the system:
      | key          | age |  | occupation |
      | Jason Bourne | 20  |  | Programmer |
      | Lucio        | 20  |  | Student    |
    When I receive the users
    Then I should get a success response '200'
    And the following users are returned:
      | key          | age |  | occupation |
      | Jason Bourne | 20  |  | Programmer |
      | Lucio        | 20  |  | Student    |


  Scenario: Delete a user
    Given least two user are in the system:
      | key          | age |  | occupation |
      | Jason Bourne | 20  |  | Programmer |
      | Lucio        | 20  |  | Student    |
    When I delete the user 'Lucio'
    Then I should get a success response '200'
    And 'Lucio' is not in the system


  Scenario: Create a user
    Given I not have a user 'Jason Bourne' in the system
    When I create a user 'Jason Bourne' with the following details:
      | key          | age |  | occupation |
      | Jason Bourne | 20  |  | Programmer |
    Then I should get a success response '201'
    And I should have a user 'Jason Bourne' with the following details:
      | key          | age |  | occupation |
      | Jason Bourne | 20  |  | Programmer |

  Scenario: Update a user
    Given I have a user 'Jason Bourne' in the system with the following details:
      | key          | age |  | occupation |
      | Jason Bourne | 20  |  | Programmer |
    When I update the user 'Jason Bourne' with the following details:
      | key          | age |  | occupation |
      | Jason Bourne | 21  |  | Student    |
    Then I should get a success response '204'
    And I should have a user 'Jason Bourne' like the following:
      | key          | age |  | occupation |
      | Jason Bourne | 21  |  | Student    |
