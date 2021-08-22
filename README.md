## Information

This repository is a fork of phenom4n4n's [TagScript](https://github.com/phenom4n4n/TagScript) which is a fork of JonSnowbd's [TagScript](https://github.com/JonSnowbd/TagScript).

This fork adds stuff or adjust certain stuff for my discord bot Z3R0 (ziBot). For general usage please use phenom4n4n's [TagScript](https://github.com/phenom4n4n/TagScript) instead!

## Installation

Download the latest version through pip:

```
pip(3) install git+https://github.com/ZiRO-Bot/TagScript.git
```

Download from a commit:

```
pip(3) install git+https://github.com/ZiRO-Bot/TagScript.git@<COMMIT_HASH>
```

Install for editing/development:

```
git clone https://github.com/ZiRO-Bot/TagScript.git
pip(3) install -e ./TagScript
```

## What?

TagScript is a drop in easy to use string interpreter that lets you provide users with ways of
customizing their profiles or chat rooms with interactive text.

For example TagScript comes out of the box with a random block that would let users provide
a template that produces a new result each time its ran, or assign math and variables for later
use. See [the documentation folder](https://github.com/JonSnowbd/TagScript/tree/v2/Documentation) for
some design documents and basic tutorials or hit up our [biggest user's documentation](https://docs.carl.gg/tags-and-triggers/tags-advanced-usage/) to see how its being used
on one of the biggest bots on discord!

## Dependencies

`Python 3.5+` due to type hinting

`PyParsing` provides the math block with intelligent mathematical expressions

`PyGObject` is required if one wants to use the playground feature
