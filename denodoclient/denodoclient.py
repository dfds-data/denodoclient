import pyodbc
from socket import gethostname
from sys import version
from os import getenv

from denodoclient.vqlquery import VqlQuery


__options = {
    "DRIVER": "{DenodoODBC Unicode(x64)}",
    "SERVER": "denodo",
    "PORT": 9996,
    "SSLmode": "require",
    "service": "",
    "UserAgent": f"{gethostname()}-{version}",
    "ReadOnly": 1,
    "Protocol": "7.4-1",
    "FakeOidIndex": 0,
    "ShowOidColumn": 0,
    "RowVersioning": 0,
    "ShowSystemTables": 0,
    "ConnSettings": r"set+i18n+to+us%5fpst%3b",
    "Fetch": 100,
    "Socket": 4096,
    "UnknownSizes": 0,
    "MaxVarcharSize": 255,
    "MaxLongVarcharSize": 8190,
    "Debug": 0,
    "CommLog": 0,
    "Optimizer": 0,
    "Ksqo": 0,
    "UseDeclareFetch": 1,
    "TextAsLongVarchar": 1,
    "UnknownsAsLongVarchar": 0,
    "BoolsAsChar": 0,
    "Parse": 0,
    "CancelAsFreeStmt": 0,
    "ExtraSysTablePrefixes": "dd_",
    "LFConversion": 1,
    "UpdatableCursors": 0,
    "DisallowPremature": 0,
    "TrueIsMinus1": 0,
    "BI": 0,
    "ByteaAsLongVarBinary": 0,
    "UseServerSidePrepare": 0,
    "LowerCaseIdentifier": 0,
    "PreferLibpq": 1,
    "GssAuthUseGSS": 0,
    "XaOpt": 3,
    "krbsrvname": "HTTP",
}


def __set_connection_string_options(options) -> None:
    (__options.update({k: v} for k, v in options.items()))


def __create_connection_string() -> str:
    """Returns a string of the form KEY1=value1;KEY2=value2"""
    return [f"{k}={v};" for k, v in __options.items()].join().strip(";")


class DenodoClient:
    def __init__(self, database: str, **options) -> None:
        if (not isinstance(database, str)) or len(database) < 1:
            raise ValueError(f"Invalid database name {database}")

        if (uid := getenv("DENODO_UID")) is not None:
            __options.update({"UID": uid})
        else:
            raise ValueError(f"Environmental variable DENODO_UID must be set")

        if (pwd := getenv("DENODO_PWD")) is not None:
            __options.update({"PWD": pwd})
        else:
            raise ValueError(f"Environmental variable DENODO_UID must be set")

        __set_connection_string_options(options)

        connection = pyodbc.connect(__create_connection_string(__options))
        self._cursor = connection.cursor()

    def query(self, query: VqlQuery):
        self._cursor.execute(str(query))
        return self

    @property
    def cursor(self):
        return self._cursor
