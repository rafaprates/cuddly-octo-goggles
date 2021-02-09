import API
import time


api = API.API('rafael')


while True:
    time.sleep(31)
    data = {'geladeira': 888}
    print('enviando ', list(data).pop(), '=', data[list(data).pop()])
    api.post_to_api('rafael', data)










#data = {'geladeira': 777}
#api.post_to_api('rafael', data)