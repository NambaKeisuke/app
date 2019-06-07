from bottle import Bottle, route, run, jinja2_template as template, static_file, request,redirect
import bottle
from utils.util import Utils
#import routes
 
#app = routes.app

@bottle.get('/static/<filePath:path>')
def index(filePath):
    return static_file(filePath, root='./static')

@bottle.route('/', method=['POST','GET'])
def add():
    view = ""
    registId = ""
    form = {}
    kind = "入力"
    data = ["かなり弱めの方がいい　", "少し弱めの方がいい　", "ちょうどいい　", "少し強めの方がいい　", "かなり強めの方がいい"]

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
        form['name'] = request.forms.decode().get('name')
        form['volume'] = request.forms.decode().get('volume')
        form['author'] = request.forms.decode().get('author')
        form['publisher'] = request.forms.decode().get('publisher')
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
            headers = ['ワインの甘さ', 'ワインの辛さ', 'ワインの酸っぱさ', 'ワインの香り', 'メモ']
            return template('confirm.html'
                    , form=form
                    , headers=headers
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