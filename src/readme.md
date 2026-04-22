# 🐾 Sistema de Gestão de Clínica Veterinária (SQLAlchemy)

## 📌 Objetivo

Este projeto tem como objetivo servir como prática completa de **SQLAlchemy**, cobrindo desde a modelagem de banco de dados até a organização em camadas (controller + service), simulando um cenário real de backend.

A proposta é evoluir gradualmente, construindo um sistema robusto e bem estruturado.

---

## 🧩 Cenário

Você foi contratado para desenvolver um sistema para uma clínica veterinária que deseja digitalizar seus processos.

O sistema deve gerenciar:

* Clientes
* Pets
* Veterinários
* Consultas
* Prontuários
* Pagamentos
* Tratamentos

---

## 🔄 Fluxo da Aplicação

1. Usuário interage via terminal (input)
2. Controller recebe a entrada
3. Controller chama a Service
4. Service executa regras de negócio
5. Service interage com o banco via models

---

## 🧠 Modelagem do Banco

### 👤 Cliente

* nome
* cpf
* telefone

Relacionamento:

* Um cliente pode ter vários pets

---

### 🐶 Pet

* nome
* espécie
* idade

Relacionamento:

* Pertence a um cliente
* Pode ter várias consultas
* Possui um prontuário

---

### 👨‍⚕️ Veterinário

* nome
* especialidade

Relacionamento:

* Pode atender várias consultas

---

### 📅 Consulta

* data
* descrição

Relacionamentos:

* Pertence a um pet
* Pertence a um veterinário
* Possui um pagamento

---

### 📄 Prontuário

* histórico médico

Relacionamento:

* Um para um com Pet

---

### 💰 Pagamento

* valor
* status

Relacionamento:

* Um para um com Consulta

---

### 💊 Tratamento (N:N)

* nome
* descrição

Relacionamento:

* Muitos para muitos com Pet

---

## 🔗 Relacionamentos obrigatórios

* 1:N → Cliente → Pets 
* 1:N → Pet → Consultas
* 1:N → Veterinário → Consultas
* 1:1 → Pet ↔ Prontuário
* 1:1 → Consulta ↔ Pagamento
* N:N → Pet ↔ Tratamento

---

## 🗄️ Banco de Dados

Requisitos:

* Utilizar SQLite inicialmente
* Criar engine
* Criar sessão
* Criar tabelas automaticamente

---

## ⚙️ Funcionalidades (CRUD)

### ➕ Inserções

* Criar cliente
* Adicionar pets ao cliente
* Criar veterinário
* Criar consulta
* Criar prontuário
* Criar pagamento

---

### 🔍 Consultas

* Listar pets de um cliente
* Listar consultas de um pet
* Visualizar prontuário
* Listar pagamentos pendentes

---

### ✏️ Atualizações

* Atualizar telefone do cliente
* Atualizar status de pagamento

---

### ❌ Deleções

* Remover pet
* Remover consulta

---

## 🧠 Regras de Negócio

* Não permitir consulta sem pet
* Não permitir consulta sem veterinário
* Não permitir pagamento sem consulta
* Garantir integridade dos relacionamentos

---

## 🔥 Desafios

### 1. Integridade de dados

* O que acontece ao deletar um cliente?
* Como tratar pets relacionados?
* Como lidar com consultas existentes?

Sugestões:

* Uso de cascade
* Definição de comportamento em deleção

---

### 2. Performance

* Evitar múltiplas queries desnecessárias
* Pensar em carregamento eficiente de dados

---

### 3. Organização de código

* Separar responsabilidades
* Não colocar lógica de negócio no controller
* Service deve centralizar regras

---

### 4. Escalabilidade

* Estruturar o projeto pensando em API futura

---

## 🧪 Controller (Simulação de API)

A camada de controller será baseada em funções que utilizam `input()` para simular requisições.

Exemplo de responsabilidades:

* Ler dados do usuário
* Validar entradas básicas
* Chamar services
* Exibir resultados

---

## 🧪 Service

Responsável por:

* Regras de negócio
* Validações
* Orquestração de operações no banco

---

## 🚀 Etapas de Desenvolvimento

### 1. Configuração inicial

* Criar conexão com banco
* Criar estrutura do projeto

### 2. Modelagem básica

* Cliente
* Pet

### 3. Relacionamentos 1:N

* Cliente → Pets
* Pet → Consultas

### 4. Adicionar consultas e veterinários

### 5. Relacionamentos 1:1

* Prontuário
* Pagamento

### 6. Relacionamento N:N

* Tratamentos

### 7. Implementar CRUD

### 8. Refatorar arquitetura

---

## 🧠 Boas Práticas

* Nomear bem tabelas e campos
* Usar padrões consistentes
* Separar responsabilidades
* Testar cada etapa antes de avançar

---

## 💡 Bônus (Opcional)

* Criar API com FastAPI
* Usar Alembic para migrations
* Criar dados iniciais (seed)
* Adicionar logs

---

## 🎯 Objetivo Final

Ao concluir este projeto, você deverá ser capaz de:

* Modelar bancos relacionais com SQLAlchemy
* Trabalhar com todos os tipos de relacionamento
* Organizar código em camadas
* Implementar regras de negócio corretamente
* Preparar base para sistemas reais

---


