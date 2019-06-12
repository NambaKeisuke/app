from bottle import Bottle, route, run, jinja2_template as template, static_file, request,redirect
import bottle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

from utils.util import Utils
from recommend import Recommend, search_info
#import routes

#app = routes.app

#ワインのステータスデータの読み込み
base_df = pd.read_csv("./data/demo_wine.csv")

#ワインの属性データの読み込み
wine_df = pd.read_csv("./data/wine_modified.csv")

@bottle.get('/static/<filePath:path>')
def index(filePath):
    return static_file(filePath, root='./static')

@route('/add', method=['POST','GET'])
def add():
    view = ""
    registId = ""
    form = {}
    kind = "入力"
    data = [-2, -1, 0, 1, 2]

    # GETされた場合
    if request.method == 'GET':
        # TODO: id指定された場合
 
        # 表示処理
        return template('add.html'
                , form = form
                , kind=kind
                , registId=registId
                , data=data)
 
    # POSTされた場合
    if request.method == 'POST':
        # POST値の取得
        form['evaluation'] = request.forms.decode().get('evaluation')
        form['weight'] = request.forms.decode().get('weight')
        form['fruity'] = request.forms.decode().get('fruity')
        form['acidity'] = request.forms.decode().get('acidity')
        form['spicy'] = request.forms.decode().get('spicy')
        form['memo'] = request.forms.decode().get('memo')
        registId = ""
        # idが指定されている場合
        if request.forms.decode().get('id') is not None:
            registId = request.forms.decode().get('id')
 
        # バリデーション処理
        errorMsg = []
        errorMsg = Utils.validate(data=form)

        # 表示処理
 
        # 確認画面から戻る場合
        if request.forms.get('next') == 'back':
            return template('add.html'
                    , form=form
                    , kind=kind
                    , registId=registId
                    , data=data)
 
        if not errorMsg:
            headers = ['重み（軽やか - 濃厚）', '果実味（スパイシー - フルーティ）', '酸味（まろやか - シャープ）', '辛み（甘い - 辛い）', 'メモ']
            temp_df = Recommend(base_df, wine=0, weight=form['weight'], fruity=form['fruity'], acidity=form['acidity'], spicy=form['spicy'])
            df = search_info(temp_df, wine_df)
            return template('confirm.html'
                    , form=form
                    , headers=headers
                    , df=df
                    , registId=registId)
        else:
            return template('add.html'
                    , error=errorMsg
                    , kind=kind
                    , form=form
                    , registId=registId
                    , data=data)
 
if __name__ == '__main__':
    run(port=8080, reloader=True, debug=True)