package luhn

import (
    "strings"
    "strconv"
)

func Valid(str string) bool {
    // Cleanup
	runes := []rune(strings.ReplaceAll(str, " ", ""))

    // Initial values and length validation
	length := len(runes)
    sum := 0

	if length < 2 {
		return false
	}

	for i := 0; i < length; i++ {
		num, err := strconv.Atoi(string(runes[length-1-i]))
		if err != nil {
			return false
		}

		if i % 2 == 1 {
			if num * 2 >= 9 {
				sum += (num * 2) - 9
			} else {
				sum += num * 2
			}
		} else {
			sum += num
		}
	}

	return sum % 10 == 0
}
