using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace determinarNumPrimos
{
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
}
