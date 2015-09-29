from helga.plugins import match


@match(r'\w* ?[:,] ?ping\W*$', priority=101)
def naked_ping(client, channel, nick, message, matches):
    """
    Annoy users on naked pings
    """
    return "%s: consider using pings with data please. See: https://blogs.gnome.org/markmc/2014/02/20/naked-pings/" % nick
