## Official Add-on repository of Xodi 5.0+.
Xodi File Manager Source: https://xbmc4xbox.github.io/repository.xodi.org/

Xodi 5.0 (Omega) add-on sources live in `omega/`, with generated packages,
the add-on index, and its checksum in `omega/zips/`. Later releases can use
their own codename directories.

Initialize the pinned add-on submodules after cloning:

```sh
git submodule update --init --recursive
```

To generate the Omega packages and index from the repository root:

```sh
python3 -B -c "from _repo_generator import Generator; Generator('omega')"
```
