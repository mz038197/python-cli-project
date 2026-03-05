"""demo-cli 命令行介面層"""

from typing import List, Optional
import typer

from . import core

app = typer.Typer(
    name="demo-cli",
    help="簡單的 Python CLI 工具示範",
)


@app.command()
def hello(
    name: str = typer.Argument("World", help="要問候的人名"),
) -> None:
    """問候使用者"""
    result = core.greet(name)
    typer.echo(result)


@app.command()
def add(
    numbers: List[float] = typer.Argument(..., help="要相加的數字"),
) -> None:
    """將數字相加"""
    result = core.add_numbers(numbers)
    typer.echo(f"結果：{result}")


def main(args: Optional[List[str]] = None) -> int:
    """CLI 主程式進入點"""
    try:
        app(args=args, standalone_mode=False)
        return 0
    except KeyboardInterrupt:
        typer.echo("\n\n操作已取消。")
        return 1
    except Exception as e:
        typer.echo(f"錯誤：{str(e)}", err=True)
        return 1


if __name__ == "__main__":
    import sys
    sys.exit(main())
