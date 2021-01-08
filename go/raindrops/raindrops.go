// Package raindrops convert a number into raindrop sounds string
package raindrops

import "strconv"

// Convert converts the int
func Convert(number int) string {
	converted := ""
	if number%3 == 0 {
		converted += "Pling"
	}
	if number%5 == 0 {
		converted += "Plang"
	}
	if number%7 == 0 {
		converted += "Plong"
	}

	if converted == "" {
		return strconv.Itoa(number)
	}

	return converted

}
