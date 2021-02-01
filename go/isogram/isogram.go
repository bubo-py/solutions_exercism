// Package isogram is for determining if a word or phrase is an isogram
package isogram

import "strings"

// IsIsogram checks if given word is an isogram
func IsIsogram(word string) bool {
	r := strings.NewReplacer(" ", "", "-", "")
	word = strings.ToLower(r.Replace(word))

	for _, v := range word {
		if strings.Count(word, string(v)) > 1 {
			return false
		}
	}

	return true
}
