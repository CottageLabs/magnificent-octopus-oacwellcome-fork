from lxml import etree
import re

encoding_rx = re.compile('^<\?xml .*encoding=["\'](.+?)["\'].*\?>')

def detect_encoding(s):
    m = encoding_rx.match(s)
    if m is None:
        return None
    return m.group(1)

def fromstring(s):
    # first try and parse the string directly
    error = None
    try:
        return etree.fromstring(s)
    except ValueError as e:
        error = e

    # if this failed, and this is not a unicode string, then just raise
    # the exception, as there's nothing more to do for now
    if not isinstance(s, unicode):
        raise error

    # our next best bet is to attempt to encode the unicode to a byte-stream
    # with the relevant encoding
    enc = detect_encoding(s)
    if enc is not None:
        try:
            bs = s.encode(enc)
            return etree.fromstring(bs)
        except LookupError:
            # this means the detected encoding is junk
            pass
        except ValueError as e:
            # we had a problem parsing with the given encoding
            pass

    # if we get here, we failed to decode or failed to parse.  Let's therefore strip
    # the encoding declaration and see if lxml can sort it out (and just let the
    # error raise as necessary)
    clean = encoding_rx.sub("", s).strip()
    return etree.fromstring(clean)

