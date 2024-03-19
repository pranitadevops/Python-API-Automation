Feature: Bank Transaction
  Tests to Bank Transactions like withdrawal,deposit

  Scenario: Withdrawal money
    Given the account balance is 100
    When the account holder withdrawn 100
    Then the account balance should be 70