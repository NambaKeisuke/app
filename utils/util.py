class Utils():
 
    @classmethod
    def validate(cls, data):
        errMsg = []
        noInput = 'が未入力です。'
        if not data['name']:
            errMsg.append('甘さ' + noInput)
        if not data['volume']:
            errMsg.append('辛さ' + noInput)
        if not data['author']:
            errMsg.append('酸っぱさ' + noInput)
        if not data['publisher']:
            errMsg.append('酸っぱさ' + noInput)
        return errMsg