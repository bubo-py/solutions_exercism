// Package isogram is for determining if a word or phrase is an isogram
package isogram

import "strings"

// IsIsogram checks if given word is an isogram
func IsIsogram(word string) bool {
	r := strings.NewReplacer(" ", "", "-", "")
	word = strings.ToLower(r.Replace(word))
	wasBefore := make(map[rune]int)

	for _, n := range word {
		wasBefore[n]++
	}

	for _, v := range wasBefore {
		if v > 1 {
			return false
		}
	}
	return true
}
