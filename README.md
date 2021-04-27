# Denodo Client

[![PyPI license](https://img.shields.io/pypi/l/denodoclient.svg)](https://pypi.python.org/pypi/denodoclient/)
[![PyPI version shields.io](https://img.shields.io/pypi/v/denodoclient.svg)](https://pypi.python.org/pypi/denodoclient/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/denodoclient.svg)](https://pypi.python.org/pypi/denodoclient/)
[![PyPI download month](https://img.shields.io/pypi/dm/denodoclient.svg)](https://pypi.python.org/pypi/denodoclient/)
![Unit tests](https://github.com/dfds-data/denodoclient/actions/workflows/python-package.yml/badge.svg)
![Publish to pypi](https://github.com/dfds-data/denodoclient/actions/workflows/python-publish.yml/badge.svg)

Thin high level client to use when consuming data through the Denodo proprietory ODBC driver.

This project is not in any way associated with Denodo.

- Free software: MIT license

# Features

- ODBC cursor low-level access to Denodo with sensible default connection string
- High-level client using Pandas to fetch results to a dataframe, all in one go or chunkwise
- Simple query templating functionality

# How to use

Requires python 3.8 or higher.

```bash
pip install denodoclient pandas
```

## Query to dataframe

```python
from denodoclient.dataframes import DenodoDataFrameClient
from denodoclient import VqlQuery
from pathlib import Path

client = DenodoDataFrameClient("database_name")
vqlquery = VqlQuery(Path("examples/template.sql"))
df = client.query(vqlquery).to_dataframe()
```

## Using pyodbc cursor without pandas

```python
from denodoclient import DenodoClient
from denodoclient import VqlQuery
from pathlib import Path
client = DenodoClient("database_name")
vqlquery = VqlQuery(Path("examples/template.sql"))
cursor = client.query(vqlquery).cursor
# Do whatever you want with the pyodbc cursor
```

## Changing the default connection string

Default server is `denodo` and default ODBC driver name is `DenodoODBC Unicode(x64)`. You can change
this by passing parameters in as follows.

```python
from denodoclient import DenodoClient
from denodoclient import VqlQuery
from pathlib import Path
client = DenodoClient("database_name", DRIVER="my_denodo_driver", SERVER="denodo-uat")
```

For a list of options, have a look at `DenodoClient.OPTIONS`.

```python
print(DenodoClient.OPTIONS)
```

## Dynamically change query parameters

You can just set parameters on the query object, or in the constructor.

```
SELECT * FROM table WHERE name = "{foo}";
```

```python
from denodoclient import VqlQuery
from pathlib import Path
vqlquery = VqlQuery(Path("examples/template.sql"), foo="John")
vqlquery.foo = "Mark"

# You can set any variable you want
vqlquery.baz = "Foobaz!"

# See a list of the currently set variables
print(vqlquery.tokens)

# See the string representation of the query
print(str(vqlquery))
```

# Caveats

Please be aware that the templating functionality in this package is vulnerable to SQL-injection
attacks. Use with caution.

# Credits

This package was created at [DFDS](https://www.dfds.com/).

## Contributors

[Martin Morset](https://github.com/dingobar/)

# Contributing

Contributions are welcome, and they are greatly appreciated! Every little bit helps, and credit will
always be given.

If you find bugs or have a feature request, please
[file an issue](https://github.com/dfds-data/denodoclient/issues).

If you are reporting a bug, please include:

- Your operating system name and version.
- Any details about your local setup that might be helpful in troubleshooting.
- Detailed steps to reproduce the bug.
