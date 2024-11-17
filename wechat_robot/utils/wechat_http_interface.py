from wechat_robot.utils.httpx_handle import HttpxHandle
from wechat_robot.utils.config_utils import get_config

port = get_config("wechat","port")
http_client = HttpxHandle(base_url=f"http://127.0.0.1:{port}", timeout=5)


def pull_wechat_list(pull_type: int = 1) -> dict:
    """
    拉取微信列表
    :param pull_type: 拉取类型，1:群列表 2:好友列表 3:公众号列表 4:其它列表
    :return: 指定列表
    """
    response = http_client.request(
        "POST", "/api", json_data={"type": 5, "pull_type": pull_type}
    )
    return response

def pull_wechat_list_members(chat_room_id: str) -> dict:
    """
    拉取微信列表
    :param pull_type: 拉取类型，1:群列表 2:好友列表 3:公众号列表 4:其它列表
    :return: 指定列表
    """
    response = http_client.request(
        "POST", "/api", json_data={"type": 6, "chat_room_id": chat_room_id}
    )
    return response
