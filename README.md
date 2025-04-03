# Desafio Vinteum - Bitcoin Regtest com RPC

Este repositório demonstra o uso do Bitcoin Core em modo `regtest` rodando dentro de um container Docker, com interações via 
chamadas RPC usando Python. A proposta faz parte do desafio prático do seminário da [Vinteum](https://vinteum.org/).

## Pré-requisitos

- Docker
- Python 3
- Biblioteca `requests` (instalar com `pip3 install requests`)

## Como executar

### 1. Inicie o container `bitcoind`:

```bash
docker run -d --name bitcoind-regtest \
  -v $HOME/bitcoin-data:/bitcoin \
  -p 18443:18443 -p 18444:18444 \
  ruimarinho/bitcoin-core \
  -regtest=1 \
  -printtoconsole \
  -rpcallowip=0.0.0.0/0 \
  -rpcbind=0.0.0.0 \
  -rpcuser=bitcoin \
  -rpcpassword=local321 \
  -fallbackfee=0.0002
