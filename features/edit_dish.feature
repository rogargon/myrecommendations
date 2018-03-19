Feature: Edit Dish
  In order to keep updated my previous registers about dishes
  As a user
  I want to edit a dish register I created

  Background: There are registered users and a dish by one of them
    Given Exists a user "user1" with password "password"
    And Exists a user "user2" with password "password"
    And Exists restaurant registered by "user1"
      | name            | city            | country         |
      | The Tavern      | London          | USA             |
    And Exists dish at restaurant "The Tavern" by "user2"
      | name            | price           |
      | Fish and Chips  | 12.50           |

  Scenario: Edit owned restaurant registry country
    Given I login as user "user2" with password "password"
    When I view the details for dish "Fish and Chips"
    And I edit the current dish
      | price           |
      | 11.49           |
    Then I'm viewing the details page for dish at restaurant "The Tavern" by "user2"
      | name            | price           |
      | Fish and Chips  | 11.49           |
    And There are 1 dishes

  Scenario: Try to edit dish but not logged in
    Given I'm not logged in
    When I view the details for dish "Fish and Chips"
    Then There is no "edit" link available

  Scenario: Try to edit dish but not the owner
    Given I login as user "user1" with password "password"
    When I view the details for dish "Fish and Chips"
    Then There is no "edit" link available
