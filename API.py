import requests, time

class API:
    def __init__(self):
        self.URL = "http://127.0.0.1:8000/users/rafael/kwh"
        self.start_time = time.time()
        self.end_time = 0
        self.post_data = dict()


    def post_to_api(self, user, data):
        '''Presume que user seja string e que data seja um dicionário'''
        
        # Se o tempo determinado ainda não passou, atualiza os valores de post_data.
        key = list(data).pop()
        print('A key é ->', key)
        if key in list(self.post_data):
            # Se já existe uma key contido em post_data, atualiza o valor de post_data.
            self.post_data[key] += data[key]
        else:
            # Se a key de data não existe em post_data, acrescenta key em post_data 
            self.post_data[key] = data[key]
    
        if self.has_time_elapsed(1) == True:
            # Se se passaram 15min, deve escrever as informações no banco.
            for key, value in self.post_data.items():
                self.post_data = dict()
                self.post_data["eq"] = key
                self.post_data["kwh"] = value
                r = requests.post(self.URL, self.post_data)
            self.post_data.clear()
            return 
        return


    def has_time_elapsed(self, minutes):
        '''Presume que minutes seja um valor do tipo Int.
        Retorna True se minutes*60 segundos se passaram.''' 
        
        end_time = time.time()
        if end_time - self.start_time < minutes*60:
            print('has_time_elapsed() -> FALSE')
            print('self.start_time', self.start_time)
            return False
        else:
            # Se se passou 15min, resete o relógio.
            self.start_time = time.time()
            print('has_time_elapsed TRUE')
            return True