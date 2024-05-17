# Criando-uma-Pipeline-de-CI-CD-com-GitHub-Actions-e-Testes-Automatizados

Criando uma Pipeline de CI/CD com GitHub Actions e Testes Automatizados
Objetivo: Configurar uma pipeline de CI/CD usando GitHub Actions para um projeto de software simples e escrever dois testes automatizados: um teste unitário e um teste de integração.

# Uma aplicação em flask

Este é um projeto simples para demonstrar a configuração de uma Pipeline de CI/CD com GitHub Actions e Testes Automatizados.

## Configuração do Projeto

1. **Criar um novo repositório no GitHub**: [Link para o repositório](link_para_o_repositório)

2. **Adicionar código básico da aplicação**: Adicione o código básico da sua aplicação Flask ao repositório.

## Configuração do GitHub Actions

Este projeto usa o GitHub Actions para automatizar a construção, teste e deploy da aplicação. O arquivo `ci-cd.yml` define a pipeline de CI/CD e contém as seguintes etapas:

- Instalação de dependências
- Execução de testes unitários
- Implantação em produção (condicional ao branch main)

## Testes Automatizados

Os testes automatizados são implementados usando o módulo `unittest` do Python. O arquivo `test_soma.py` contém os testes para a função de soma da aplicação. Os testes são executados como parte da pipeline de CI/CD para garantir que o código esteja funcionando conforme o esperado antes de ser implantado em produção.

## Dependências

As dependências para o funcionamento da aplicação estão listadas no arquivo `requirements.txt`. Este arquivo contém uma lista de pacotes Python necessários, incluindo o Flask e quaisquer outras bibliotecas utilizadas no projeto.

## Como a Pipeline de CI/CD Funciona

Quando ocorre um push no branch main ou é aberto um pull request para o branch main, a pipeline de CI/CD é acionada. Ela realiza as seguintes etapas:

1. Instalação de dependências: As dependências do projeto são instaladas usando o arquivo `requirements.txt`.
2. Execução de testes unitários: Os testes unitários são executados para garantir que o código esteja funcionando corretamente.
3. Implantação em produção: Se todos os testes passarem com sucesso e o push for para o branch main, a aplicação é implantada em produção.

Flask==2.0.2
Werkzeug==2.0.2
