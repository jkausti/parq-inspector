import rich_click as click
from textual.app import ComposeResult, App
from textual.widgets import DataTable, Header, Footer, Button, RadioSet, Input
from textual.containers import Vertical
from textual.binding import Binding
from inspector.src.sidebar import Sidebar
from inspector.src.parq_table import ParqTable
from textual import on
from pathlib import Path


@click.command
@click.option("-f", "--filepath", "filepath", default="", required=False)
@click.option("-rl", "--row_limit", "row_limit", default=200, required=False)
def inspector(filepath: str, row_limit: int):
    """Welcome to the data inspector tool."""

    table_app = TableApp(filepath, row_limit)
    table_app.run()


class TableApp(App):
    CSS_PATH = "./styles/basic.tcss"

    BINDINGS = [
        Binding(
            key="q",
            action="quit",
            description="Quit the app",
        ),
        Binding(
            key="s",
            action="toggle_sidebar",
            description="Show/Hide settings",
        ),
    ]

    def __init__(self, filepath: str = "", row_limit: int = 200):
        """
        Constructor handles potential input from commandline for
        filepath and row_limit
        """
        self.row_limit = row_limit if row_limit else 200
        self.path = Path(filepath)
        self.sidebar = Sidebar(self.path, self.row_limit)
        self.data_table = ParqTable()

        super().__init__()

    def compose(self) -> ComposeResult:
        with Vertical():
            yield Header()

            # if input for filepath received from command line
            if str(self.path) != ".":
                input_data = {
                    "storage": "local",
                    "path": self.path,
                    "row_limit": self.row_limit,
                }
                self.data_table.get_and_set_data(input_data)
                yield self.data_table
            else:
                yield self.data_table
            yield self.sidebar
            yield Footer()

    def action_toggle_sidebar(self) -> None:
        """Toggels sidebar"""
        sidebar = self.query_one(Sidebar)
        self.set_focus(None)
        if sidebar.has_class("-hidden"):
            sidebar.remove_class("-hidden")

        else:
            if sidebar.query("*:focus"):
                self.screen.set_focus(None)
            sidebar.add_class("-hidden")

    @on(Button.Pressed)
    def show_data(self) -> None:
        # get values from ui
        radio_set = self.query_one("#storagetype_set")
        if not isinstance(radio_set, RadioSet):
            raise Exception("Could not get radioset from ui")
        if radio_set.pressed_button:
            storage_value = radio_set.pressed_button.label
        else:
            raise Exception("No value set for storage")
            # TODO: show messag on screen indicating no value set for radioset
        row_limit_input = self.query_one("#row_limit_input")
        if isinstance(row_limit_input, Input):
            row_limit = int(row_limit_input.value)
        else:
            row_limit = 200

        path_input = self.query_one("#path_input")
        if isinstance(path_input, Input):
            path = path_input.value
            self.sub_title = str(self.path)
        else:
            raise Exception("No path set")

        file_type = self.query_one("#filetype_set")
        if not isinstance(file_type, RadioSet):
            raise Exception("Could not get filetype from ui.")
        if file_type.pressed_button:
            filetype_value = file_type.pressed_button.label
        else:
            raise Exception("No value set for filetype")

        input_args = {
            "storage": str(storage_value),
            "row_limit": row_limit,
            "path": path,
            "filetype": str(filetype_value),
        }
        print(f"INPUT_ARGS: {input_args}")

        self.data_table.get_and_set_data(input_args)

    def on_mount(self):
        self.title = "Inspector"
