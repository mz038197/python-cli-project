"""demo-cli 核心業務邏輯測試"""

import pytest
from demo_cli import core


class TestGreet:
    """問候函數測試"""
    
    def test_greet_default(self):
        """測試預設問候"""
        result = core.greet()
        assert result == "你好，World！歡迎使用 demo-cli 工具！"
    
    def test_greet_with_name(self):
        """測試帶名字的問候"""
        result = core.greet("Alice")
        assert result == "你好，Alice！歡迎使用 demo-cli 工具！"


class TestAddNumbers:
    """加法函數測試"""
    
    def test_add_two_numbers(self):
        """測試兩個數字相加"""
        assert core.add_numbers([1, 2]) == 3
    
    def test_add_multiple_numbers(self):
        """測試多個數字相加"""
        assert core.add_numbers([1, 2, 3, 4, 5]) == 15
    
    def test_add_empty_list(self):
        """測試空列表"""
        assert core.add_numbers([]) == 0

