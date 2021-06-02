# FastAPI-PostgreSQL-Backend-Base

**利用FastAPI與PostgreSQL實現「非同步」資料庫連線與使用者建立、登入功能作為開發模組**

**操作環境與預先安裝**
- Ubuntu==20.04
- docker-ce==20.10.5, build 55c4c88
- docker-compose==1.25.0
- Python==3.8.5
- Python packages: virtualenv==20.0.4

**使用流程**
1. 在資料夾外建立虛擬環境
    ```{bash}
    $ cd ../
    $ virtualenv Basic-FastAPI-Backend-Module
    ```
2. 將env改為.env，並修改.env與app config檔
   ```{bash}
   $ mv env .env
   ```
   - .env中，修改APP_HOST相關設定 (例如IP、PORT等)
   - src/configs/中，修改psql.py中資料庫連線設定，其餘config依使用需求調整
3. 安裝相依套件與建立定時任務置放資料夾
   ```{bash}
   $ cd Basic-FastAPI-Backend-Module
   $ source bin/activate
   $ pip install -r src/requirements.txt
   $ mkdir -p db/scheduler
   ```
4. 啟動資料庫與FastAPI
   **開啟2個terminal**
   ```{bash}
   <!-- 
   可將Makefile中，onDB target內容進行調整，使用-d參數使docker-compose於背景執行
   註記：首次使用不建議，需透過log查看資料庫是否正常啟動
   -->

   $ make onDB
   ```
   ```{bash}
   $ make run
   ```
5. 開啟瀏覽器(Browser)連線，利用FastAPI swagger測試，http://{IP}:{PORT}/docs