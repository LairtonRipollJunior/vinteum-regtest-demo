import requests
import json
from base64 import b64encode

# Configuração do RPC
rpc_user = "bitcoin"
rpc_password = "local321"
rpc_port = 18443
rpc_url = f"http://127.0.0.1:{rpc_port}/"

# Autenticação básica
headers = {
    "content-type": "application/json",
    "Authorization": "Basic " + b64encode(f"{rpc_user}:{rpc_password}".encode()).decode('utf-8')
}

# Função para fazer chamadas RPC
def rpc_call(method, params=[]):
    payload = json.dumps({
        "method": method,
        "params": params,
        "jsonrpc": "2.0",
        "id": 0,
    })
    response = requests.post(rpc_url, headers=headers, data=payload)
    return response.json()

# Gerar um novo endereço de destino
dest_address = rpc_call("getnewaddress")["result"]

# Enviar 1 BTC para o novo endereço
txid = rpc_call("sendtoaddress", [dest_address, 1.0])["result"]

print(f"Transação enviada com sucesso! TXID: {txid}")
# Função para fazer chamadas RPC
def rpc_call(method, params=[]):
    payload = json.dumps({
        "method": method,
        "params": params,
        "jsonrpc": "2.0",
        "id": 0,
    })
    response = requests.post(rpc_url, headers=headers, data=payload)
    return response.json()

# Gerar um novo endereço de destino
dest_address = rpc_call("getnewaddress")["result"]

# Enviar 1 BTC para o novo endereço
txid = rpc_call("sendtoaddress", [dest_address, 1.0])["result"]

print(f"Transação enviada com sucesso! TXID: {txid}")

