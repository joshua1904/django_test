from django.http import HttpResponse
from django.shortcuts import render
from .scripts import get_quiz_question
# Create your views here.

def get_quiz(request):
    if request.method == "POST":
        user_answer = request.POST.get("quizAnswer")
        correct_answer = request.session.get("correct_answer")
        question = request.session.get("question")
        if user_answer == correct_answer:
            return render(request, "answer.html", {"message": f"Richtig! Die Antwort auf die Frage: \"{question}\" is  \"{correct_answer}\""})
        else:
            return render(request, "answer.html", {"message": f"Falsch, die Richtige Antwort auf die Frage: \"{question}\" lautet: \"{correct_answer}\" und nicht {user_answer}"})
    question = get_quiz_question()
    request.session["correct_answer"] = question.correct_answer
    request.session["question"] = question.question
    return render(request, "quiz.html", {"question": question})