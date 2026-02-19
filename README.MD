# 💳 Payment API – Stripe-like Simulation

API de processamento de pagamentos inspirada no fluxo do Stripe.

Projeto desenvolvido com foco em arquitetura backend profissional, incluindo autenticação JWT, gerenciamento de pedidos e simulação de Payment Intent.

---

## 🚀 Tecnologias Utilizadas

- Python 3
- Flask
- Flask SQLAlchemy
- PostgreSQL
- Flask JWT Extended
- Flask Bcrypt
- UUID para identificação de entidades
- Arquitetura modular com Blueprints

---

## 📦 Funcionalidades

✔ Registro e autenticação de usuários  
✔ Criação de pedidos (Order)  
✔ Criação de Payment Intent  
✔ Confirmação de pagamento  
✔ Atualização automática do status do pedido  
✔ Proteção de rotas com JWT  
✔ Hash seguro de senha com bcrypt  

---

## 🧠 Fluxo de Pagamento

1. Usuário cria um pedido (status: `PENDING`)
2. Usuário cria um Payment Intent
3. Usuário confirma o pagamento
4. Pedido é atualizado automaticamente para `PAID`

---

## 🔐 Autenticação

A API utiliza JWT.

Após login, utilize o token no header:

## 📌 Endpoints Principais

### 🔹 Auth

**POST** `/auth/register`
```json
{
  "email": "user@email.com",
  "password": "123456"
}

POST /auth/login


🔹 Orders

POST /orders/

{
  "amount": 150.00
}

🔹 Payments

POST /payments/create-intent

{
  "order_id": "UUID_DO_PEDIDO"
}


POST /payments/confirm

{
  "payment_intent_id": "ID_DO_PAYMENT_INTENT"
}


⚙️ Configuração do Projeto
1️⃣ Clone o repositório
git clone URL_DO_REPOSITORIO
cd payment-api

2️⃣ Crie o ambiente virtual
python -m venv venv


Ativar:

Windows:

venv\Scripts\activate


Mac/Linux:

source venv/bin/activate

3️⃣ Instale as dependências
pip install -r requirements.txt

4️⃣ Configure as variáveis de ambiente

Crie um arquivo .env:

DATABASE_URL=postgresql://usuario:senha@localhost:5432/payment_db
JWT_SECRET_KEY=sua_chave_secreta


Ou para testes rápidos:

DATABASE_URL=sqlite:///payment.db
JWT_SECRET_KEY=dev_secret

5️⃣ Execute a aplicação
python app.py


A API estará disponível em:

http://127.0.0.1:5000



🏗 Arquitetura
payment-api/
│
├── app.py
├── config.py
├── extensions.py
├── models.py
│
├── routes/
│   ├── auth.py
│   ├── orders.py
│   └── payments.py