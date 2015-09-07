import urllib


def setup_jinja2_filters(jinja_env):
    jinja_env.filters['pretty_days_away'] = _pretty_days_away
    jinja_env.filters['urlencode'] = _urlencode
    jinja_env.filters['title_case'] = _title_case
    jinja_env.filters['sentence_case'] = _sentence_case


def _pretty_days_away(days):
    if days is None:
        return "TDB"
    elif days == -1:
        return "Yesterday"
    elif days == 0:
        return "Today"
    elif days == 1:
        return "Tomorrow"
    elif days < -1:
        return "{0} Days Ago".format(days * -1)
    return "{0} Days".format(days)


def _urlencode(val):
    return urllib.quote_plus(val).replace("%E9", "e")


def _title_case(val):
    return ' '.join([ s[0:1].upper() + s[1:] for s in val.split(' ') ])


def _sentence_case(s):
    return s[0:1].upper() + s[1:]

