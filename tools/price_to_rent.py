from collections.abc import Generator
from typing import Any

from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

from tools.get_data import priceToRent


class PriceToRentTool(Tool):
    def _invoke(self, tool_parameters: dict[str, Any]) -> Generator[ToolInvokeMessage]:
        b_excel = priceToRent(
            token=self.runtime.credentials['token'],
            plazaId=tool_parameters['plazaId'],
            startDate=tool_parameters['startDate'],
            endDate=tool_parameters['endDate']
        )
        if b_excel != b"":
            yield self.create_blob_message(
                blob=b_excel,
                meta={
                    "mime_type": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                }
            )
        else:
            yield self.create_text_message("获取失败")
