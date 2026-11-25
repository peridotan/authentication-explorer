# Authentication Explorer

認証方式の仕組みと攻撃耐性を、図解とSTEP再生で学ぶ日本語のWeb教材です。IT業界の新人・若手など、認証の基本を学ぶ人を想定しています。

**バージョン：v1.0.0**

公開URL：https://peridotan.github.io/authentication-explorer/

## 使い方

- 01 認証方式の仕組み：認証方式を選び、次へ・自動再生などで通信と認証情報の所在を確認します。
- 02 認証方式の耐性：比較表で組み合わせを選択し、攻撃の成否と理由を確認します。「正常系と比較」で対応する正常STEPを確認でき、元の異常STEPへ戻れます。対応する正常処理がないSTEPは比較できません。
- 画面右上で配色・文字サイズを変更できます。詳細な前提は画面下部の「使い方・前提条件・参考資料」を参照してください。

## 閲覧環境

構成図とSTEP一覧・解説を見比べやすいPCでの閲覧を推奨します。スマートフォンでも利用できますが、構成図は画面幅に合わせて縮小表示され、横スクロールはできません。構成図を細部まで確認する用途にはPCをお使いください。

## 学習対象

認証方式はパスワード、パスワード＋TOTP、パスワード＋SMS OTP、パスワード＋プッシュ承認（単純承認）、パスキー（UV必須）の5種類です。認証情報の漏洩、フィッシング攻撃（AiTM型）、認証情報DBの漏洩、SMS受信先の乗っ取り、MFA疲労攻撃の5シナリオを扱います。対象となる組み合わせは17件です。

教育用の簡略モデルであり、実際の認証通信や攻撃は行いません。パスキーは同期型とデバイスバウンド型の共通部分を扱い、登録済み・UV必須・代替認証なしを前提とします。登録・同期・移行・復旧、ポリシー設定差、マルウェア感染、認証後のセッション窃取は対象外です。認証方式の評価は教材内の条件に限定され、実製品の安全性を保証しません。

## ローカル実行

`index.html` をブラウザーで開くだけで利用できます。ビルド、バックエンド、APIキーは不要です。外部参考資料のリンクを開く場合はインターネット接続が必要です。

## 検証

Python 3 と Playwright を使用します。

```sh
pip install playwright==1.55.0
python -m playwright install chromium
python tests/test_flows.py
python tests/test_ui.py
```

GitHub Actions でも同じ検証を実行する構成です。公開前の確認事項は `docs/RELEASE.md` を参照してください。

Chat側で実施したPlaywright検証結果と、今回の技術レビュー・残る未検証項目は [`QA-REPORT.md`](QA-REPORT.md) に記録しています。公開時の検証状況と残る制約も同レポートに記録しています。

## 参考資料

- NIST SP 800-63B-4: https://pages.nist.gov/800-63-4/sp800-63b.html
- W3C WebAuthn Level 3: https://www.w3.org/TR/webauthn-3/
- RFC 6238: https://www.rfc-editor.org/rfc/rfc6238
- OpenID Connect Core 1.0: https://openid.net/specs/openid-connect-core-1_0.html

## ライセンス

MIT License — Copyright (c) 2026 peridotan。詳細は [`LICENSE`](LICENSE) を参照してください。
