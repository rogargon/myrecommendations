Feature: Register Restaurant
  In order to keep track of the restaurants I visit
  As a user
  I want to register a restaurant together with its location and contact details

  Background: There is a registered user
    Given Exists a user "user" with password "password"

  Scenario: Register just restaurant name
    Given I login as user "user" with password "password"
    When I register restaurant
      | name        |
      | The Tavern  |
    Then I'm viewing the details page for restaurant
      | name        |
      | The Tavern  |
    And There are 1 restaurants
