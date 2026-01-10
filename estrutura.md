# Projeto: Aplicação Web com Kubernetes e MySQL

## 📌 Visão Geral

Este projeto tem como objetivo demonstrar uma arquitetura **simples, realista e gerenciável** usando Kubernetes.

A aplicação permite a **inserção de dados via formulário web**, que são enviados para um **backend Python**, responsável por persistir os dados em um **banco MySQL** executando no Kubernetes.

O foco do projeto é **aprendizado de arquitetura e orquestração**, não complexidade de código.

---

## 🧱 Arquitetura

```
[ Navegador ]
      ↓ HTTP
[ Frontend Web ]
      ↓ /api
[ Backend Python ]
      ↓
[ MySQL ]
```

No Kubernetes:

```
Ingress
 ├── frontend-service (ClusterIP)
 └── backend-service (ClusterIP)
        ↓
     backend-pods
        ↓
mysql-headless-service
        ↓
mysql-statefulset
        ↓
PersistentVolumeClaim
```

---

## 🧩 Componentes do Projeto

### Frontend

* Página web simples (HTML + JS)
* Contém formulário para envio de dados
* Comunica-se apenas com o backend via HTTP

### Backend

* Python (Flask ou FastAPI)
* Recebe dados do frontend
* Valida e insere dados no MySQL
* Stateless (pode escalar)

### Banco de Dados

* MySQL (imagem oficial do Docker Hub)
* Executa em StatefulSet
* Usa volume persistente (PVC)

---

## 🐳 Containerização

* Cada componente possui sua **própria imagem Docker**
* Imagens publicadas em registry (ex: Docker Hub)

```
frontend → imagem própria
backend  → imagem própria
mysql    → mysql:8 (oficial)
```

---

## ☸️ Objetos Kubernetes Utilizados

### Frontend

* Deployment
* Service (ClusterIP)

### Backend

* Deployment
* Service (ClusterIP)
* ConfigMap (configurações)
* Secret (credenciais do banco)

### MySQL

* StatefulSet
* Headless Service
* PersistentVolumeClaim

### Exposição

* Ingress (ponto único de entrada)

---

## 🔗 Comunicação Entre Componentes

### Frontend → Backend

* HTTP
* Roteado via Ingress
* Endpoint `/api`

### Backend → MySQL

* DNS do Service
* Exemplo:

```
mysql-0.mysql:3306
```

---

## 🔐 Boas Práticas Adotadas

* Nenhum IP fixo
* Senhas fora do código-fonte
* Banco com persistência
* Componentes desacoplados
* Escalabilidade horizontal

---

## 🎯 Objetivos de Aprendizado

* Entender a transição de aplicações simples para Kubernetes
* Separar frontend, backend e banco corretamente
* Utilizar Services e DNS do Kubernetes
* Trabalhar com StatefulSet e PVC
* Usar Ingress como ponto de entrada

---

## 🚀 Evoluções Futuras (opcional)

* Helm Chart
* TLS no Ingress
* Autenticação
* Monitoramento (Prometheus / Grafana)
* CI/CD

---

## 📎 Observações Finais

Este projeto não utiliza Docker Compose em produção.
O Docker Compose pode existir **apenas para desenvolvimento local**.

> Kubernetes não gerencia aplicações, ele gerencia **serviços em execução contínua**.
