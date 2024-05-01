# gimme-shelter

Gimme Shelter is a Demo server app using `streamlit` that asks an LLM to write a personalized letter to the landlord of a free apartment in Berlin, if the user provides it with some information about the apartment.

- [gimme-shelter](#gimme-shelter)
  - [Develop](#develop)
  - [Build](#build)
  - [License](#license)

## Develop

Its easiest to use [![Hatch project](https://img.shields.io/badge/%F0%9F%A5%9A-Hatch-4051b5.svg)](https://github.com/pypa/hatch) as project manager for developemnt and so on. To start the dev server you can just run

```console
hatch run serve
```

from the project root.

## Build

This becomes a bit more tricky. First you need to build with hatch, the generate a requirements.txt for docker
and build the docker image.

```console
hatch build -t sdist
hatch show deps requirements.txt > dist
docker build -t [SOME TAG] -n gimme-shelter
```

A demo if this container is hosted on [fly.io](fly.io).

## License

`gimme-shelter` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
