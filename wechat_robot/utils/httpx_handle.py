import logging
from typing import Any, Dict, Optional
import httpx
from tenacity import retry, stop_after_attempt, wait_exponential

_logger = logging.getLogger(__name__)

class HttpxHandle:
    def __init__(self, base_url: str, timeout: float = 5.0, max_retries: int = 3) -> None:
        self.base_url = base_url
        self.timeout = timeout
        self.max_retries = max_retries
        self.session = httpx.Client(base_url=self.base_url, timeout=self.timeout)

    @retry(
        stop=stop_after_attempt(3),  # 最多重试3次
        wait=wait_exponential(multiplier=1, min=4, max=10)  # 指数退避重试
    )
    def request(
        self,
        method: str,
        url: str,
        params: Optional[Dict[str, Any]] = None,
        data: Optional[Dict[str, Any]] = None,
        json_data: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
    ) -> Dict[str, Any]:
        try:
            response = self.session.request(
                method=method,
                url=url,
                params=params,
                data=data,
                json=json_data,
                headers=headers,
            )
            
            # 检查响应状态码
            if response.status_code >= 500:
                _logger.error(f"服务器错误: {response.status_code} - {response.text}")
                raise httpx.HTTPError(f"服务器错误: {response.status_code}")
            
            if response.status_code >= 400:
                _logger.error(f"客户端错误: {response.status_code} - {response.text}")
                raise httpx.HTTPError(f"客户端错误: {response.status_code}")
            
            return response.json()
            
        except httpx.TimeoutException as e:
            _logger.error(f"请求超时: {e}")
            raise
            
        except httpx.HTTPError as e:
            _logger.error(f"HTTP请求错误: {e}")
            raise
            
        except Exception as e:
            _logger.error(f"未知错误: {e}")
            raise
            
    def close(self):
        """关闭会话"""
        if self.session:
            self.session.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
        
# 使用示例
# try:
#     http_client = HttpxHandle(base_url="http://127.0.0.1:30001")
#     response = http_client.request("GET", "/api")
#     print(response)
# except Exception as e:
#     print(f"请求失败: {e}")
# finally:
#     http_client.close()