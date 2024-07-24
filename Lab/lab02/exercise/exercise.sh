#! /usr/bin/bash

python manage.py shell

# exercise Datetime & Timezone

>>> from datetime import datetime as dt, timedelta as delta
>>> from django.utils import timezone as tz

# exercise 01

>>> now = tz.make_aware(dt.now())
>>> print(now)

# exercise 02

>>> future = now + delta(days = 500)
>>> future.weekday() # Monday = 0, Sunday = 6
>>> future.isoweekday() # Monday = 1, Sunday = 7
