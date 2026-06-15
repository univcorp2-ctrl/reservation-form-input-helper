# Setup Guide

## 1. Codespaces で開く

GitHub のリポジトリ画面から `Code` → `Codespaces` → `Create codespace` を選ぶと、依存関係のインストールまで自動で進みます。

## 2. プロフィールを設定

```bash
cp .env.example .env
```

`.env` に氏名、メール、電話番号などを入れます。

## 3. 実行

```bash
python -m reservation_input_helper --store ginza
```

店舗キー:

- `osaka`
- `ginza`
- `omotesando`
- `shinjuku`
- `nagoya-sakae`

## 4. 画面確認

入力後、ブラウザが開いたままになります。CAPTCHA と最終送信は人が確認して行ってください。

## 5. ローカル実行の場合

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
playwright install chromium
python -m reservation_input_helper --store ginza
```

Windows PowerShell では仮想環境有効化が次になります。

```powershell
.venv\Scripts\Activate.ps1
```
