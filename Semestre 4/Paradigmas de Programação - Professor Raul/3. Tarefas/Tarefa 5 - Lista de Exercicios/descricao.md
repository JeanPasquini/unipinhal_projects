# TAREFA 5 - LISTA DE EXERCÍCIOS

## DESCRIÇÃO:

Realizar as atividades com base na linguagem escolhida.

### Informações:

- Link no moodle: https://ead.unipinhal.edu.br/mod/assign/view.php?id=58819

- Data lançada no moodle: 19/09/2024 ❗
- Data término de envio: 26/09/2024 ⚠

## CONFIGURAÇÃO DO AMBIENTE DE DESENVOLVIMENTO 

- Linguagem Utilizada: C#
- IDE: Visual Studio 2022

## PROJETO CONCLUÍDO

### Introdução:

Realizar 3 códigos com as seguintes funções:

- Determinar quantos números são pares em uma sequência.
- Determinar o máximo divisor comum entre 2 números.
- Determinar quantos números são primos em uma sequência.

### Códigos principais:

``` C#
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Digite a quantidade de números (N): ");
            int N = int.Parse(Console.ReadLine());

            int countPares = 0;

            Console.WriteLine("Digite os números:");
            for (int i = 0; i < N; i++)
            {
                int numero = int.Parse(Console.ReadLine());
                if (numero % 2 == 0)
                {
                    countPares++;
                }
            }

            Console.WriteLine($"Quantidade de números pares: {countPares}");
            Console.ReadLine();
        }
    }
```

``` C#
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Digite o primeiro número inteiro positivo: ");
            int a = int.Parse(Console.ReadLine());

            Console.Write("Digite o segundo número inteiro positivo: ");
            int b = int.Parse(Console.ReadLine());

            int mdc = CalcularMDC(a, b);

            Console.WriteLine($"O máximo divisor comum entre {a} e {b} é: {mdc}");
            Console.ReadLine();
        }

        static int CalcularMDC(int a, int b)
        {
            while (b != 0)
            {
                int temp = b;
                b = a % b;
                a = temp;
            }
            return a;
        }
    }
```

``` C#
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Digite a quantidade de números (N): ");
            int N = int.Parse(Console.ReadLine());

            int countPrimos = 0;

            Console.WriteLine("Digite os números:");
            for (int i = 0; i < N; i++)
            {
                int numero = int.Parse(Console.ReadLine());
                if (EhPrimo(numero)) 
                {
                    countPrimos++;
                }
            }

            Console.WriteLine($"Quantidade de números primos: {countPrimos}");
            Console.ReadLine();
        }

        static bool EhPrimo(int numero)
        {
            if (numero <= 1) return false; 
            for (int i = 2; i <= Math.Sqrt(numero); i++)
            {
                if (numero % i == 0) return false; 
            }
            return true; 
        }
    }
```

## EXTRA

Programas em exibição dentro da pasta 'app'
