# 💈 Sistema de Vendas - Barbearia

Um sistema de gerenciamento de vendas e estoque de produtos voltado para barbearias, desenvolvido em **Python** com interface gráfica interativa utilizando **Tkinter**.

---

## 📋 Sumário
- [Visão Geral](#-visão-geral)
- [Funcionalidades](#-funcionalidades)
- [Tecnologias Utilizadas](#-tecnologias-utilizadas)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Como Executar o Projeto](#-como-executar-o-projeto)
- [Licença](#-licença)

---

## 🔍 Visão Geral

O **Sistema de Vendas para Barbearia** foi projetado para facilitar o controle e a administração do estoque e das vendas de produtos comercializados no estabelecimento. 

A aplicação conta com uma interface gráfica simples, intuitiva e amigável. Todas as operações são executadas por meio de campos de entrada e botões interativos, dispensando o uso do terminal. Além disso, o sistema conta com validação de dados, tratamento de exceções, atualização de estoque em tempo real e cálculo automático do faturamento total.

---

## ✨ Funcionalidades

- **📦 Cadastro de Produtos:** Adicione novos itens informando nome, preço e quantidade inicial em estoque.
- **👁️ Exibição em Tempo Real:** Listagem organizada de todos os produtos cadastrados com seus respectivos detalhes.
- **🛒 Registro de Vendas:** Baixa e controle automático da quantidade disponível no estoque ao realizar uma venda.
- **🔍 Busca por Nome:** Localize rapidamente produtos específicos no sistema.
- **🏷️ Aplicação de Descontos:** Aplique porcentagens de desconto nos valores dos produtos.
- **💲 Atualização de Preços:** Modifique os valores cadastrados dos produtos a qualquer momento.
- **📥 Reposição de Estoque:** Adicione novas unidades aos produtos já existentes.
- **🗑️ Remoção de Produtos:** Delete itens obsoletos ou incorretos do cadastro.
- **📊 Controle de Faturamento:** Acompanhe o total acumulado gerado pelas vendas realizadas.
- **⚠️ Feedback Visual:** Mensagens popup de aviso, erro e confirmação (`messagebox`) para evitar falhas operacionais.

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** [Python 3](https://www.python.org/)
- **Interface Gráfica:** [Tkinter](https://docs.python.org/3/library/tkinter.html)

### Componentes de Interface Utilizados
- `Tk()` — Janela principal da aplicação.
- `Label`, `Entry`, `Button`, `Frame` e `LabelFrame` — Organização gráfica e interação.
- `Text` — Exibição dinâmica e estruturada da lista de produtos.
- `messagebox` — Alertas de confirmação, aviso e erros.
- `ttk.Style` — Estilização e personalização visual do sistema.

### Arquitetura e Programação
- Armazenamento em memória através de dados/estruturas globais.
- Modularização das operações em funções Python.
- Estruturas condicionais (`if`, `elif`, `else`) para fluxos de decisão.
- Tratamento de exceções (`try`, `except`) para validação de entradas numéricas.
- Manipulação baseada em eventos via GUI.

---

## 📂 Estrutura do Projeto

```text
.
├── main.py          # Código-fonte principal da aplicação
├── README.md        # Documentação do projeto