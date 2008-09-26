"""

A Django implementation of email-to-a-friend
that works with unregistered or registered users.

"""

import datetime

from django.contrib.contenttypes.models import ContentType
import django.db

from emailthis.models import EmailEvent

def get_most_emailed(numdays=7, limit=10):
    """
    Returns the most emailed <limit> things of the last <numdays> days as a list
    of (count, thing) tuples.
    """
    sql="""
    SELECT count(e.*) as cnt, e.content_type_id, e.object_id
    FROM emailthis_emailevent e
    WHERE happened_at >= %%s
    GROUP BY e.content_type_id, e.object_id
    ORDER BY cnt DESC
    LIMIT %d

    """ % limit
    when=datetime.datetime.now() - datetime.timedelta(days=numdays)
    c=django.db.connection.cursor()
    c.execute(sql, (when,))
    res=c.fetchall()
    ctypes=dict((x.pk, x) for x in ContentType.objects.filter(pk__in=set(r[1] for r in res)))
    return [(cnt, ctypes[ct].get_object_for_this_type(pk=oid)) for cnt, ct, oid in res]
