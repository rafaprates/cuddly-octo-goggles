# Exemplo de uso

```python
import API

# Instanciando a classe API.
# Presume que user_name seja uma String e que user_name esteja cadastrado no banco
api = API.API(user_name)

# Escrevendo um dado ao banco
# Presume que data seja um dicionário, onde as keys são strings que representam o nome do equipamento e os values é a potência consumida pelo equipamento.
# Exemplo: data = {'geladeira': 1500}
api.post(data)
```
