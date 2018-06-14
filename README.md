# sublime_black

[![Licence](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/csurfer/sublime_black/master/LICENSE)
[![Thanks](https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg)](https://saythanks.io/to/csurfer)

SublimeText3 package to format python code using black formatter.

![Demo](https://i.imgur.com/10aO24T.gif)

## Features

* **Black: Diff** to see the changes that would be done to the file.
* **Black: Format** to format the file in place using [black](https://github.com/ambv/black).

## Prerequisites

* Install [black](https://github.com/ambv/black) and ensure you can use it in command line to format files.

## Setup

### Directly from the repository

Clone the git repo into your `Packages` folder using

```python
git clone https://github.com/csurfer/sublime_black Black
```

and restart SublimeText3.

### Package Control

Submitted to Package Control on May 1st 2018. Should be available soon!

## Settings

* Line length setting for the package is set to 88 by default to be in sync with `black`. If you intend to change the same `Open command palette -> Goto Preferences: Black Settings - User -> Change "line_length"` to the value you desire.
* Locale setting for the package (required by click's http://click.pocoo.org/5/python3/#python-3-surrogate-handling) by default is set to `en_CA.UTF-8`. If you intend to change the same `Open command palette -> Goto Preferences: Black Settings - User -> Change "encoding"` to the value you desire.
* String quotes or prefixes are normalized by the default to be in sync with `black`. This works great for new projects, but may not be the default you want for existing projects. Check out [the docs](https://github.com/ambv/black#strings) for specific details. If you intend to change the same `Open command palette -> Goto Preferences: Black Settings - User -> Change "skip_string_normalization"` to either `true` or `false` (the default).

## Notes

* Currently supports only saved file formatting due to conflict between SublimeText3 default python version (3.3) and [black](https://github.com/ambv/black) supported version (3.6).
* More to come as soon as SublimeText supports latest python version.

## Contributing

### Bug Reports and Feature Requests

Please use [issue tracker](https://github.com/csurfer/sublime_black/issues) for reporting bugs or feature requests.

### Development

Pull requests are most welcome.

### Buy the developer a cup of coffee!

If you found the utility helpful you can buy me a cup of coffee using

[![Donate](https://www.paypalobjects.com/webstatic/en_US/i/btn/png/silver-pill-paypal-44px.png)](https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=3BSBW7D45C4YN&lc=US&currency_code=USD&bn=PP%2dDonationsBF%3abtn_donate_SM%2egif%3aNonHosted)
