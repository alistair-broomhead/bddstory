# -*- coding: utf-8 -*-
from lettuce import step
import subprocess

STORYTIME = subprocess.Popen('/home/pi/storytime2/bin/python ../storytime.py', stdin=subprocess.PIPE, stdout=subprocess.PIPE)
OUT = []


@step(u'Given I enter that my name is (\w+)')
def given_i_enter_that_my_name_is_name(step, name):
    STORYTIME.communicate(name)


@step(u'And I enter that my gender is (\w+)')
def and_i_enter_that_my_gender_is_gender(step, gender):
    STORYTIME.communicate(gender)


@step(u'And I enter the date (.+)')
def and_i_enter_the_date_date(step, date):
    OUT.append(STORYTIME.communicate(date)[0])


@step(u'Then I expect the first scentence to contain (\w+)')
def then_i_expect_the_first_scentence_to_contain_name(step, name):
    
    assert False, OUT


@step(u'And I expect the second scentence to begin with (\w+)')
def and_i_expect_the_second_scentence_to_begin_with_pronoun(step, pronoun):
    assert False, 'This step must be implemented'
