The county registrar has an api that can be queried like (using [httpie][0]):

http \
    --form \
    https://www.sdvote.com/bin/sdc/electioninfo \
    houseNumber=8125 \
    streetName=fletcher \
    streetType=pkwy \
    zipCode=91942

[0]: https://httpie.io
