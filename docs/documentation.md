# Documentação da API FastAPI

## Descrição geral

Este é um aplicativo FastAPI simples com dois endpoints que permitem criar e recuperar itens de uma loja fictícia. Os itens são armazenados em uma lista Python.

## Dependências necessárias

Este aplicativo requer as seguintes dependências:

- `fastapi`
- `pydantic`

Você pode instalar essas dependências usando pip:

```bash
pip install fastapi pydantic
```

## Modelos

### Item

Um objeto `Item` contém as seguintes propriedades:

- `name` (str): O nome do item.
- `description` (str): Uma descrição do item.
- `price` (float): O preço do item.

## Endpoints

### POST /items/

Cria um novo item.

#### Parâmetros

- `item` (Item): O item a ser criado (requerido)

#### Exemplo de uso

```bash
curl -X POST "http://localhost:8000/items/" -H "accept: application/json" -H "Content-Type: application/json" -d "{\"name\":\"foo\",\"description\":\"A foo item\",\"price\":12.99}"
```

### GET /items/{item_id}

Recupera um item pelo ID.

#### Parâmetros

- `item_id` (int): O ID do item a ser recuperado (requerido)

#### Exemplo de uso

```bash
curl -X GET "http://localhost:8000/items/0" -H "accept: application/json"
```

## Notas importantes

- Os IDs de item são atribuídos automaticamente na ordem em que os itens são criados. O primeiro item tem ID 0, o segundo tem ID 1 e assim por diante.
- Se você tentar recuperar um item que não existe (ou seja, um item com um ID que ainda não foi atribuído), a API retornará um erro 404.