import logging
import json
from typing import Any, Dict, Optional
import httpx

_logger = logging.getLogger(__name__)


class HttpxHandle:
    def __init__(self, base_url: str, timeout: float = 5.0) -> None:
        self.base_url = base_url
        self.timeout = timeout
        self.session = httpx.Client(base_url=self.base_url, timeout=self.timeout)

    def request(
        self,
        method: str,
        url: str,
        params: Optional[Dict[str, Any]] = None,
        data: Optional[Dict[str, Any]] = None,
        json_data: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Optional[Dict[str, Any]]:
        """
        通用请求方法，支持 GET、POST 等方法。

        参数:
            method (str): 请求方法���如 'GET'、'POST' 等。
            url (str): 请求的 URL（相对地址）。
            params (dict): 查询参数。
            data (dict): 表单数据。
            json_data (dict): JSON 数据。
            headers (dict): 请求头。

        返回:
            Optional[Dict[str, Any]]: 响应的 JSON 数据，失败返回 None。
        """
        try:
            response = self.session.request(
                method=method,
                url=url,
                params=params,
                data=data,
                json=json_data,
                headers=headers,
            )
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as e:
            _logger.error(f"请求失败，状态码：{e.response.status_code}，错误信息：{e}")
        except httpx.RequestError as e:
            _logger.error(f"请求错误：{e}")
        except json.JSONDecodeError as e:
            _logger.error(f"JSON 解码错误：{e}")
        return None

    def close(self) -> None:
        """
        关闭 HTTP 会话。
        """
        self.session.close()


# http_client = HttpxHandle(base_url="https://example.com/api", timeout=10.0)

# # 发送 GET 请求
# response = http_client.request("GET", "/endpoint", params={"key": "value"})

# # 发送 POST 请求
# response = http_client.request(
#     "POST",
#     "/endpoint",
#     json_data={"key": "value"},
#     headers={"Authorization": "Bearer token"},
# )

# # 处理响应
# if response is not None:
#     # 处理成功的响应数据
#     pass
# else:
#     # 处理错误情况
#     pass

# # 关闭会话
# http_client.close()