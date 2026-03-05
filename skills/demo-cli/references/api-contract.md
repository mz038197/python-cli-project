# demo-cli API 契約

## 命令列介面 (CLI)

### 全域命令入點

```bash
demo-cli [options] <command> [args]
```

### 命令清單

| 命令 | 用途 | 參數 | 範例 |
|-----|------|------|------|
| `hello` | 問候使用者 | `[name]` - 選擇性的人名 | `demo-cli hello Alice` |
| `add` | 相加數字 | `<numbers...>` - 一個或多個數字 | `demo-cli add 1 2 3 4 5` |
| `multiply` | 相乘數字 | `<numbers...>` - 一個或多個數字 | `demo-cli multiply 2 3 4` |

### 全域選項

| 選項 | 說明 |
|------|------|
| `--help` | 顯示幫助信息 |
| `--version` | 顯示版本號 |

### 輸出格式

成功時輸出結果到 stdout：

```
你好，World！歡迎使用 demo-cli 工具！
```

或

```
結果：15
```

失敗時輸出到 stderr：

```
錯誤：[錯誤訊息]
```

## 安裝方式

### 開發模式

```bash
pip install -e .
```

### 正式安裝

```bash
pip install .
```

### 從 GitHub 安裝

```bash
pip install git+https://github.com/username/python-cli-demo.git
```

## 版本

當前版本：**0.1.0**

查詢版本：

```bash
demo-cli --version
# 輸出：demo-cli 0.1.0
```

## 錯誤碼

| 代碼 | 說明 |
|-----|------|
| `0` | 成功 |
| `1` | 一般性錯誤（無效命令、參數錯誤等） |

## 環境變數

目前未使用任何環境變數。

## 相容性

- Python 版本：3.8+
- 作業系統：Windows、macOS、Linux
