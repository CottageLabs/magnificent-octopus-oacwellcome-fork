import requests
from octopus.core import app


class CrossRefAPIException(Exception):
    pass


class Crossref(object):

    @classmethod
    def get_by_doi(cls, unencoded_doi):
        try:
            r = requests.get(app.config['CROSSREF_API_BY_DOI'] + unencoded_doi)
        except KeyError as e:
            raise CrossRefAPIException(
                "You have to have the CROSSREF_API_BY_DOI config var set "
                "to use the Crossref.get_by_doi method. Original "
                "exception message: \n{0}".format(e.message)
            )
        except Exception as e:
            raise CrossRefAPIException(
                "Unknown problem while talking to Crossref API. Original "
                "exception: \n{0}".format(e.message)
            )

        j = r.json()
        if j['status'] != 'ok':
            raise CrossRefAPIException(
                "Unknown problem while talking to Crossref API. "
                "Status was not \"ok\" in response envelope."
            )

        return j['message']
