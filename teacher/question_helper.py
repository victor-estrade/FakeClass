# coding: utf-8
from __future__ import division
from __future__ import print_function
from __future__ import absolute_import
from __future__ import unicode_literals

from .evaluation import ensure_score
from .evaluation import evaluate

def Score(sc):
    def score_decorator(question):
        question.score = sc
        question.max_score = sc
        return question
    return score_decorator


def Combine(*args):
    total_score = sum([ensure_score(sub_q).score for sub_q in args])
    def combine_decorator(question):
        def new_question(answer):
            new_question.score = sum([evaluate(sub_q, answer).score for sub_q in args])
            return None
        new_question.__name__ = question.__name__
        new_question.score = total_score
        new_question.max_score = total_score
        return new_question
    return combine_decorator

