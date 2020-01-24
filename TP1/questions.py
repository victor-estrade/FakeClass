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


@Score(1/4)
@SubQuestion('question_02')
def question_02_a(answer):
	"""
	number of features ?
	"""
	CORRECT = 4
	assert answer().get('nb_features', None) == CORRECT

@Score(1/4)
@SubQuestion('question_02')
def question_02_b(answer):
	"""
	number of training samples ?
	"""
	CORRECT = 35
	assert answer().get('nb_training_samples', None) == CORRECT

@Score(1/4)
@SubQuestion('question_02')
def question_02_c(answer):
	"""
	number of validation samples ?
	"""
	CORRECT = 35
	assert answer().get('nb_validation_samples', None) == CORRECT

@Score(1/4)
@SubQuestion('question_02')
def question_02_d(answer):
	"""
	number of test samples ?
	"""
	CORRECT = 35
	assert answer().get('nb_test_samples', None) == CORRECT



@Score(1/4)
@SubQuestion('question_03')
def question_03_a(answer):
	"""
	Open and read given code and answer simple question
	"""
	CORRECT = "np"
	assert answer().get("import_numpy_as", None) == CORRECT

@Score(1/4)
@SubQuestion('question_03')
def question_03_b(answer):
	"""
	Open and read given code and answer simple question
	"""
	CORRECT = "pd"
	assert answer().get("import_pandas_as", None) == CORRECT, "hint : PanDas"

@Score(1/4)
@SubQuestion('question_03')
def question_03_c(answer):
	"""
	Open and read given code and answer simple question
	"""
	CORRECT = "basename"
	assert answer().get("name_of_first_argument_of_read_as_df", None) == CORRECT

@Score(1/4)
@SubQuestion('question_03')
def question_03_d(answer):
	"""
	Open and read given code and answer simple question
	"""
	CORRECT = "train"
	assert answer().get("default_value_of_second_argument_of_read_as_df", None) == CORRECT
