from wechat_robot.utils.httpx_handle import HttpxHandle
from wechat_robot.utils.config_utils import get_config

port = get_config("wechat","port")
http_client = HttpxHandle(base_url=f"http://127.0.0.1:{port}", timeout=1)


def pull_wechat_list(pull_type: int = 1) -> dict:
    """
    拉取微信列表
    :param pull_type: 拉取类型，1:群列表 2:好友列表 3:公众号列表 4:其它列表
    :return: 指定列表
    """
    return http_client.request(
        "POST", "/api", json_data={"type": 5, "pull_type": pull_type}
    )

def pull_wechat_list_members(chat_room_id: str) -> dict:
    """
    拉取微信列表
    :param pull_type: 拉取类型，1:群列表 2:好友列表 3:公众号列表 4:其它列表
    :return: 指定列表
    """
    return http_client.request(
        "POST", "/api", json_data={"type": 6, "chat_room_id": chat_room_id}
    )

def send_wechat_msg(wx_id:str,msg:str):
    """
    发送微信消息
    :param wx_id: 微信id
    :param msg: 消息内容
    :return:
    """
    return http_client.request(
        "POST", "/api", json_data={"type": 7, "wx_id": wx_id, "msg": msg}
    )