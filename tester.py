import API
import time


<<<<<<< HEAD
api = API.API('rafael')
=======
api = API.API()
>>>>>>> 457fef991ac1c1ae8ae48646a43a9e980138f29e


while True:
    time.sleep(31)
    data = {'geladeira': 888}
    print('enviando ', list(data).pop(), '=', data[list(data).pop()])
    api.post_to_api('rafael', data)










#data = {'geladeira': 777}
#api.post_to_api('rafael', data)