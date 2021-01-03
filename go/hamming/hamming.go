// Package hamming calculate the hamming distance between two DNA strands
package hamming

import "errors"

// Distance calculate the hamming distance
func Distance(a, b string) (int, error) {

	ar, br := []rune(a), []rune(b)

	if len(ar) != len(br) {
		return 0, errors.New("lengths are not equal")
	}

	count := 0
	for n := range ar {
		if ar[n] != br[n] {
			count++
		}
	}
	return count, nil
}
