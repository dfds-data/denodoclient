from typing import Iterable
from denodoclient.denodoclient import DenodoClient
import pandas as pd


class DenodoDataFrameClient(DenodoClient):
    def __init__(self, database: str, **options) -> None:
        super(DenodoDataFrameClient, self).__init__(database=database, **options)

    def to_dataframe(self, chunksize: int = None):
        if not chunksize:
            return self._all_rows_to_dataframe()
        else:
            return self._chunkwise_rows_to_dataframe(chunksize)

    def _all_rows_to_dataframe(self) -> pd.DataFrame:
        return pd.DataFrame((tuple(t) for t in self._cursor.fetchall()))

    def _chunkwise_rows_to_dataframe(self, chunksize) -> Iterable[pd.DataFrame]:
        rows = self._cursor.fetchmany(chunksize)
        while rows:
            yield pd.DataFrame(tuple(t) for t in rows)
            rows = self._cursor.fetchmany(chunksize)
