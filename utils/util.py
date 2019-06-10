class Utils():
 
    @classmethod
    def validate(cls, data):
        errMsg = []
        noInput = 'が未入力です。'
        if not data['name']:
            errMsg.append('重み' + noInput)
        if not data['volume']:
            errMsg.append('果実味' + noInput)
        if not data['author']:
            errMsg.append('酸味' + noInput)
        if not data['publisher']:
            errMsg.append('辛み' + noInput)
        return errMsg