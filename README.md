# 仮想環境構築・実行方法

次のコマンドを実行します。
```
python -m venv env
```
このコマンドを実行すると、env ディレクトリに myvenv という仮想環境が作成されます。

仮想環境を有効にするには、次のコマンドを実行します。
```
env/Scripts/Activate.ps1
```

カレントディレクトリをmanage.pyがあるscrapingにします。
最終的には次のコマンドを実行します。
```
cd scraping
```

equirements.txt ファイルに記載されているパッケージをインストールするため、次のコマンドを実行します。
```
pip install -r requirements.txt
```

マイグレーションを適用させます。
```
python manage.py migrate
```

最後に以下のコマンドを実行します。
```
python manage.py runserver
```
実行したら、http:から始まるリンクが表示されるのでクリックして完了です。
