import logging
from typing import Optional, Dict, Any, Union
from functools import wraps

from wechat_robot.utils.httpx_handle import HttpxHandle
from wechat_robot.utils.config_utils import get_config

logger = logging.getLogger(__name__)


def api_call(func):
    """API 调用装饰器"""

    @wraps(func)
    def wrapper(self, *args, **kwargs):
        try:
            result = func(self, *args, **kwargs)
            return self._validate_response(result)
        except Exception as e:
            logger.error(f"API call failed: {func.__name__}, error: {str(e)}")
            raise

    return wrapper


class WeChatAPI:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            port = get_config("wechat", "port")
            cls._instance = super().__new__(cls)
            cls._instance.client = HttpxHandle(
                base_url=f"http://127.0.0.1:{port}", timeout=2
            )
        return cls._instance

    def __del__(self):
        if hasattr(self, "client"):
            self.client.close()

    def _validate_response(self, response: Dict[str, Any]) -> Dict[str, Any]:
        if not isinstance(response, dict):
            raise ValueError(f"Invalid response format: {response}")
        # if response.get('code') != 0:
        #     raise ValueError(f"API error: {response.get('message', 'Unknown error')}")
        return response

    @api_call
    def pull_wechat_list(self, pull_type: int = 1) -> Dict[str, Any]:
        """拉取微信列表"""
        return self.client.request(
            "POST", "/api", json_data={"type": 5, "pull_type": pull_type}
        )

    @api_call
    def check_wechat_login_status(self) -> Dict[str, Any]:
        """检查微信登录状态"""
        return self.client.request("POST", "/api", json_data={"type": 1})

    @api_call
    def get_user_info(self) -> Dict[str, Any]:
        """获取用户信息"""
        return self.client.request("POST", "/api", json_data={"type": 3})

    @api_call
    def pull_wechat_list_members(self, chat_room_id: str) -> Dict[str, Any]:
        """拉取群成员列表"""
        return self.client.request(
            "POST", "/api", json_data={"type": 6, "chat_room_id": chat_room_id}
        )

    @api_call
    def send_wechat_msg(self, wx_id: str, msg: str) -> Dict[str, Any]:
        """发送微信消息"""
        return self.client.request(
            "POST", "/api", json_data={"type": 7, "wx_id": wx_id, "msg": msg}
        )

    @api_call
    def search_wxid_info(self, wx_id: str) -> Dict[str, Any]:
        """搜索微信用户信息"""
        return self.client.request(
            "POST", "/api", json_data={"type": 19, "wx_id": wx_id}
        )

    @api_call
    def api_agree_friend_application(self, wx_id: str, v3: str, v4: str) -> Dict[str, Any]:
        """发送微信消息"""
        return self.client.request(
            "POST",
            "/api",
            json_data={
                "type": 17,
                "wx_id": wx_id,
                "v3": v3,
                "v4": v4,
            },
        )


# 创建全局实例
wechat_api = WeChatAPI()

# 为了向后兼容，保留原有的函数调用方式
# pull_wechat_list = wechat_api.pull_wechat_list
# pull_wechat_list_members = wechat_api.pull_wechat_list_members
# send_wechat_msg = wechat_api.send_wechat_msg
# search_wxid_info = wechat_api.search_wxid_info
