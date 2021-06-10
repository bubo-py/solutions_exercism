// Package luhn checks whether or not a number is valid per the Luhn formula
package luhn

import (
	"strings"
	"unicode"
)

// Valid checks if given string is valid per the Luhn formula
func Valid(str string) bool {
	// Cleanup
	runes := []rune(strings.ReplaceAll(str, " ", ""))

	// Initial values and length validation
	sum := 0
	if len(runes) < 2 {
		return false
	}

	for double, i := false, len(runes)-1; i >= 0; double, i = !double, i-1 {

		// Check if the element is a number
		if !unicode.IsDigit(runes[i]) {
			return false
		}

		n := int(runes[i] - '0')

		if double {
			n *= 2
			if n > 9 {
				n -= 9
			}
		}
		sum += n
	}
	return sum%10 == 0
}
