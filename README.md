# FIAP Software Security – Modelagem de Ameaças com IA

MVP para **detecção supervisionada de ameaças** a partir de diagramas de arquitetura de software, utilizando a metodologia **STRIDE**.

## Objetivos

- Desenvolver uma IA que interprete automaticamente um diagrama de arquitetura, identificando componentes (usuários, servidores, bases de dados, APIs, etc.).
- Gerar um **Relatório de Modelagem de Ameaças** baseado na metodologia STRIDE.
- Construir ou buscar um **dataset** de imagens de arquitetura de software.
- Anotar o dataset para treinar um modelo supervisionado na identificação de componentes.
- Treinar o modelo.
- Desenvolver um sistema que busque vulnerabilidades por componente e contramedidas por ameaça.

## Estrutura do Projeto

```
Hackathon/
├── README.md
├── requirements.txt
├── app.py                   # Frontend Streamlit (upload de diagrama)
├── docs/                    # Documentação do fluxo de desenvolvimento
├── dataset/                 # Imagens e anotações para treino
├── model/                   # Scripts de treino e modelos salvos
├── src/                     # Código da aplicação
│   ├── diagram_parser/      # Interpretação de diagramas (visão + ML)
│   ├── stride_report/       # Geração do relatório STRIDE
│   └── vulnerabilities/     # Busca de vulnerabilidades e contramedidas
└── tests/                   # Testes e arquiteturas de avaliação
```

*FIAP Software Security – Hackathon Fase 5 – IADT*
