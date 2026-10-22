using System.Numerics;

namespace Quantum;

internal abstract class Program
{
    private static void Main()
    {
        var I = Complex.ImaginaryOne;

        Complex[,] a =
        {
            { -9, 3 * I },
            { -1 * I, 7 }
        };

        Complex[,] b =
        {
            { 5 * I, 6 * I },
            { 20, 8 }
        };

        Console.WriteLine("Inner Product:");
        QuantumMath.PrintVector(new[]
        {
            QuantumMath.InnerProduct(
                new[] { a[0, 0], a[0, 1] },
                new[] { b[0, 0], b[0, 1] }
            )
        });

        Console.WriteLine("Outer Product:");
        QuantumMath.PrintMatrix(QuantumMath.OuterProduct(new[] { a[0, 0], a[1, 0] }, new[] { b[0, 0], b[1, 0] }));
        
        Console.WriteLine("Matrix Multiplication:");
        QuantumMath.PrintMatrix(QuantumMath.MatrixProduct(a, b));
        
        Console.WriteLine("Tensor Product:");
        QuantumMath.PrintMatrix(QuantumMath.TensorProduct(a, b));

        Console.ReadKey();
    }
}