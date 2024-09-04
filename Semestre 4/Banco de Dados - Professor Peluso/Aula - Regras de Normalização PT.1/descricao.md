# AULA CRIAR UM BANCO DE DADOS COM REGRAS DE NORMALIZAÇÃO PT.1

- Aula referente ao dia: 27/08/2024 

## DESCRIÇÃO:

Criar um banco de dados no MySQL Workbench. Nesse projeto estamos criando um banco de dados para tratar dados
com regras de normalização.

### Informações:

- Link de estudo: https://ead.unipinhal.edu.br/mod/resource/view.php?id=57081

- Link atividade no moodle: N/A

- Data lançada no moodle: N/A
- Data término de envio: N/A


## CONFIGURAÇÃO DO AMBIENTE DE DESENVOLVIMENTO 

- Linguagem Utilizada: SQL
- IDE: MySQL Workbench

## PROJETO CONCLUÍDO

### Introdução:

A ideia principal foi mostrar como é a criação de um banco de dados e inserir dados através da ferramenta (software) MySQL Worbench.
Contudo inserimos alguns códigos feitos a mão e outros pela própria ferramenta do MySQL.

1. Criar um banco chamado 'banco01'.
2. Criar a tabela 'notas_fiscais'.
3. Inserimos dados de exemplo na tabela 'notas_fiscais'
4. Visualizamos os dados na tabela 'notas_fiscais'

### Códigos principais:

``` SQL
    CREATE SCHEMA `banco01` ;
	--CÓDIGO PARA CRIAR BANCO DE DADOS
```

``` SQL
    CREATE TABLE `banco01`.`notas_fiscais` (
    `num_nf` INT(11) NOT NULL,
    `serie` INT(11) NOT NULL,
    `data_emi` INT(11) NOT NULL,
    `cod_clie` INT(11) NOT NULL,
	`total_ger` DOUBLE NOT NULL,
    PRIMARY KEY (`num_nf`));
    --CÓDIGO DE CRIAÇÃO DA PRIMEIRA TABELA QUE UTILIZAMOS NO PROJETO
    --OBSERVAÇÃO: CRIAMOS A TABELA PARTINDO DA FERRAMENTA DO MYSQL WORKBENCH (VISUAL SEM CÓDIGO)
```

``` SQL
    INSERT INTO notas_fiscais(num_nf, serie, data_emi, cod_clie, total_ger) VALUES ('1111', '11', '27092024', '1234', '10000')
    --CÓDIGO PARA INSERIR DADOS EM UMA TABELA
    --EXEMPLO DO CÓDIGO DADO EM AULA
```

``` SQL
    SELECT * FROM notas_fiscais
    --CÓDIGO PARA MOSTRAR OS DADOS EM UMA TABELA
```

## EXTRA

Atividade em exibição junto com o arquivo do SQL. 
