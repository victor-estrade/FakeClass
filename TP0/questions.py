from teacher import Combine
from teacher import Score

def question_00(answer):
    """
    Remind question
    Explain answer
    """
    CORRECT = 0
    assert answer() == CORRECT

@Score(1)
def question_01(answer):
    """
    Remind question
    Explain answer
    """
    pass

def sub_question_02_a(answer):
    pass

def sub_question_02_b(answer):
    pass

@Score(1.5)
def sub_question_02_c(answer):
    assert 1 == 0, '1 != 0'

@Combine(sub_question_02_a, sub_question_02_b, sub_question_02_c, )
def question_02(answer):
    pass


@Score(1)
def question_0e(answer):
    """
    Remind question
    Explain answer
    """
    raise ValueError('A free value error')

