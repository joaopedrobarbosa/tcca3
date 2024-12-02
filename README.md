# tcca3

Repositório destinado para atividade A3 da UC teoria da computação e compiladores

### Rodando o projeto

Para criar um ambiente virtual e instalar as dependências:

```bash
./setup.sh
```

#### Para compilar e executar um arquivo .bahia

```bash
python main.py ./caminho/para/arquivo.bahia
```

O arquivo será compilado e executado.
O resultado será exibido no terminal.
A saída estará disponível em `./output.py`

#### Para rodar o servidor interativo (interface de usuário)

```bash
uvicorn main:app
```

Acesse a aplicação em `http://localhost:8000`

### Sobre o projeto

Implementada com a ajuda da biblioteca Ply, a linguagem Bahia é uma linguagem de programação de alto nível expressiva e de fácil compreensão.
As palavras chave da linguagem são derivadas da cultura baiana, refletindo a expressividade do povo baiano.

Um exemplo de código em Bahia:

```bahia
x = 0;
y = 2 * 3 + 4 * (5 - x);

se (x > 5) {
    amostre("x is greater than 5");
} senao {
    amostre("x is less than or equal to 5");
}

vai_de i (0 ate 10) {
    amostre(i);
    amostre("MANOWELL");
    se (x == i) {
        amostre("x == i");
    }
}

se (eh_mermo) {
    amostre(migue);
}

z = 5;
enquanto (z < 10) {
  amostre("RAPHAWELL");
  z = z + 1;
}
```

Palavras chave da linguagem:
se (if)
senao (else)
vai_de (for)
eh_mermo (True)
migue (False)
amostre (print)
enquanto (while)
