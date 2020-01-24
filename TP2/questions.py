# coding: utf-8
from __future__ import division
from __future__ import print_function
from __future__ import absolute_import
from __future__ import unicode_literals

from teacher import Score
from teacher import SubQuestion

def question_01(answer):
	"""
	Just read !
	"""
	CORRECT = 1
	assert answer() == CORRECT, 'hint : I am one'



def question_02(answer):
	"""
	square(2) == 4
	"""
	assert answer(2) == 4


def question_03(answer):
	"""
	Try external code
	"""
	assert answer(3) == 9


def question_04(answer):
	"""
	Try external code
	"""
	assert answer(1) == 1


