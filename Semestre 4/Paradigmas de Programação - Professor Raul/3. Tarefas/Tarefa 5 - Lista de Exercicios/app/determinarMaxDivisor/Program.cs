using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace determinarMaxDivisor
{
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
}
