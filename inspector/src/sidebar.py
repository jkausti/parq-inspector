from textual.app import ComposeResult
from textual.widgets import (
    Input,
    RadioButton,
    RadioSet,
    Label,
    Button,
)
from textual.containers import Container, Horizontal, Vertical
from pathlib import Path


class StoragePickerGroup(Container):
    def __init__(self):
        super().__init__()

    def compose(self) -> ComposeResult:
        with Vertical():
            yield Label("Storage type", classes="storage-type-title")
            with RadioSet(id="storagetype_set"):
                yield RadioButton("Local")
                yield RadioButton("Azure")
                yield RadioButton("AWS")
                yield RadioButton("GCP")


class RowLimitSetter(Container):
    def __init__(self, row_limit: int = 200):
        self.row_limit = row_limit
        super().__init__()

    def compose(self) -> ComposeResult:
        yield Label("Row limit", classes="row_limit_label")
        yield Input(
            placeholder="Input a number",
            id="row_limit_input",
            value=str(self.row_limit),
        )


class PathSetter(Container):
    def __init__(self, placeholder: str = ""):
        self.placeholder = placeholder if placeholder != "." else None
        super().__init__()

    def compose(self) -> ComposeResult:
        yield Label("Path", classes="path_label")
        yield Input(id="path_input", value=self.placeholder)


class FileTypeSetter(Container):
    def __init__(self):
        super().__init__()

    def compose(self) -> ComposeResult:
        yield Label("Filetype", classes="filetype-title")
        with RadioSet(id="filetype_set"):
            yield RadioButton("Parquet")
            yield RadioButton("Delta table")


class Sidebar(Container):
    def __init__(self, filepath: Path, row_limit: int):
        self.path_placeholder = str(filepath) if str(filepath) != "." else ""
        self.row_limit = row_limit if row_limit else 200
        super().__init__()

    def compose(self) -> ComposeResult:
        with Vertical():
            yield Label("Settings", classes="sidebar-title")
            with Horizontal(id="upper_row"):
                yield StoragePickerGroup()
                yield RowLimitSetter(self.row_limit)
                yield PathSetter(str(self.path_placeholder))
            with Horizontal(id="lower_row"):
                yield Button("Show data", id="submit_button", variant="primary")
                yield FileTypeSetter()
            # id="button_cont",
