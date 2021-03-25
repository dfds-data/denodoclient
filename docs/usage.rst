=====
Usage
=====

To use Denodo Client in a project::

    from pathlib import Path
    from denodoclient.dataframes import DenodoDataFrameClient
    from denodoclient import VqlQuery


    if __name__ == "__main__":
        client = DenodoDataFrameClient("ddp")

        vqlquery = VqlQuery(Path("examples/template.sql"))

        # Using dataframes requires pandas installed
        df = client.query(vqlquery).to_dataframe()

        print(f"got {df.shape[0]} records!")
    