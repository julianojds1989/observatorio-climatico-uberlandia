import duckdb
import pandas as pd
import json

with open(
    "dados/clima_uberlandia.json",
    "r",
    encoding="utf-8"
) as arquivo:
    dados = json.load(arquivo)

df = pd.DataFrame({
    "data": dados["daily"]["time"],
    "temperatura_max": dados["daily"]["temperature_2m_max"],
    "temperatura_min": dados["daily"]["temperature_2m_min"],
    "precipitacao": dados["daily"]["precipitation_sum"]
})

df["data"] = pd.to_datetime(df["data"])

print("=== VALIDAÇÕES ===")

print("\nValores ausentes:")
print(df.isnull().sum())

print("\nDuplicados:")
print(df.duplicated().sum())

print("\nQuantidade de registros:")
print(len(df))

con = duckdb.connect("dados/clima.duckdb")

con.execute("""
DROP TABLE IF EXISTS clima_uberlandia;
""")

con.execute("""
CREATE TABLE clima_uberlandia (
    data DATE,
    temperatura_max DOUBLE,
    temperatura_min DOUBLE,
    precipitacao DOUBLE
)
""")

con.register("df_temp", df)

con.execute("""
INSERT INTO clima_uberlandia
SELECT * FROM df_temp
""")

resultado = con.execute("""
SELECT *
FROM clima_uberlandia
LIMIT 5
""").fetchdf()

print("\n=== PRIMEIROS REGISTROS ===")
print(resultado)

con.close()

print("\nTabela carregada com sucesso!")
