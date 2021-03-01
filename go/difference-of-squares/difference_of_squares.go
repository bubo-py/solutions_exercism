// Package diffsquares calculates the difference between definite squares
package diffsquares

import "math"

// SquareOfSum calculates the square of the sum
func SquareOfSum(n int) int {
    var sum int = 0
    for x := 0; x <= n; x++ {
        sum += x
    }
    return int(math.Pow(float64(sum), 2))
}

// SumOfSquares calculates the sum of the squares
func SumOfSquares(n int) int {
    var squaredSum float64 = 0
    for x := 0; x <= n; x++ {
        squaredSum += math.Pow(float64(x), 2)
    }
    return int(squaredSum)
}

// Difference calculates the difference between squares, using above functions
func Difference(n int) int {
    return SquareOfSum(n) - SumOfSquares(n)
}
