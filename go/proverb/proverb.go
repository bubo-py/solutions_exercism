// Package proverb generates bunch of proverb lines with given words
package proverb

import "fmt"

// Proverb generates bunch of proverb lines with given words
func Proverb(rhyme []string) []string {
	var result []string
	var end string

	if len(rhyme) != 0 && len(rhyme) != 1 {
		for i := 0; i < len(rhyme)-1; i++ {
			line := fmt.Sprintf("For want of a %v the %v was lost.", rhyme[i], rhyme[i+1])
			result = append(result, line)
		}
	}

	if len(rhyme) != 0 {
		end = fmt.Sprintf("And all for the want of a %v.", rhyme[0])
		result = append(result, end)
	}
	return result
}
