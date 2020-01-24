# coding: utf-8
from __future__ import division
from __future__ import print_function
from __future__ import absolute_import
from __future__ import unicode_literals

from .student_code import square
from bad_student_code import square_bis

def answer_01():
	"""
	Just read !
	"""
	solution = None
	return solution


def answer_02(x):
	"""
	Make a square funtion
	"""
	return x * x


def answer_03(x):
	"""
	Make a square in another module.
	Import it (relative import) and return its results
	"""
	x = square(x)
	return x


def answer_04(x):
	"""
	Make a square in another module.
	Import it (absolute import) and return its results
	"""
	x = square_bis(x)
	return x
