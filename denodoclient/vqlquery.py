from pathlib import Path
import re
from typing import Any, Dict


class VqlQuery:
    def __init__(self, path: Path, **kwargs) -> None:
        with open(path, "r") as query_file:
            self.__query_template = query_file.read()

        for k, v in kwargs.items():
            setattr(self, k, v)

    @property
    def tokens(self) -> Dict[str, Any]:
        return {k: v for k, v in self.__dict__.items() if k[0] != "_"}

    @tokens.setter
    def tokens(self, var):
        raise AttributeError(
            (
                f"Cannot change tokens in this way. Use {self.__class__.__name__}(path).foo = 'bar'"
                " or pass tokens as keyword arguments to the constructor"
            )
        )

    def __str__(self) -> str:
        to_replace = re.findall(r"{(\w+)}", self.__query_template)

        for t in to_replace:
            if not t in self.tokens:
                raise ValueError(
                    f"No value for token '{t}' - cannot convert template to query string!"
                )

        return self.__query_template.format_map(self.tokens)
