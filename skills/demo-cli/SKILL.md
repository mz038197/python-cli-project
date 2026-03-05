---
name: demo-cli
description: 簡單的 Python CLI 工具示範，用於教學如何建立可全域安裝的命令行工具和 Skill 系統。
---

# demo-cli Skill

使用 `demo-cli` 工具進行簡單的計算和文字操作。

## 安裝方式

### 全域安裝 CLI 工具

```bash
pip install python-cli-demo
```

### 將 Skill 添加到 Claude Code Agent

```bash
npx skills add username/python-cli-demo
```

## 使用方式

安裝後，可直接執行 `demo-cli` 命令：

### 問候命令

```bash
# 基本問候
demo-cli hello

# 自訂名字
demo-cli hello Alice
```

### 計算命令

```bash
# 數字相加
demo-cli add 1 2 3 4 5
# 輸出：結果：15

# 數字相乘
demo-cli multiply 2 3 4
# 輸出：結果：24
```

## CLI 參數說明

| 命令 | 參數 | 說明 |
|-----|------|------|
| `hello` | `[name]` | 問候指定的人名（預設值：World） |
| `add` | `<numbers...>` | 將多個數字相加（必填至少一個數字） |
| `multiply` | `<numbers...>` | 將多個數字相乘（必填至少一個數字） |
| `--version` | 無 | 顯示版本號 |
| `--help` | 無 | 顯示幫助信息 |

## 工作流程

使用 `demo-cli` 的典型流程：

1. **安裝工具**
   ```bash
   pip install python-cli-demo
   ```

2. **執行命令**
   ```bash
   demo-cli hello Alice
   ```

3. **查看結果**
   ```
   你好，Alice！歡迎使用 demo-cli 工具！
   ```

## 範例場景

### 場景 1：簡單計算

當需要快速計算時：

```bash
demo-cli add 100 200 300 400
# 輸出：結果：1000

demo-cli multiply 10 5 2
# 輸出：結果：100
```

### 場景 2：批量處理

可以在 shell 腳本中使用：

```bash
#!/bin/bash
for i in {1..5}; do
  result=$(demo-cli add $i $(($i+1)) $(($i+2)))
  echo "第 $i 組：$result"
done
```

## 常見問題

### Q: 如何更新 demo-cli？

```bash
pip install --upgrade python-cli-demo
```

### Q: 如何卸載？

```bash
pip uninstall python-cli-demo
```

### Q: 如何查看完整幫助？

```bash
demo-cli --help
demo-cli add --help
```

## 相關資源

- 官方儲存庫：https://github.com/username/python-cli-demo
- PyPI 頁面：https://pypi.org/project/python-cli-demo/
- 問題回報：https://github.com/username/python-cli-demo/issues
