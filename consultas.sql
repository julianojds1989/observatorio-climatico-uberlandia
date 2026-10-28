-- KPI 1 - Dia mais quente

SELECT
    data,
    temperatura_max
FROM clima_uberlandia
ORDER BY temperatura_max DESC
LIMIT 1;

-- KPI 2 - Dia mais chuvoso

SELECT
    data,
    precipitacao
FROM clima_uberlandia
ORDER BY precipitacao DESC
LIMIT 1;

-- KPI 3 - Dias chuvosos

SELECT
    COUNT(*) AS dias_chuvosos
FROM clima_uberlandia
WHERE precipitacao > 0;

-- Temperatura máxima média

SELECT
    ROUND(AVG(temperatura_max),2) AS media_temperatura_max
FROM clima_uberlandia;

-- Precipitação total

SELECT
    ROUND(SUM(precipitacao),2) AS precipitacao_total
FROM clima_uberlandia;
