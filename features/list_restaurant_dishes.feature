Feature: List Restaurant Dishes
  In order to know about the typical dishes at a restaurant
  As a user
  I want to list all the dishes registered by any user at a restaurant

  Background: There is one restaurant with 2 dishes and another without
    Given Exists a user "user1" with password "password"
    And Exists a user "user2" with password "password"
    And Exists restaurant registered by "user1"
      | name            |
      | Famous          |
      | Unknown         |
    And Exists dish at restaurant "Famous" by "user1"
      | name            |
      | Fish and Chips  |
    And Exists dish at restaurant "Famous" by "user2"
      | name            |
      | Apple Pie       |

  Scenario: List dishes for a restaurant with some
    When I list dishes at restaurant "Famous"
    Then I'm viewing a restaurant dishes list containing
      | name            | user          |
      | Fish and Chips  | user1         |
      | Apple Pie       | user2         |
    And The list contains 2 dishes

  Scenario: List dishes for a restaurant without
    When I list dishes at restaurant "Unknown"
    Then I'm viewing a restaurant dishes list containing
      | name            |
    And The list contains 0 dishes