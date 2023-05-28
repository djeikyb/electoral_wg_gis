import datetime
import typing
from dataclasses import dataclass, asdict

import requests as requests

import logging
from http.client import HTTPConnection

# Enabling debugging at http.client level (requests->urllib3->http.client)
# you will see the REQUEST, including HEADERS and DATA, and RESPONSE with HEADERS but without DATA.
# the only thing missing will be the response.body which is not logged.
HTTPConnection.debuglevel = 1
logging.basicConfig()  # you need to initialize logging, otherwise you will not see anything from requests
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True


@dataclass
class NominatumSearchParameter:
    """Should only be number and street name. DO NOT include suite or apartment identifiers"""
    street: str

    city: str
    state: str

    """Must be two letter iana code"""
    country: str

    postalcode: str

    def query(self):
        l = filter(lambda x: x is not None, asdict(self).values())
        return ", ".join(l)


def query_address():
    nom_query: NominatumSearchParameter = NominatumSearchParameter(
        street="4265 Fairmount Avenue",
        city="san diego",
        state="ca",
        postalcode="92105",
        country="us",
    )

    # format: typing.Literal["xml", "json", "jsonv2", "geojson", "geocodejson"]
    d = {"q": nom_query.query(), "addressdetails": 1, "format": "xml"}

    print(d)
    res = requests.get('https://nominatim.openstreetmap.org/search', params=d)
    print(res.status_code)
    print(res.text)


class MemberGeocoded:
    AK_ID: str
    lat: float
    lon: float


class MemberInfo:
    AK_ID: str
    first_name: str
    middle_name: str
    last_name: str
    suffix: str
    Billing_Address_Line_1: str
    Billing_Address_Line_2: str
    Billing_City: str
    Billing_State: str
    Billing_Zip: str
    Mailing_Address1: str
    Mailing_Address2: str
    Mailing_City: str
    Mailing_State: str
    Mailing_Zip: str
    Mobile_Phone: str
    Home_Phone: str
    Work_Phone: str
    Email: str
    Mail_preference: str
    Do_Not_Call: str
    Join_Date: str
    Xdate: str
    membership_type: str
    monthly_dues_status: str
    membership_status: str
    union_member: str
    union_name: str
    union_local: str
    student_yes_no: str
    student_school_name: str
    YDSA_Chapter: str
    DSA_chapter: str


if __name__ == "__main__":
    query_address()
