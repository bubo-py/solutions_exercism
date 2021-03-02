// Package diffsquares calculates the difference between definite squares
package diffsquares

// SquareOfSum calculates the square of the sum
func SquareOfSum(n int) int {
	result := (n + 1) * n / 2
	return result * result
}

// SumOfSquares calculates the sum of the squares
func SumOfSquares(n int) int {
	result := n * (n+1) * (n * 2 + 1) / 6
	return result
}

// Difference calculates the difference between squares, using above functions
func Difference(n int) int {
	return SquareOfSum(n) - SumOfSquares(n)
}
