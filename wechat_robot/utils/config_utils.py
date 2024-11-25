import os
from configparser import ConfigParser
import tomli
import logging
from typing import Optional

# 配置日志记录器
logger = logging.getLogger(__name__)

# 动态计算配置文件路径
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, '..', '..')) 
config_file = os.path.join(current_dir, '../../config/config.toml')
with open(config_file, mode="rb") as fp:
    read_files = tomli.load(fp)

# 获取当前目录
def get_current_dir() -> str:
    """
    获取当前目录。

    返回:
        str: 当前目录的绝对路径。
    """
    return current_dir

# current_dir + '\\assets\\dll\\inject_tool.exe' 拼接
def get_inject_tool_dir() -> str:
    """
    获取 assets\\dll\\inject_tool 目录。

    返回:
        str: assets\\dll\\inject_tool.exe 目录的绝对路径。
    """
    # 获取脚本执行的根路径
    return os.path.join(project_root, 'assets', 'dll', 'start_wechat.exe')

# 获取配置文件中的配置
def get_config(section: str = 'wechat',option: str = 'version') -> Optional[str]:
    """
    获取配置文件中的配置项。

    参数:
        section (str): 配置部分名称，默认值为 'wechat'。
        option (str): 配置项名称,，默认值为 'version'。
        

    返回:
        Optional[str]: 配置项的值，如果获取失败则返回 None。
    """
    try:
        return read_files[section][option]
    except Exception as e:
        logger.error(f"读取配置文件时发生错误: {e}")
    return None

# 设置配置文件中的配置
# def set_config(section: str = 'wechat',option: str = 'version',value: str = '3.9.11.19') -> Optional[str]:
    # """
    # 设置配置文件中的配置项。

    # 参数:
    #     section (str): 配置部分名称，默认值为 'wechat'。
    #     option (str): 配置项名称,，默认值为 'version'。
    #     value (str): 配置项的值，默认值为 '3.9.11.19'。
    # """
    # try:
    #     config.set(section, option, value)
    #     with open(config_file, 'w', encoding='utf-8') as f:
    #         config.write(f)
    # except Exception as e:
    #     logger.error(f"写入配置文件时发生错误: {e}")
        

if __name__ == '__main__':
    print(current_dir)
    print(get_config('wechat','version'))
    print(get_config('wechat_robot','name'))
    print(get_inject_tool_dir())