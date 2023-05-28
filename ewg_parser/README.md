## Security

No personal information should ever be committed to this repo.
The tools we write here should be able to read a csv of addresses, then output that same csv amended with columns of precinct information.
No data should be transmitted in bulk to any service.

## What and why "poetry"?

[Poetry][0] lets us declare library dependencies in a non-hellish way.
If you're used to popular package managers used with javascript, rust, golang, ruby, et al; it's that.
Also, it uses virtualenv.
The packages needed by these python projects won't interfere with your other python projects.

To get into the venv, run

    poetry shell

To run a particular project:

    poetry run python hello_world

## What's all in here anyway

There's two approaches..

### county_api

We found a county website with a form intended for San Diego County voters to find their elected officials.
It doesn't generalize beyond our chapter, but I believe has all the information our chapter cares about.

### geonom

This approach would use gis information.
We'll need to geocode addresses.
Then query sources of precinct information.

This path is a lot more complex.
But, it generalizes beyond our own county.
Bring your own shapes and address csv, press go, brrrrr, and you get a csv amended with precinct data.

[Nominatim][1] is software that can hold gis data and answer questions.
Running it ourselves would be the ideal for security.
But OpenStreetMap does have a free service we could use.


[0]: https://python-poetry.org/docs/basic-usage/
[1]: https://nominatim.org