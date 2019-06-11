class Utils():
 
    @classmethod
    def validate(cls, data):
        errMsg = []
        noInput = 'が未入力です。'
        if not data['weight']:
            errMsg.append('重み' + noInput)
        if not data['fruity']:
            errMsg.append('果実味' + noInput)
        if not data['acidity']:
            errMsg.append('酸味' + noInput)
        if not data['spicy']:
            errMsg.append('辛み' + noInput)
        return errMsg