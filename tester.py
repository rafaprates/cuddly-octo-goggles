import API 
import time



api = API.API()


while True:
    time.sleep(10)
    data = {'geladeira': 888}
    print('enviando ', list(data).pop(), '=', data[list(data).pop()])
    api.post('rafael', data)











#data = {'geladeira': 777}
#api.post_to_api('rafael', data)
