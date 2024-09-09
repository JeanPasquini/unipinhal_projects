# AULA CRIAR UM BANCO DE DADOS COM REGRAS DE NORMALIZAÇÃO PT.2

- Aula referente ao dia: 03/09/2024 

## DESCRIÇÃO:

Criar um banco de dados no MySQL Workbench. Nesse projeto estamos criando um banco de dados para tratar dados
com regras de padronizações.

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

Nessa parte concluimos as seguintes tarefas:

1. Criar tabela de 'vendas'
2. Adicionamos a relação de FOREIGN KEY ('Chave Estrangeira') para a coluna 'num_nf' na tabela 'vendas'
3. Inserimos dados de exemplo para testar o FOREIGN KEY na tabela 'notas_fiscais'
4. Inserimos dados de exemplos na tabela 'vendas' utilizando a FOREIGN KEY

### Códigos principais:

``` SQL
    CREATE TABLE `banco01`.`vendas` (
    `num_nf` INT(11) NOT NULL,
    `cod_prod` INT(11) NOT NULL,
    `qtd_vendas` DOUBLE NOT NULL,
    `total_vend` DOUBLE NOT NULL,
    PRIMARY KEY (`num_nf`, `cod_prod`));
    --CÓDIGO DE CRIAÇÃO DA SEGUNDA TABELA QUE UTILIZAMOS NO PROJETO
    --OBSERVAÇÃO: CRIAMOS A TABELA PARTINDO DA FERRAMENTA DO MYSQL WORKBENCH (VISUAL SEM CÓDIGO)
```

``` SQL
    INSERT INTO vendas(num_nf, cod_prod, qtd_vendas, total_vend) VALUES ('2222', '5555', '150', '1500')
    --CÓDIGO PARA INSERIR DADOS EM UMA TABELA
    --EXEMPLO DO CÓDIGO DADO EM AULA
```

``` SQL
    INSERT INTO notas_fiscais(num_nf, serie, data_emi, cod_clie, total_ger) VALUES ('2222', '22', '03092024', '1234', '10000');
	--CÓDIGO PARA INSERIR DADOS EM UMA TABELA
    --EXEMPLO DO CÓDIGO DADO EM AULA
```

``` SQL
    ALTER TABLE `banco01`.`vendas` 
    ADD CONSTRAINT `fk_num_nf`
    FOREIGN KEY (`num_nf`)
    REFERENCES `banco01`.`notas_fiscais` (`num_nf`)
    ON DELETE NO ACTION
    ON UPDATE RESTRICT;
    --CÓDIGO PARA DEIXAR UMA CHAVE ESTRANGEIRA DEFINIDA
    --OBSERVAÇÃO: FIZEMOS ESSA ALTERAÇÃO NA FERRAMENTA DO MYSQL WORKBENCH (VISUAL SEM CÓDIGO)
```

## EXTRA

Atividade em exibição junto com o arquivo do SQL. 
