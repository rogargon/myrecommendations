Feature: View Restaurant
  In order to know about a restaurant
  As a user
  I want to view the restaurant details including all its dishes and reviews

  Background: There is one restaurant with 2 dishes and another without
    Given Exists a user "user1" with password "password"
    And Exists a user "user2" with password "password"
    And Exists restaurant registered by "user1"
      | name            | city          | country       |
      | Famous          | London        | England       |
      | Unknown         | Paris         | France        |
    And Exists dish at restaurant "Famous" by "user1"
      | name            |
      | Fish and Chips  |
    And Exists dish at restaurant "Unknown" by "user2"
      | name            |
      | Apple Pie       |
    And Exists review at restaurant "Famous" by "user1"
      | rating          | comment       |
      | 4               | Quite good    |
    And Exists review at restaurant "Famous" by "user2"
      | rating          |
      | 2               |

  Scenario: View details for owned restaurant with two reviews and a dish
    Given I login as user "user1" with password "password"
    When I view the details for restaurant "Famous"
    Then I'm viewing restaurants details including
      | name            | city          | country       |
      | Famous          | London        | England       |
    And There is "edit" link available
    And I'm viewing a restaurant reviews list containing
      | rating          | comment       | user          |
      | 4               | Quite good    | user1         |
      | 2               |               | user2         |
    And The list contains 2 reviews
    And I'm viewing a restaurant dishes list containing
      | name            | user          |
      | Fish and Chips  | user1         |
    And The list contains 1 dishes

  Scenario: View details for other user restaurant with 1 dish but no reviews
    Given I login as user "user2" with password "password"
    When I view the details for restaurant "Unknown"
    Then I'm viewing restaurants details including
      | name            | city          | country       |
      | Unknown         | Paris         | France        |
    And There is no "edit" link available
    And I'm viewing a restaurant dishes list containing
      | rating          | comment       | user          |
    And The list contains 0 reviews
    And I'm viewing a restaurant dishes list containing
      | name            |
      | Apple Pie       |
    And The list contains 1 dishes

  Scenario: View details for restaurant with 1 dish but no reviews when not logged in
    Given I'm not logged in
    When I view the details for restaurant "Unknown"
    Then I'm viewing restaurants details including
      | name            | city          | country       |
      | Unknown         | Paris         | France        |
    And There is no "edit" link available
    And I'm viewing a restaurant dishes list containing
      | rating          | comment       | user          |
    And The list contains 0 reviews
    And I'm viewing a restaurant dishes list containing
      | name            |
      | Apple Pie       |
    And The list contains 1 dishes