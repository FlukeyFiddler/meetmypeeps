Feature: Homepage
  As a new visitor
  I want to see a working site

  Scenario: Visit Homepage

    Given I land on the site
    Then I will see "Meet My Peeps" in the title bar
    And I will see "Meet My Peeps" in the H1 tag
    And I see the event form
    And I will see a Google Map

