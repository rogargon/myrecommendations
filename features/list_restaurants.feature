Feature: List Restaurants
  In order to keep myself up to date about restaurants registered in myrestaurants
  As a user
  I want to list the last 5 registered restaurants

  Background: There are 6 registered restaurants by same user
    Given Exists a user "user" with password "password"
    And Exists restaurant registered by "user"
      | name            | date        |
      | The First       | 1970-01-01  |
      | The Second      | 1970-01-02  |
      | The Third       | 1970-01-03  |
      | The Fourth      | 1970-01-04  |
      | The Fifth       | 1970-01-05  |

  Scenario: List the last five
    When I list restaurants
    Then I'm viewing a list containing
      | name            |
      | The Fifth       |
      | The Fourth      |
      | The Third       |
      | The Second      |
      | The First       |
    And The list contains 5 restaurants

  Scenario: List the last five
    Given Exists restaurant registered by "user"
      | name            | date        |
      | The Sixth       | 1970-01-06  |
    When I list restaurants
    Then I'm viewing a list containing
      | name            |
      | The Sixth       |
      | The Fifth       |
      | The Fourth      |
      | The Third       |
      | The Second      |
    And The list contains 5 restaurants