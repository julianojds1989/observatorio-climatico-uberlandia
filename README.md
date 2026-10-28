Observatório Climático Local - Uberlândia/MG

Objetivo

Analisar dados meteorológicos históricos da cidade de Uberlândia-MG para produzir indicadores climáticos que auxiliem a comunidade local na compreensão das condições climáticas do município.

Público-alvo
Moradores de Uberlândia
Estudantes
Comunidade escolar
Pequenos produtores rurais
Pessoas que realizam atividades ao ar livre

Fonte dos Dados
Open-Meteo Historical Weather API

Localidade
Uberlândia - MG
Latitude: -18.9186
Longitude: -48.2772

Período Analisado
01/09/2025 a 30/09/2025

Variáveis Meteorológicas
Temperatura máxima diária (°C)
Temperatura mínima diária (°C)
Precipitação diária acumulada (mm)

Estrutura do Projeto
coleta.py
banco.py
consultas.sql
requirements.txt
README.md

dados/
docs/AE2/

Instalação
pip install -r requirements.txt

Execução
1. Coleta dos dados
python coleta.py
2. Tratamento e carga no banco
python banco.py

Banco de Dados
O banco é gerado em:
dados/clima.duckdb

Principais Resultados
KPI 1 - Dia mais quente
Data: 11/09/2025
Temperatura máxima: 35,0°C
KPI 2 - Dia mais chuvoso
Data: 24/09/2025
Precipitação: 15,4 mm
KPI 3 - Dias chuvosos
Total: 7 dias

Indicadores Complementares
Temperatura máxima média: 31,16°C
Precipitação total acumulada: 39,2 mm

Limitações
O banco foi construído a partir de uma única fonte de dados (Open-Meteo), não havendo comparação com outras bases meteorológicas para validação independente.
Os indicadores calculados dependem diretamente da qualidade dos dados fornecidos pela API de origem; eventuais inconsistências ou atualizações da fonte podem refletir nos resultados armazenados no banco.
O banco foi desenvolvido para fins acadêmicos e extensionistas, não possuindo mecanismos avançados de auditoria, segurança ou versionamento de dados normalmente encontrados em sistemas de monitoramento meteorológico em produção.
