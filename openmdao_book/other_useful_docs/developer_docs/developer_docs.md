# Developer Docs (if you're going to contribute code)
---


## Developer Install
-----------------

Use `git` to clone the repository:

`git clone http://github.com/OpenMDAO/OpenMDAO`

Use `pip` to install openmdao locally:

`cd OpenMDAO`

`pip install -e .`

```{note}
The `-e` option tells pip to install directly from your repository. This is very useful when you're developing because when you change the code or pull new commits down from GitHub, you don't necessarily need to re-run the `pip install`.
```

## Building the Docs
---
You can read the docs online, so it is not necessary to build them locally on your machine.
But if you're going to build new features or add new examples, you'll want to build the docs locally, so that you can check them while you are writing them.

- [Local Building of OpenMDAO Documentation]()
- [Automating Doc Build and Custom Doc Deployment from Travis CI]()
- [Caching on Travis CI]()


## Creating Your Own OpenMDAO Plugins
---

- [How To Write OpenMDAO Plugins]()


## Documentation Style Guide
---

This document exists to help OpenMDAO documentation writers follow appropriate guidelines,
in terms of formatting and embedding code.

- [OpenMDAO Docs Style Guide](doc_style_guide.ipynb)
- [Sphinx and Decorated Methods]()


