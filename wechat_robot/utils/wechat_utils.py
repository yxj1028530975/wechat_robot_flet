import winreg
import logging
import psutil
from typing import Optional
import subprocess
from wechat_robot.utils.config_utils import get_inject_tool_dir,get_config

# 配置日志记录器
logger = logging.getLogger(__name__)

def get_wechat_install_path() -> Optional[str]:
    """
    获取微信的安装路径。

    返回:
        微信安装路径字符串，如果获取失败则返回 None。
    """
    registry_path = r"Software\Tencent\WeChat"
    value_name = "InstallPath"

    try:
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, registry_path, 0, winreg.KEY_READ) as key:
            wechat_path, _ = winreg.QueryValueEx(key, value_name)
            if wechat_path:
                logger.info(f"找到微信安装路径: {wechat_path}")
                return wechat_path
            else:
                logger.warning(f"注册表值 '{value_name}' 为空。")
                return None
    except Exception as e:
        logger.error(f"获取微信安装路径失败：{e}")
    return None

def get_current_wechat_version() -> Optional[str]:
    """
    获取微信的版本号。
    
    返回:
        微信版本号字符串，如果获取失败则返回 None。
    """
    try:
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Tencent\WeChat", 0, winreg.KEY_READ) as key:
            return _extracted_from_get_wx_version_(key)
    except Exception as e:
        print(f"打开注册表失败：{e}")
        return None
    

def _extracted_from_get_wx_version_(key):
    int_version = winreg.QueryValueEx(key, "Version")[0]
    hex_version = hex(int_version)
    hex_str = hex_version[2:]
    new_hex_str = f"0{hex_str[1:]}"
    new_hex_num = int(new_hex_str, 16)
    major = (new_hex_num >> 24) & 0xFF
    minor = (new_hex_num >> 16) & 0xFF
    patch = (new_hex_num >> 8) & 0xFF
    build = (new_hex_num >> 0) & 0xFF
    return f"{major}.{minor}.{patch}.{build}"

# 检测网络端口有没有被占用
def check_port_in_use(port: int) -> bool:
    """
    检查指定端口是否被占用。

    参数:
        port (int): 端口号。

    返回:
        bool: 如果端口被占用则返回 True，否则返回 False。
    """
    try:
        return any(
            conn.laddr.port == port
            for conn in psutil.net_connections(kind='inet')
        )
    except Exception as e:
        logger.error(f"检查端口 {port} 时发生错误: {e}")
        return False

#从30001-30100中找到一个没有被占用的端口
def get_available_port() -> Optional[int]:
    """
    获取一个未被占用的端口号。

    返回:
        Optional[int]: 可用的端口号，如果没有找到则返回 None。
    """
    return next((port for port in range(30001, 30100) if not check_port_in_use(port)), None)

# 拼接启动微信命令
def start_wechat_command(port:str) -> Optional[str]:
    """
    拼接启动微信命令。

    返回:
        Optional[str]: 启动命令字符串，如果未找到可用端口则返回 None。
    """

    # TODO 专业版
    # key = get_config("wechat", "key")
    # print(f"key: {key}")
    # if key is None:
    #     logger.error("获取配置项 'wechat' 中的 'key' 失败。")
    #     return None
    
    exe_path = get_inject_tool_dir()
    print(f"exe_path: {exe_path}")
    if exe_path is None:
        logger.error("获取 inject_tool.exe 路径失败。")
        return None
    
    # return f"{exe_path} start {port} --key={key}"
    return f"{exe_path} start {port}"

# 获取微信hook启动命令
def start_wechat() -> Optional[str]:
    """
    获取微信 hook 启动命令。

    返回:
        str: 微信 hook 启动命令。
    """
    port = get_available_port()
    wechat_command = start_wechat_command(str(port))
    print(f"启动命令: {wechat_command}")
    if wechat_command:
        # 将命令字符串拆分为列表
        cmd_list = wechat_command.split()
        try:
            subprocess.Popen(
                cmd_list,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )
            return str(port)
        except Exception as e:
            logger.error(f"启动微信时发生错误: {e}")
    return None

if __name__ == '__main__':
    ...