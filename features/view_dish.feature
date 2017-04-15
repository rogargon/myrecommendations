Feature: View Dish
  In order to know about a dish
  As a user
  I want to view the registered dish details

  Background: There is one restaurant with 2 dishes and another without
    Given Exists a user "user1" with password "password"
    And Exists a user "user2" with password "password"
    And Exists restaurant registered by "user1"
      | name            |
      | The Tavern      |
    And Exists dish at restaurant "The Tavern" by "user1"
      | name            | price           |
      | Fish and Chips  | 12.50           |
    And Exists dish at restaurant "The Tavern" by "user2"
      | name            | description     |
      | Apple Pie       | The best pie in town |

  Scenario: View details about owned dish
    Given I login as user "user1" with password "password"
    When I view the details for dish "Fish and Chips"
    Then I'm viewing dish details including
      | name            | price           |
      | Fish and Chips  | 12.50           |
    And There is "edit" link available

  Scenario: View details about dish but not logged in
    Given I'm not logged in
    When I view the details for dish "Fish and Chips"
    Then I'm viewing dish details including
      | name            | price           |
      | Fish and Chips  | 12.50           |
    And There is no "edit" link available

  Scenario: View details about other user dish
      Given I login as user "user1" with password "password"
    When I view the details for dish "Apple Pie"
    Then I'm viewing dish details including
      | name            | description     |
      | Apple Pie       | The best pie in town |
    And There is no "edit" link available
