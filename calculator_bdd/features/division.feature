Feature: dividing two numbers

  Scenario: when dividing two non-zero integers
    Given two valid non-zero integers
    When dividing the non-zero integers
    Then it should result to another integer

  Scenario: when dividing zero with a non-zero integer
    Given zero and a non-zero integer
    When dividing zero with the non-zero integer
    Then is should result to zero
 
  Scenario: when dividing a non-zero integer with zero
    Given a non-zero integer and zero
    When dividing the non-zero integer with zero
    Then it should result to undefined
  
  Scenario: when dividing two zeroes
    Given two zeroes
    When dividing the two zeroes
    Then it should result to undefined