# Analisador Climático Inteligente

Uma aplicação console em Python projetada para consulta meteorológica em tempo real de qualquer localidade do mundo. O sistema consome APIs web em cadeia para localizar o texto inserido pelo usuário e retornar dados de temperatura e vento atualizados, acompanhados de alertas dinâmicos e personalizados.
# Desenvolvimento 

Este projeto foi construído de forma colaborativa, utilizando inteligência artificial como assistente técnica de para otimizar o fluxo de desenvolvimento e acelerar a entrega de código limpo.

Minha atuação direta no desenvolvimento do projeto envolveu:
* **Codificação e Refatoração:** Implementação direta do código em Python, garantindo que as estruturas de dados e funções estivessem organizadas de forma limpa.
* **Lógica de Negócios Personalizada:** Definição das faixas de temperatura exatas (30°C, 25°C, 20°C e 15°C) e criação das condicionais que guiam as recomendações do sistema.
* **Gestão de Requisitos:** Decisão de migrar de uma lista estática de cidades para um sistema de busca dinâmica por digitação livre.
* **Integração de APIs (Suporte da IA):** Utilização de inteligência artificial para acelerar a leitura da documentação, estruturar de forma ágil as chamadas à API e otimizar a extração de dados do JSON retornado pelo ecossistema (Open-Meteo).

## Funcionalidades

- **Busca Livre:** Digite o nome de qualquer cidade (nacional ou internacional).
- **Geocodificação Automática:** Converte o texto digitado em coordenadas geográficas (Latitude e Longitude) via API.
- **Lógica de Alertas Precisa:** Classifica a temperatura atual em faixas dinâmicas para gerar recomendações personalizadas de vestuário e cuidados.
- **Resiliência:** Tratamento de erros integrado para evitar interrupções no fluxo do software caso haja instabilidade na conexão de rede.

## Tecnologias e Conceitos Utilizados

- **Linguagem:** Python 3
- **Biblioteca:** `requests` (para comunicação HTTP)
- **Consumo de APIs REST:** Integração em cadeia com o ecossistema *Open-Meteo*
- **Tratamento de Dados:** Manipulação e extração de informações em formato **JSON**
- **Tratamento de Exceções:** Uso estratégico de blocos `try/except` para lidar com timeouts e falhas de conexão

## Regras de Negócio (Alertas de Temperatura)

O sistema avalia a temperatura recebida da API e responde dinamicamente:
- `≥ 30°C`: Alerta de calor extremo e hidratação.
- `≥ 25°C`: Temperatura agradável para atividades ao ar livre.
- `≥ 20°C`: Clima ameno (recomendação de casaco leve por garantia).
- `≥ 15°C`: Frio (uso de blusa obrigatório).
- `< 15°C`: Frio intenso.
