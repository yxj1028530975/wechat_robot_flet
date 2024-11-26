import ctypes


user32 = ctypes.windll.user32
screen_width = user32.GetSystemMetrics(0)
screen_height = user32.GetSystemMetrics(1)

# 返回windows属性
def get_windows_info():
    return {
        "screen_width": screen_width,
        "screen_height": screen_height,
    }