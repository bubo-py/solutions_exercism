package twofer

import "fmt"

func helpingFunc(name string) string {
	if name == "" {
		return "One for you, one for me."
	}
	return fmt.Sprintf("One for %v, one for me.", name)
}

func ShareWith(name string) string {
	return helpingFunc(name)
}
