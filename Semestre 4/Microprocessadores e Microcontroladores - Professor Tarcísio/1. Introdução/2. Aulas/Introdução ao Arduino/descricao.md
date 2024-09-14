# AULA INTRODUÇÃO AO ARDUINO

- Aula referente ao dia: 21/08/2024 

## DESCRIÇÃO:

Primeiros passos para utilizar o Arduino, descrição de seus componentes e tipos de placa.

### Informações:

- Link de estudo: https://ead.unipinhal.edu.br/pluginfile.php/9484/mod_folder/content/0/5.1.%20Introdu%C3%A7%C3%A3o%20ao%20Arduino.pdf?forcedownload=1

- Link de estudo 2: https://ead.unipinhal.edu.br/pluginfile.php/9484/mod_folder/content/0/5.2.%20Introdu%C3%A7%C3%A3o%20%C3%A0%20pr%C3%A1tica%20com%20a%20placa%20Arduino%20Uno.pdf?forcedownload=1

- Link atividade no moodle: N/A

- Data lançada no moodle: N/A
- Data término de envio: N/A


## CONFIGURAÇÃO DO AMBIENTE DE DESENVOLVIMENTO 

- Linguagem Utilizada: Arduino (C++)
- IDE: Tinkercad, Arduino

## PROJETO CONCLUÍDO

### Introdução:

Inicio dos conhecimentos da placa Arduino, introduzimos a uma atividade prática que nos fez desenvolver um
semáforo para conhecer como os pinos inputs e outputs funcionam.

Além disso para testarmos e fazermos a programação da placa utilizamos a IDE Tinkercad, onde está disponível
no link abaixo:

https://www.tinkercad.com

### Códigos principais:

``` c++
    int brightness = 0;

    int contador = 0;

    void setup()
    {
    pinMode(11, OUTPUT);
    pinMode(12, OUTPUT);
    pinMode(13, OUTPUT);
    }

    void loop()
    {
    digitalWrite(11, LOW);
    digitalWrite(12, LOW);
    digitalWrite(13, LOW);
    contador = 0;
    while (contador >= 0) {
        digitalWrite(13, HIGH);
        delay(7000); // Wait for 7000 millisecond(s)
        digitalWrite(13, LOW);
        digitalWrite(12, HIGH);
        delay(2000); // Wait for 2000 millisecond(s)
        digitalWrite(12, LOW);
        digitalWrite(11, HIGH);
        delay(5000); // Wait for 5000 millisecond(s)
        digitalWrite(11, LOW);
    }
    }
```

## EXTRA

Atividade em exibição junto com o arquivo do codigo fonte do arduino. 
