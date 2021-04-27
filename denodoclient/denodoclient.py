import pyodbc
from socket import gethostname
from sys import version
from os import getenv

from denodoclient.vqlquery import VqlQuery


# TODO: How to test this??
class DenodoClient:
    OPTIONS = {
        "DRIVER": "{DenodoODBC Unicode(x64)}",
        "UID": None,
        "PWD": None,
        "SERVER": "denodo",
        "DATABASE": "ddp",
        "PORT": "9996",
        "SSLmode": "prefer",
        "service": "",
        "krbsrvname": "HTTP",
        "UserAgent": f"{gethostname()}-{version}",
        "ReadOnly": "0",
        "Protocol": "7.4-1",
        "FakeOidIndex": "0",
        "ShowOidColumn": "0",
        "RowVersioning": "0",
        "ShowSystemTables": "0",
        "ConnSettings": "set+i18n+to+us%5fpst%3b",
        "Fetch": "100",
        "Socket": "4096",
        "UnknownSizes": "0",
        "MaxVarcharSize": "255",
        "MaxLongVarcharSize": "8190",
        "Debug": "0",
        "CommLog": "0",
        "Optimizer": "0",
        "Ksqo": "0",
        "UseDeclareFetch": "1",
        "TextAsLongVarchar": "1",
        "UnknownsAsLongVarchar": "0",
        "BoolsAsChar": "0",
        "Parse": "0",
        "CancelAsFreeStmt": "0",
        "ExtraSysTablePrefixes": "dd_",
        "LFConversion": "1",
        "UpdatableCursors": "0",
        "DisallowPremature": "0",
        "TrueIsMinus1": "0",
        "BI": "0",
        "ByteaAsLongVarBinary": "0",
        "UseServerSidePrepare": "0",
        "LowerCaseIdentifier": "0",
        "PreferLibpq": "1",
        "GssAuthUseGSS": "0",
        "XaOpt": "3",
    }

    def __init__(self, database: str, **options) -> None:
        if (isinstance(database, str)) and len(database) > 1:
            self.OPTIONS.update({"DATABASE": database})
        else:
            raise ValueError(f"Invalid database name {database}")

        if (uid := getenv("DENODO_UID")) is not None:
            self.OPTIONS.update({"UID": uid})
        else:
            raise ValueError(f"Environmental variable DENODO_UID must be set")

        if (pwd := getenv("DENODO_PWD")) is not None:
            self.OPTIONS.update({"PWD": pwd})
        else:
            raise ValueError(f"Environmental variable DENODO_UID must be set")

        self.__set_connection_string_options(options)

        connection = pyodbc.connect(self.__create_connection_string())
        self._cursor = connection.cursor()

    def __set_connection_string_options(self, options) -> None:
        (self.OPTIONS.update({k: v} for k, v in options.items()))

    def __create_connection_string(self) -> str:
        """Returns a string of the form KEY1=value1;KEY2=value2"""
        return "".join([f"{k}={v};" for k, v in self.OPTIONS.items()]).strip(";")

    def query(self, query: VqlQuery):
        self._cursor.execute(str(query))
        return self

    @property
    def cursor(self):
        return self._cursor

    @property
    def columns(self):
        return [description[0] for description in self._cursor.description]
