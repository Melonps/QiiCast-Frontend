
# QiiCast-FRONTEND

このリポジトリは先端ソフトウェア環境構築実践のグループ課題（グループH）、QiiCast-FRONTEND プロジェクトの一部です。

main: https://github.com/penguin-prg/OMU-TeamProject-GroupH

backend: https://github.com/Melonps/QiiCast-Backend

## 必要な設定
- conf/secret.ymlに、Qiita API v2のアクセストークンを入れる
    ```
    qiita_v2:
        access_token: [ここにアクセストークンを置く]    
    ```
    - ATTENTION: このファイルはpushしないように

## インストール手順
以下の手順に従って、プロジェクトをセットアップしてください。




1. Dockerコンテナを起動

    ```shell
    TODO
    ```

2. アプリケーションを起動

    ```shell
    streamlit run src/app.py
    ```
上記コマンドを実行することで、プロジェクトがローカル環境で起動。
ウェブブラウザで http://localhost:8501 にアクセスすると、アプリケーションが表示されます。
