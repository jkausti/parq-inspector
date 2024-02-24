from numpy import source
from textual.events import InputEvent
from textual.widgets import DataTable
import polars as pl
from pathlib import Path
from inspector.src.storage_options import get_storage_options
from typing import Tuple


class ParqTable(DataTable):
    def set_data(self, data: tuple) -> None:
        self.clear(columns=True)
        self.add_columns(*data[0])
        self.add_rows(data[1])

    def get_and_set_data(self, input_args: dict) -> None:
        if input_args["storage"].lower() == "local":
            path = Path(input_args["path"]).resolve()

            if input_args["filetype"] == "Delta table":
                lf = pl.read_delta(source=str(path)).lazy()
            elif input_args["filetype"] == "Parquet":
                try:
                    lf = pl.scan_parquet(str(path))
                except Exception as e:
                    raise e

            else:
                raise Exception("Wrong filetype value in input_args")
                # TODO handle exception and show error on screen

        elif input_args["storage"].lower() in ["azure", "gcp", "aws"]:
            storage_options = get_storage_options(str(input_args["storage"]).lower())

            if input_args["filetype"] == "Delta table":
                try:
                    lf = pl.read_delta(
                        source=str(input_args["path"]),
                        storage_options=storage_options,
                    ).lazy()
                except Exception as e:
                    raise e
            elif input_args["filetype"] == "Parquet":
                try:
                    lf = pl.scan_parquet(
                        str(input_args["path"]),
                        storage_options=storage_options,
                    )
                except Exception as e:
                    raise e
                    # TODO handle exception
            else:
                raise Exception("Wrong filetype value in input_args")
        else:
            raise NotImplementedError

        columns = [col for col, _ in lf.schema.items()]
        rows = lf.select(pl.all()).limit(input_args["row_limit"]).collect().rows()

        self.set_data((columns, rows))
