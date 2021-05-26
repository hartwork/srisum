# About `srisum`

**srisum** is a minimal command-line tool to
compute and display
the [Subresource Integrity](https://developer.mozilla.org/en-US/docs/Web/Security/Subresource_Integrity) checksum
of a local file or a remote file accessible via an HTTPS URL.

That is useful in at least these two contexts:

- Adding new static file asset to an existing HTML document
- Bumping a nixOS package for nixOS from a non-nixOS host

**srisum** is software libre
written in Python 3
and licensed under the MIT license.


# Installation

```console
# pip install srisum
```


# Example

```
# srisum https://github.com/libexpat/libexpat/releases/download/R_2_4_1/expat-2.4.1.tar.xz
sha256-zwMtDbqbkoY2VI4ysyei1msaq2PE9KE90TLC0dLy+2o=
```


# Alternatives

## JavaScript

- [`zkat/srisum`](https://github.com/zkat/srisum) — package `srisum` [on npm](https://www.npmjs.com/package/srisum)


## Python

- [`hartwork/srisum`](https://github.com/hartwork/srisum) — package `srisum` [on PyPI](https://pypi.org/project/srisum/)


## Rust

- [`zkat/srisum-rs`](https://github.com/zkat/srisum-rs) — package `srisum` [on crates.io](https://crates.io/crates/srisum)
