def user_time_update(user):
    try:
        session = UserSession.objects.get(user=user, running=True)
    except:
        return -1
    have_time = session.registered_at + timedelta(minutes=TIME_FOR_ATTEMT) - timezone.now()
    have_minutes = have_time.total_seconds() / 60
    if have_minutes <= 0:
        session.running = False
        session.save()
    return int(have_minutes)


def test_answer_inside(sql_query, right_sql_query):
    return Review.check_answer(sql_query=sql_query, right_sql_query=right_sql_query)


def toHex(x):
    return "".join([hex(ord(c))[2:].zfill(2) for c in x])