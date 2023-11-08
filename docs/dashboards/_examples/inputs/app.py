# This file generated by Quarto; do not edit by hand.

from __future__ import annotations

from pathlib import Path
from shiny import App, Inputs, Outputs, Session, ui




def server(input: Inputs, output: Outputs, session: Session) -> None:
    import seaborn as sns
    penguins = sns.load_dataset("penguins")

    # ========================================================================

    from shiny import render, ui
    ui.input_select("x", "Variable:",
                    choices=["bill_length_mm", "bill_depth_mm"])
    ui.input_select("dist", "Distribution:", choices=["hist", "kde"])
    ui.input_checkbox("rug", "Show rug marks", value = False)

    # ========================================================================

    @render.plot
    def displot():
        sns.displot(
            data=penguins, hue="species", multiple="stack",
            x=input.x(), rug=input.rug(), kind=input.dist())

    # ========================================================================




_static_assets = ["input-panel_files"]
_static_assets = {"/" + sa: Path(__file__).parent / sa for sa in _static_assets}

app = App(
    Path(__file__).parent / "input-panel.html",
    server,
    static_assets=_static_assets,
)
