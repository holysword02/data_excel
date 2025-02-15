from typing import Any

import requests
from dify_plugin import ToolProvider
from dify_plugin.errors.tool import ToolProviderCredentialValidationError

from tools.get_data import get_headers


class DataExcelProvider(ToolProvider):
    def _validate_credentials(self, credentials: dict[str, Any]) -> None:
        url = "http://jyfx.wandacm.cn/onemap-wanda/api/basic/square"
        # "573e5c90b0564c2a6d93c391e95f6dd3"
        try:
            response = requests.get(url, headers=get_headers(credentials.get("token")))
            # if response.json()['msg'] != "success":
            #     raise ToolProviderCredentialValidationError("token is invalid")
        except Exception as e:
            # raise ToolProviderCredentialValidationError("token is invalid")
            pass
