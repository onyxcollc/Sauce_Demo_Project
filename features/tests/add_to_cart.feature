Feature: User should be able to add inventories into cart and checkout



  Scenario: User should be able to select items into cart and verify cart badge
    Given Open sauce demo webpage
    When Enter Username standard_user
    When Enter Password secret_sauce
    And Click Login button
    When Add several items to cart
    And Click cart icon
    Then Verify cart badge number updates




  Scenario: User should be able to select items into cart and checkout
    Given Open sauce demo webpage
    When Enter Username standard_user
    When Enter Password secret_sauce
    And Click Login button
    When Add several items to cart
    And Click cart icon
    When Click Checkout button
    When Fill out Checkout information
    And Click Continue button
    When Click Finished button
    Then Verify Checkout Complete