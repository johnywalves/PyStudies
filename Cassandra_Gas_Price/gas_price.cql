CREATE KEYSPACE gas_price WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1};

CREATE TABLE gas_price.vendas (
    regiao text,
    estado text,
    municipio text,
    revenda text,
    produto text,
    dt_coleta text,
    mes int,
    ano int,    
    valor_compra float,
    valor_venda float,
    unidade_medida text,
    bandeira text,
    PRIMARY KEY (regiao, estado, municipio, revenda, produto, bandeira, dt_coleta)
);

CREATE TABLE gas_price.vendas_valor (
    municipio text,
    bandeira text,    
    revenda text,
    produto text,
    dt_coleta text,
    valor_venda float,
    PRIMARY KEY ((municipio, produto), valor_venda, bandeira, revenda, dt_coleta)
) WITH CLUSTERING ORDER BY (valor_venda ASC);

CREATE TABLE gas_price.dolares_mes (
    ano int,    
    mes int,
    valor_compra float,
    PRIMARY KEY ((ano, mes))
);

CREATE TABLE gas_price.combustivel_mes (
    ano int,
    mes int,
    produto text,
    valor_venda float,
    qtd int,
    PRIMARY KEY (ano, mes, produto)
);

CREATE TABLE gas_price.media_mes (
    ano int,
    mes int,
    dolar float,
    diesel float,
    diesel_s10 float,
    etanol float,
    gasolina float,
    gnv float,
    PRIMARY KEY ((ano, mes))
);

