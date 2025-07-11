from __future__ import annotations

from dataclasses import KW_ONLY, field
import typing as t

import rio

from .. import components as comps


@rio.page(
    name="Sample Page",
    url_segment="",
)
class SamplePage(rio.Component):
    """
    This is an example Page. Pages are identical to other Components and only
    differ in how they're used.
    """

    def build(self) -> rio.Component:
        return rio.Column(
            rio.Text("Fast Food Spending Tracker", style="heading1"),
            rio.Icon(
                "material/restaurant",
                min_width=2.5,
                min_height=2.5,
            ),
            rio.Text("Replacing Stuff with my own content"),
            spacing=2,
            margin=2,
            align_x=0.5,
            align_y=0,
        )
