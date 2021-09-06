Feature: whyscount Login
  Scenario: Login to Whyscount with valid credentials
    Given I Launch Chrome browser
    When I open wyscout Homepage
    And Enter username"poojamulke77@gmail.com" and Password "pw_IndiaTest!"
    And Click on Login button
    Then User must successfully login to the Whyscount Homepage
