Feature: Storytime original features

Scenario Outline: Stories

	Given I enter that my name is <name>
	  And I enter that my gender is <gender>
	  And I enter the date <date>
	 Then I expect the first scentence to contain <name>
	  And I expect the second scentence to begin with <pronoun>

Examples:
	| name	| gender | date  | pronoun |
	| Al	| boy	 | today | he	   |
