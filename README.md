# スタートアップガイド

このガイドでは、Pythonアプリケーション、Redis、RabbitMQ、Celery Workerを含むDocker環境のセットアップ方法について説明します。

## 前提条件

- DockerとDocker Composeがインストールされていることを確認してください。インストールに関する情報は、[Dockerの公式サイト](https://docs.docker.com/get-docker/)を参照してください。
- `.env.local` ファイルがプロジェクトディレクトリに存在し、必要な環境変数が定義されていることを確認してください。

## 環境変数の設定

- `.env.local` ファイルに `OPENAI_API_KEY` 環境変数を追加してください。このキーはOpenAIのAPIにアクセスするために必要です。

```bash
OPENAI_API_KEY=your_openai_api_key_here
```

## セットアップ手順

1. **Dockerイメージのビルド**:
 プロジェクトのルートディレクトリで以下のコマンドを実行して、Dockerイメージをビルドします。

 ```bash
  docker-compose build
  ```

## アプリケーションへのアクセス

- アプリケーションは `http://localhost:8000` で利用可能です。

## RabbitMQの管理インターフェース

- RabbitMQの管理インターフェースは `http://localhost:15672` でアクセスできます。

## Redisサーバー
- Redisサーバーはポート `6379` でローカルマシンに公開されています。

## テストの実行
- `test` フォルダ配下の `pytest` を実行するには、以下のコマンドを使用します。


```bash
docker-compose run python pytest
```

## 停止とクリーンアップ

- コンテナを停止するには、以下のコマンドを実行します。

```bash
docker-compose down
```
