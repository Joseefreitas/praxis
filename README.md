# PRÁXIS

**Um auxiliador educacional para a construção de prompts com Inteligência Artificial.**

O PRÁXIS é um projeto acadêmico desenvolvido com Python que busca incentivar o uso consciente e eficiente da Inteligência Artificial na educação.

A ferramenta foi pensada para estudantes do Ensino Médio que estão se preparando para o ENEM. Seu objetivo é ajudar esses estudantes a desenvolverem melhores prompts, compreendendo como formular solicitações mais claras e eficientes para ferramentas de IA.

Em vez de simplesmente executar o pedido do estudante, o PRÁXIS analisa o prompt, identifica possíveis melhorias e apresenta uma versão aprimorada, incentivando a autonomia e o pensamento crítico.

Video da aplicação no [Youtube](https://youtu.be/Tbb5Q33egLs).

## Funcionalidades

- **Análise de prompts:** avalia clareza, contexto, especificidade e formato esperado.
- **Sugestões de melhoria:** identifica problemas reais e apresenta recomendações.
- **Prompt aprimorado:** propõe uma versão melhorada sem alterar a intenção original do estudante.
- **Gerenciamento de usuários:** permite cadastrar, consultar, atualizar e excluir perfis.
- **Autenticação:** acesso por login e senha.
- **Modo anônimo:** permite utilizar o auxiliador sem cadastro e sem registrar histórico local.
- **Histórico individual:** armazena e permite consultar as análises de cada estudante.
- **Exclusão de histórico:** remove as análises associadas quando um usuário é excluído.

## Tecnologias utilizadas

- Python
- Groq API
- CSV
- Git e GitHub

## Como executar localmente

### 1. Clonar o repositório

```bash
git clone https://github.com/Joseefreitas/praxis.git

cd praxis
```

### 2. Criar um ambiente virtual

```bash
python -m venv .venv
```

### 3. Ativar o ambiente virtual

**Linux ou Mac:**

```bash
source .venv/bin/activate
```

**Windows:**

```powershell
.venv\Scripts\activate
```

### 4. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 5. Configurar a API

O PRÁXIS utiliza a API da Groq para realizar as análises dos prompts.

Crie uma chave de API na plataforma da [Groq](https://console.groq.com/) e configure um arquivo `.env` na raiz do projeto:

```env
GROQ_API_KEY=sua_chave_aqui
```

**Importante:** não compartilhe sua chave de API nem envie o arquivo `.env` para o GitHub.

### 6. Executar o projeto

```bash
python main.py
```

## Armazenamento de dados

O projeto utiliza arquivos CSV para armazenar os dados localmente:

| Arquivo | Finalidade |
| --- | --- |
| `usuarios.csv` | Dados dos usuários cadastrados |
| `historico.csv` | Histórico individual das análises |

Os arquivos são criados automaticamente conforme o uso do programa.

O modo anônimo não gera registros no histórico local.

## Estrutura do projeto

```text
praxis/
├── main.py
├── usuarios.py
├── analisador.py
├── requirements.txt
├── .env
├── usuarios.csv
└── historico.csv
```

Os arquivos `.env`, `usuarios.csv` e `historico.csv` são gerados ou configurados localmente e não devem ser compartilhados no repositório.

## Sobre o projeto

O PRÁXIS foi desenvolvido como parte de um projeto acadêmico da graduação em Gestão da Tecnologia da Informação, na CESAR School.

A proposta é explorar como a Inteligência Artificial pode contribuir para a educação, não substituindo o processo de aprendizagem, mas ajudando os estudantes a desenvolverem autonomia no uso dessas ferramentas, sem perda de pensamento crítico.

---

**PRÁXIS — Aprender a perguntar também faz parte de aprender.**
