#!/usr/bin/env python

import sys
import smtplib
import uuid
from datetime import date, datetime
import time

from email.mime.text import MIMEText

# Where, from whom, subject and what to send:
to = u"MusicBrainz Developer Discussion <musicbrainz-devel@lists.musicbrainz.org>"
sender = "Statler & Waldorf <noreply@musicbrainz.org>"
subject_template = u"Dev chat reminder, issue %s"
msg_template = u'''We've got our weekly dev chat on %s on IRC in #musicbrainz-devel on irc.freenode.net. We're going to meet at Regular Meeting Time [1] (%s).

%sIf there is any topic you would like to discuss during the meeting, please add it to the agenda in the channel topic.

[1] http://musicbrainz.org/doc/Development_Chat

--
This message brought to you by https://github.com/mayhem/statler-waldorf
Don't even think of responding to this email. We won't answer! http://goo.gl/FSZdF
''';

meeting_time = 19 # UTC

unow = datetime.utcnow()
udate = date(unow.year, unow.month, unow.day)

if udate.weekday() == 0 and unow.hour < meeting_time:
    meeting_date = udate
else:
    meeting_date = date.fromtimestamp(time.time() + ((7 - udate.weekday()) * 24 * 60 * 60))

subject = subject_template % uuid.uuid4().hex
msg = MIMEText(msg_template % (meeting_date.strftime("%Y-%m-%d"), "%02d:00 UTC" % meeting_time, ""))

msg['Subject'] = subject
msg['From'] = sender
msg['To'] = to

s = smtplib.SMTP('localhost')
s.sendmail(sender, [to], msg.as_string())
s.quit()
