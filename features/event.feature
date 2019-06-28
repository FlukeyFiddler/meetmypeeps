Feature: As a user, I want to be able to add an event
    and see events in my neighbourhood

  Scenario: Add event

    Given I land on the site
    Then I see the event form
    And  I enter my latitude "52.2345504", longitude "5.9870061", title "bday partay" and date "21-07-2999"
    And I will see a table that displays my events

