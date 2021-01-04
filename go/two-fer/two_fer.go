// Package twofer is for formatting the sentence
package twofer

import "fmt"

func helpingFunc(name string) string {
	if name == "" {
		return "One for you, one for me."
	}
	return fmt.Sprintf("One for %v, one for me.", name)
}

// ShareWith returns a string with a given name
func ShareWith(name string) string {
	return helpingFunc(name)
}
