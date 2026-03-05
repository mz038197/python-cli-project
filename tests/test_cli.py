"""demo-cli 命令行介面測試"""

from typer.testing import CliRunner
from demo_cli.cli import app, main

runner = CliRunner()


class TestCommands:
    """命令執行測試"""
    
    def test_hello_command(self):
        """測試 hello 命令執行"""
        result = runner.invoke(app, ["hello"])
        assert result.exit_code == 0
        assert "你好，World" in result.stdout
    
    def test_hello_with_name(self):
        """測試 hello 命令帶名字"""
        result = runner.invoke(app, ["hello", "Alice"])
        assert result.exit_code == 0
        assert "你好，Alice" in result.stdout
    
    def test_add_command(self):
        """測試 add 命令執行"""
        result = runner.invoke(app, ["add", "1", "2", "3"])
        assert result.exit_code == 0
        assert "結果：6" in result.stdout
    
    def test_help_command(self):
        """測試 help 命令"""
        result = runner.invoke(app, ["--help"])
        assert result.exit_code == 0
        assert "demo-cli" in result.stdout or "Usage" in result.stdout


