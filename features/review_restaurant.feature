Feature: Register Review
  In order to share my opinion about a restaurant
  As a user
  I want to register a review with a rating and comment about a restaurant

  Background: There is a registered user and restaurant
    Given Exists a user "user" with password "password"
    And Exists restaurant registered by "user"
      | name            |
      | The Tavern      |

  Scenario: Register review with rating and comment
    Given I login as user "user" with password "password"
    When I register a review at restaurant "The Tavern"
      | rating          | comment       |
      | 4               | Quite good    |
    Then I'm viewing the details page for restaurant by "user"
      | name            |
      | The Tavern      |
    And I'm viewing a restaurant reviews list containing
      | rating          | comment       | user          |
      | 4               | Quite good    | user          |
    And The list contains 1 reviews
    And There are 1 reviews

  Scenario: Try to register review but not logged in
    Given I'm not logged in
    When I register a review at restaurant "The Tavern"
      | rating          | comment       |
      | 4               | Quite good    |
    Then I'm redirected to the login form
    And There are 0 reviews

  Scenario: User reviews same restaurant replaces previous review
    Given Exists review at restaurant "The Tavern" by "user"
      | rating          | comment       |
      | 4               | Quite good    |
    And I login as user "user" with password "password"
    When I register a review at restaurant "The Tavern"
      | rating          | comment       |
      | 2               | Not so happy  |
    Then I'm viewing the details page for restaurant by "user"
      | name            |
      | The Tavern      |
    And I'm viewing a restaurant reviews list containing
      | rating          | comment       | user          |
      | 2               | Not so happy  | user          |
    And The list contains 1 reviews
    And There are 1 reviews
