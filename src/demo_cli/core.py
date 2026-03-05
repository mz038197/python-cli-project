"""demo-cli 核心業務邏輯層"""

from typing import List


def greet(name: str = "World") -> str:
    """問候使用者
    
    Args:
        name: 要問候的人名，預設為 "World"
        
    Returns:
        問候訊息
    """
    return f"你好，{name}！歡迎使用 demo-cli 工具！"


def add_numbers(nums: List[float]) -> float:
    """將數字相加
    
    Args:
        nums: 要相加的數字列表
        
    Returns:
        相加後的結果
    """
    return sum(nums)

