# demo-cli 工作流程

## 典型使用流程

### 1. 安裝階段

使用者首先需要安裝 `demo-cli` 工具：

```bash
# 方式一：從 PyPI 安裝（正式發佈後）
pip install python-cli-demo

# 方式二：從 GitHub 安裝（開發版本）
pip install git+https://github.com/username/python-cli-demo.git

# 方式三：本地開發安裝
git clone https://github.com/username/python-cli-demo.git
cd python-cli-demo
pip install -e .
```

### 2. 驗證安裝

安裝後檢查工具是否正常：

```bash
# 查看版本
demo-cli --version

# 查看幫助
demo-cli --help
```

### 3. 基本使用

#### 使用問候命令

```bash
# 預設問候
demo-cli hello
# 輸出：你好，World！歡迎使用 demo-cli 工具！

# 自訂問候
demo-cli hello Bob
# 輸出：你好，Bob！歡迎使用 demo-cli 工具！
```

#### 執行計算

```bash
# 相加
demo-cli add 10 20 30
# 輸出：結果：60

# 相乘
demo-cli multiply 2 3 4
# 輸出：結果：24
```

### 4. 在腳本中使用

可以在 Shell 腳本或 Python 程式中使用 `demo-cli`：

#### Shell 腳本範例

```bash
#!/bin/bash

echo "開始執行計算..."

# 計算數字總和
sum=$(demo-cli add 100 200 300)
echo "總和：$sum"

# 計算數字乘積
product=$(demo-cli multiply 5 6 7)
echo "乘積：$product"

# 問候所有人
for person in Alice Bob Charlie; do
  demo-cli hello "$person"
done
```

#### Python 程式範例

```python
import subprocess
import sys

def run_demo_cli(command):
    """執行 demo-cli 命令並返回結果"""
    try:
        result = subprocess.run(
            ["demo-cli"] + command,
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"錯誤：{e.stderr}", file=sys.stderr)
        return None

# 使用範例
if __name__ == "__main__":
    # 執行問候
    greeting = run_demo_cli(["hello", "Alice"])
    print(greeting)

    # 執行計算
    result = run_demo_cli(["add", "5", "10", "15"])
    print(result)
```

### 5. 與 Claude Code Agent 集成

#### 添加 Skill 到 Claude

```bash
# 使用 skills 工具添加
npx skills add username/python-cli-demo
```

添加後，Claude Code Agent 可以：

1. 理解如何使用 `demo-cli` 工具
2. 在適當時機建議使用 `demo-cli`
3. 自動生成正確的命令語法

#### Claude 中的使用場景

Claude 可能會建議：

```
我建議使用 demo-cli 工具來計算：

$ demo-cli add 100 200 300
結果：600
```

## 進階場景

### 場景 1：批量計算

```bash
#!/bin/bash

# 計算多組數字的總和
values=(
  "1 2 3 4 5"
  "10 20 30"
  "100 200 300 400 500"
)

for value_group in "${values[@]}"; do
  result=$(demo-cli add $value_group)
  echo "計算結果：$result"
done
```

### 場景 2：錯誤處理

```bash
#!/bin/bash

# 執行命令並檢查返回碼
if demo-cli add 10 20 30 > /tmp/result.txt; then
  echo "計算成功："
  cat /tmp/result.txt
else
  echo "計算失敗"
  exit 1
fi
```

### 場景 3：集成到 CI/CD

```yaml
# GitHub Actions 範例
name: CLI Test

on: [push]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v2
        with:
          python-version: '3.8'
      - run: pip install -e .
      - run: demo-cli --version
      - run: demo-cli hello
      - run: demo-cli add 1 2 3 4 5
```

## 故障排除

### 問題 1：命令未找到

```
command not found: demo-cli
```

**解決方法：**

```bash
# 確認已安裝
pip list | grep python-cli-demo

# 重新安裝
pip install --force-reinstall python-cli-demo
```

### 問題 2：版本不相容

**解決方法：**

```bash
# 檢查 Python 版本
python --version  # 應該是 3.8 或以上

# 升級 pip
pip install --upgrade pip
```

### 問題 3：權限錯誤

```
PermissionError: [Errno 13] Permission denied
```

**解決方法（Windows）：**

以管理員身份執行命令提示字元，然後重新安裝。

**解決方法（Linux/macOS）：**

```bash
# 使用 --user 標籤安裝到使用者目錄
pip install --user python-cli-demo

# 或使用 sudo
sudo pip install python-cli-demo
```

## 學習路線

1. **基礎**：理解 CLI 工具的概念和 Python 套件結構
2. **進階**：學習如何建立自己的 CLI 工具
3. **高級**：實現 Entry Points 和 Skill 系統集成
