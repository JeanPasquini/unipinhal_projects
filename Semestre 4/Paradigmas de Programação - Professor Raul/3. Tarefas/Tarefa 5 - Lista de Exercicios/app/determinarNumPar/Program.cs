using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace determinarNumPar
{
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
}
