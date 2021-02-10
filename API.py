import requests, time

class API:
    def __init__(self, user):
        self.user = user
        self.URL = "https://dry-lake-12607.herokuapp.com/"
        #self.URL = "https://dry-lake-12607.herokuapp.com/users/" + self.user + "/kwh/"
        self.start_time = time.time()
        self.post_data = dict()

    def post(self, data):
        '''Presume que user seja string e que data seja um dicionário'''
        
        self.URL = self.URL + 'users/' + self.user + "/kwh/"
        # Se o tempo determinado ainda não passou, atualiza os valores de post_data.
        key = list(data).pop()
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

    def get_all_users(self):
        '''Retorna todos os usuários cadastrados'''
        r = requests.get(self.URL)
        print(r.text)

    def create_new_user(self, fist_name, last_name):
        '''Cria um novo usuário'''
        request.post(self.URL + '/users/')


    def has_time_elapsed(self, minutes):
        '''Presume que minutes seja um valor do tipo Int.
        Retorna True se minutes*60 segundos se passaram.''' 
        
        end_time = time.time()
        if end_time - self.start_time < minutes*60:
            return False
        else:
            # Se se passou 15min, resete o relógio.
            self.start_time = time.time()
            return True

            return True
