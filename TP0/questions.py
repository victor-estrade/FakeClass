from teacher import Score
from teacher import SubQuestion

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


@SubQuestion('question_02')
def question_02_a(answer):
    pass

@SubQuestion('question_02')
def question_02_b(answer):
    pass

@Score(1.5)
@SubQuestion('question_02')
def question_02_c(answer):
    assert 1 == 0, '1 != 0'


@Score(1)
def question_0e(answer):
    """
    Remind question
    Explain answer
    """
    raise ValueError('A free value error')


@SubQuestion("question_55")
def question_04(answer):
    pass
