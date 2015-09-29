from helga.plugins import match
from helga import log

logger = log.getLogger(__name__)


@match(r'\w* ?[:,] ?ping\W*$', priority=101)
def naked_ping(client, channel, nick, message, matches):
    """
    Annoy users on naked pings
    """
    logger.debug('matched a naked ping')
    return "%s: consider using pings with data please. See: https://blogs.gnome.org/markmc/2014/02/20/naked-pings/" % nick
