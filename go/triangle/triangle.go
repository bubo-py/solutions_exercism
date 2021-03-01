// Package triangle determines a type of triangle
package triangle

import "math"

// Kind is a type of triangle
type Kind string

const (
	NaT = "not a triangle"
	Equ = "equilateral"
	Iso = "isosceles"
	Sca = "scalene"
)

// KindFromSides determines a type of triangle
func KindFromSides(a, b, c float64) Kind {
	var k Kind
	if isValidTriangle(a, b, c) {
		switch {
		case a == b && b == c:
			k = Equ
		case a == b || a == c || b == c:
			k = Iso
		case a != b && a != c && b != c:
			k = Sca
		}
	} else {
		k = NaT
	}
	return k
}

// check if given sides can make a valid triangle
func isValidTriangle(a, b, c float64) bool {
	if isValidNumber(a) && isValidNumber(b) && isValidNumber(c) {
		if a > 0 && b > 0 && c > 0 {
			if a <= b+c && b <= c+a && c <= a+b {
				return true
			}
		}
	}
	return false
}

// check if number is valid in all infinity cases
func isValidNumber(number float64) bool {
	return !math.IsInf(number, 1) && !math.IsInf(number, -1) && !math.IsNaN(number)
}
