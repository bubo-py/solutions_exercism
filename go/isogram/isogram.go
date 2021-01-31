// Package isogram is for determining if a word or phrase is an isogram
package isogram

import "strings"

// IsIsogram checks if given word is an isogram
func IsIsogram(word string) bool {
	r := strings.NewReplacer(" ", "", "-", "")
	word = strings.ToLower(r.Replace(word))

	var charCount []int

	for _, v := range(word) {
		charCount = append(charCount, strings.Count(word, string(v)))
	}

	for _, v := range charCount {
		if v > 1 {
			return false
		}
	}
	return true
}
