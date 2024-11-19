import copy
from random import shuffle

import requests
from requests import Response
from dataclasses import dataclass


@dataclass
class Quiz:
    type: str
    difficulty: str
    category: str
    category: str
    question: str
    correct_answer: str
    incorrect_answers: list[str]

    def get_all_answers(self):
        wrong_answers = copy.copy(self.incorrect_answers)
        wrong_answers.append(self.correct_answer)
        shuffle(wrong_answers)
        return wrong_answers

def get_quiz_question() -> Quiz:
    return Quiz(**requests.get("https://opentdb.com/api.php?amount=1").json()["results"][0])




