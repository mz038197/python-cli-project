"""demo-cli 命令行工具的主要實現"""

import sys
import argparse
from typing import Optional, List


def add_numbers(nums: List[float]) -> float:
    """將數字相加"""
    return sum(nums)


def multiply_numbers(nums: List[float]) -> float:
    """將數字相乘"""
    result = 1
    for num in nums:
        result *= num
    return result


def greet(name: str = "World") -> str:
    """問候使用者"""
    return f"你好，{name}！歡迎使用 demo-cli 工具！"


def parse_args(args: Optional[List[str]] = None) -> argparse.Namespace:
    """解析命令行參數"""
    parser = argparse.ArgumentParser(
        prog="demo-cli",
        description="簡單的 Python CLI 工具示範",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
範例：
  demo-cli hello                 # 執行問候命令
  demo-cli hello Alice           # 用指定的名字問候
  demo-cli add 1 2 3 4 5        # 相加數字
  demo-cli multiply 2 3 4        # 相乘數字
        """
    )

    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s 0.1.0"
    )

    subparsers = parser.add_subparsers(
        dest="command",
        help="可用的命令"
    )

    # hello 命令
    hello_parser = subparsers.add_parser(
        "hello",
        help="問候使用者"
    )
    hello_parser.add_argument(
        "name",
        nargs="?",
        default="World",
        help="要問候的人名（預設值：World）"
    )

    # add 命令
    add_parser = subparsers.add_parser(
        "add",
        help="將數字相加"
    )
    add_parser.add_argument(
        "numbers",
        nargs="+",
        type=float,
        help="要相加的數字"
    )

    # multiply 命令
    multiply_parser = subparsers.add_parser(
        "multiply",
        help="將數字相乘"
    )
    multiply_parser.add_argument(
        "numbers",
        nargs="+",
        type=float,
        help="要相乘的數字"
    )

    return parser.parse_args(args)


def main(args: Optional[List[str]] = None) -> int:
    """CLI 主程式進入點"""
    try:
        parsed_args = parse_args(args)

        if parsed_args.command is None:
            # 沒有指定命令時，顯示幫助
            parse_args(["--help"])
            return 0

        if parsed_args.command == "hello":
            result = greet(parsed_args.name)
            print(result)
            return 0

        elif parsed_args.command == "add":
            result = add_numbers(parsed_args.numbers)
            print(f"結果：{result}")
            return 0

        elif parsed_args.command == "multiply":
            result = multiply_numbers(parsed_args.numbers)
            print(f"結果：{result}")
            return 0

        else:
            print(f"未知的命令：{parsed_args.command}")
            return 1

    except KeyboardInterrupt:
        print("\n\n操作已取消。")
        return 1
    except Exception as e:
        print(f"錯誤：{str(e)}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
