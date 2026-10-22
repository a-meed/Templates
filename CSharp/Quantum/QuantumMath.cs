using System.Numerics;

namespace Quantum;

public class QuantumMath
{
    // Inner Product: <a|b>
    public static Complex InnerProduct(Complex[] a, Complex[] b)
    {
        if (a.Length != b.Length)
            throw new ArgumentException("Vectors must have the same length.");

        var result = Complex.Zero;

        for (var i = 0; i < a.Length; i++)
            result += Complex.Conjugate(a[i] * b[i]);

        return result;
    }

    // Outer Product: |a><b|
    public static Complex[,] OuterProduct(Complex[] a, Complex[] b)
    {
        var result = new Complex[a.Length, b.Length];

        for (var i = 0; i < a.Length; i++)
        {
            for (var j = 0; j < b.Length; j++)
            {
                result[i, j] = a[i] * Complex.Conjugate(b[j]);
            }
        }

        return result;
    }

    // Matrix Multiplication: C[i,j] = Σ A[i,k] * B[k,j]
    public static Complex[,] MatrixProduct(Complex[,] a, Complex[,] b)
    {
        var rowA = a.GetLength(0);
        var colsA = a.GetLength(1);
        var rowB = b.GetLength(0);
        var colsB = b.GetLength(1);

        if (colsA != rowB)
            throw new ArgumentException("A's columns must equal B's rows.");

        var result = new Complex[rowA, colsB];

        for (var i = 0; i < rowA; i++)
        {
            for (var j = 0; j < colsB; j++)
            {
                for (var k = 0; k < colsA; k++)
                {
                    result[i, j] += a[i, j] * b[k, j];
                }
            }
        }

        return result;
    }

    // Tensor Product: A ⊗ B (Kronecker product)
    public static Complex[,] TensorProduct(Complex[,] a, Complex[,] b)
    {
        var rowsA = a.GetLength(0);
        var colsA = a.GetLength(1);
        var rowsB = b.GetLength(0);
        var colsB = b.GetLength(1);

        var result = new Complex[rowsA * rowsB, colsA * colsB];

        for (var i = 0; i < rowsA; i++)
        {
            for (var j = 0; j < colsA; j++)
            {
                for (var k = 0; k < rowsB; k++)
                {
                    for (var l = 0; l < colsB; l++)
                    {
                        result[i * rowsB + k, j * colsB + l] = a[i, j] * b[k, l];
                    }
                }
            }
        }

        return result;
    }

    public static void PrintMatrix(Complex[,] matrix)
    {
        for (var i = 0; i < matrix.GetLength(0); i++)
        {
            for (var j = 0; j < matrix.GetLength(1); j++)
            {
                Console.Write($"{matrix[i, j],15}");
            }

            Console.WriteLine();
        }
    }

    public static void PrintVector(Complex[] vector) => Console.WriteLine("[" + string.Join(", ", vector) + "]");
}