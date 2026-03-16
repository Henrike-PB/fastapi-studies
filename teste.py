from fastapi import FastAPI

'''
Aqui é onde iremos criar nossa API, definimos primeiro o app e instanciamos a classe FastAPI, depois criamos uma rota para o endpoint raiz ("/") e definimos uma função que retorna uma string indicando que a API está no ar.
'''
# definição do app
app = FastAPI()

'''
Aqui criamos um dicionário de exemplo chamado orders, onde cada chave é um número inteiro representando o ID da venda, e o valor é outro dicionário contendo informações sobre o item vendido, o preço unitário e a quantidade vendida.
'''
orders = {
    1: {"item": "lata", "preco_unitario": 4, "quantidade": 5},
    2: {"item": "garrafa 2L", "preco_unitario": 15, "quantidade": 5},
    3: {"item": "garrafa 750ml", "preco_unitario": 10, "quantidade": 5},
    4: {"item": "lata mini", "preco_unitario": 2, "quantidade": 5},
}

# definção da rota para o endpoint raiz
@app.get("/")
def home():
    return {"total_vendas": len(orders)}

@app.get("/orders/{order_id}")
def get_orders(order_id: int):
    if order_id in orders:
        return orders[order_id]
    else:
        return {"erro": "Pedido não encontrado"}