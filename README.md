# python-cli-project

簡單的 Python CLI 工具示範，展示如何建立可全域安裝的命令行工具，並提供 Skill 文檔供 Claude Code Agent 使用。

## 安裝方式

### 開發模式安裝（適合貢獻者）

```bash
pip install -e .
```

### 全域安裝（適合使用者）

```bash
pip install .
```

或從 GitHub 直接安裝：

```bash
pip install git+https://github.com/username/python-cli-project.git
```

## 使用方式

安裝後，可以直接使用 `demo-cli` 命令：

```bash
# 查看幫助
demo-cli --help

# 執行簡單問候
demo-cli hello Alice

# 執行數字相加
demo-cli add 10 5 3
```

## 快速開始

1. **設定環境**
   ```bash
   pip install -e .
   ```

2. **執行測試**
   ```bash
   demo-cli hello
   ```

3. **添加 Skill 到 Claude Code Agent**
   ```bash
   npx skills add mz038197/python-cli-project
   ```

## 項目結構

```
python-cli-project/
├── pyproject.toml              # Python 打包配置
├── src/
│   └── demo_cli/
│       ├── __init__.py         # 套件初始化
│       ├── __main__.py         # 模組執行入口
│       ├── cli.py              # CLI 主邏輯
│       └── core.py             # 核心業務邏輯
├── tests/
│   ├── __init__.py             # 測試套件初始化
│   ├── test_core.py            # 核心邏輯測試
│   └── test_cli.py             # CLI 介面測試
├── skills/
│   └── python-cli-project/
│       └── SKILL.md            # Claude Code Agent Skill 文檔
├── README.md                   # 專案說明
└── LICENSE                     # MIT 授權
```

## Skill 文檔

本專案提供 Skill 文檔在 `skills/python-cli-project/SKILL.md`，說明如何使用 `demo-cli` 工具。

你可以通過以下命令將此 Skill 添加到 Claude Code Agent：

```bash
npx skills add mz038197/python-cli-project
```

## 測試

執行所有測試：

```bash
pytest
```

或使用 uv：

```bash
uv run pytest
```

## 授權

本項目採用 **MIT License**。詳見 `LICENSE` 文件。
