package diffsquares

import "math"

func SquareOfSum(n int) int {
    var sum int = 0
    for x := 0; x <= n; x++ {
        sum += x
    }
    return int(math.Pow(float64(sum), 2))
}

func SumOfSquares(n int) int {
    var squaredSum float64 = 0
    for x := 0; x <= n; x++ {
        squaredSum += math.Pow(float64(x), 2)
    }
    return int(squaredSum)
}

func Difference(n int) int {
    return SquareOfSum(n) - SumOfSquares(n)
}
