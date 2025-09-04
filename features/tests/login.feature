Feature: User should be able to login to webpage


  Scenario: User logging into sauce demo webpage valid credentials
    Given Open sauce demo webpage
    When Enter Username standard_user
    When Enter Password secret_sauce
    And Click Login button
    Then Verify you are logged In


    Scenario: User logging into sauce demo webpage invalid credentials
    Given Open sauce demo webpage
    When Enter Username happy_user
    When Enter Password hot_sauce
    And Click Login button
    Then Verify error message
