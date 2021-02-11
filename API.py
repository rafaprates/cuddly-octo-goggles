import requests, time

class API:
    def __init__(self):
        self.URL = "https://dry-lake-12607.herokuapp.com/"
        self.start_time = time.time()
        self.post_data = dict()

    def post(self, user, data):
        '''Presume que user seja string e que data seja um dicionário'''
        
        self.user = user
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
                print(self.post_data)
                r = requests.post(self.URL + 'users/' + self.user + '/kwh', self.post_data)
                print(self.URL + 'users/' + self.user + '/kwh')
                print(r)
            self.post_data.clear()
            return 
        return


    def get_all_users(self):
        '''Retorna todos os usuários cadastrados como JSON'''
        r = requests.get(self.URL + 'users/')
        print(r.text)
        return r.text

    def create_new_user(self, first_name, last_name):
        '''Cria um novo usuário.
        Presume que first_name e last_name sejam Strings'''
        #new_user = {'first_name': self.first_name, 'last_name': self.last_name}
        new_user = dict()
        new_user['first_name'] = self.first_name
        new_user['last_name'] = self.last_name
        request.post(self.URL + '/users/', new_user)
        return



    def has_time_elapsed(self, minutes):
        '''Presume que minutes seja um valor do tipo Int.
        Retorna True se minutes*60 segundos se passaram.''' 
        
        end_time = time.time()
        if end_time - self.start_time < minutes*10:
            return False
        else:
            # Se se passou 15min, resete o relógio.
            self.start_time = time.time()
            print('se passaram x min')
            return True
