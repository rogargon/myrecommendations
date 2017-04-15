Feature: List Restaurant Reviews
  In order to know about the opinion of previous visitors of a restaurant
  As a user
  I want to list all the reviews registered by any user for a restaurant

  Background: There is one restaurant with 2 reviews and another without
    Given Exists a user "user1" with password "password"
    And Exists a user "user2" with password "password"
    And Exists restaurant registered by "user1"
      | name            |
      | Famous          |
      | Unknown         |
    And Exists review at restaurant "Famous" by "user1"
      | rating          | comment       |
      | 4               | Quite good    |
    And Exists review at restaurant "Famous" by "user2"
      | rating          |
      | 2               |

  Scenario: List reviews for a restaurant with some
    When I list reviews at restaurant "Famous"
    Then I'm viewing a restaurant reviews list containing
      | rating          | comment       | user          |
      | 4               | Quite good    | user1         |
      | 2               |               | user2         |
    And The list contains 2 reviews

  Scenario: List dishes for a restaurant without
    When I list dishes at restaurant "Unknown"
    Then I'm viewing a restaurant dishes list containing
      | rating          | comment       | user          |
    And The list contains 0 dishes