# tcca3

Repositório destinado para atividade A3 da UC teoria da computação e compiladores

### Rodando o projeto

Crie um novo ambiente virtual:

```bash
python -m venv .venv && source ./.venv/bin/activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

#### Para compilar e executar um arquivo .bahia

```bash
python main.py ./caminho/para/arquivo.bahia
```

O arquivo será compilado e executado, e o resultado será exibido no terminal.
A saída estará disponível em `./output.py`

#### Para rodar o servidor interativo (interface de usuário)

```bash
uvicorn main:app
```
