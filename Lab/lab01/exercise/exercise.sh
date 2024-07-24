#! /usr/bin/bash

python manage.py shell

>>> from mypolls.models import Question, Choice
>>> from django.utils import timezone as tz
>>> import datetime as dt

>>> q1 = Question(question = "What is up?", date = tz.now())
>>> q1.question = "What's up?"
>>> q1.save()

# exercise 01

>>> q2 = Question(question = "Hello World?", date = dt.datetime(2024, 1, 1, 11))
>>> q2.save()

# exercise 02

>>> c1 = Choice(question = q1, choice = "Yes", votes = 0)
>>> c2 = Choice(question = q1, choice = "No", votes = 0)
>>> c3 = Choice(question = q1, choice = "OK", votes = 0)
>>> c1.save()
>>> c2.save()
>>> c3.save()

# exercise 03

>>> q2.choice_set.create(choice = "Bye", votes = 0)
>>> q2.choice_set.create(choice = "Hello", votes = 0)

