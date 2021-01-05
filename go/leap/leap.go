// Package leap reports if it is a leap year.
package leap

// IsLeapYear check whether year is a leap year or not
func IsLeapYear(year int) bool {
	if year%4 == 0 {
		if year%100 == 0 && year%400 != 0 {
			return false
		}
		return true
	}
	return false
}
