Feature: Register Dish
  In order to keep track of the dishes I eat
  As a user
  I want to register a dish in the corresponding restaurant together with its details

  Background: There is a registered user and restaurant
    Given Exists a user "user" with password "password"
    And Exists restaurant registered by "user"
      | name            |
      | The Tavern      |

  Scenario: Register just dish name
    Given I login as user "user" with password "password"
    When I register dish at restaurant "The Tavern"
      | name            |
      | Fish and Chips  |
    Then I'm viewing the details page for dish at restaurant "The Tavern" by "user"
      | name            |
      | Fish and Chips  |
    And There are 1 dishes

  Scenario: Register dish with picture
    Given I login as user "user" with password "password"
    When I register dish at restaurant "The Tavern"
      | name            | image                    |
      | Fish and Chips  | features/random.png      |
    Then I'm viewing the details page for dish at restaurant "The Tavern" by "user"
      | name            | image                    |
      | Fish and Chips  | myrestaurants/random.png |
    And There are 1 dishes

  Scenario: Try to register dish but not logged in
    Given I'm not logged in
    When I register dish at restaurant "The Tavern"
      | name            |
      | Fish and Chips  |
    Then I'm redirected to the login form
    And There are 0 dishes
