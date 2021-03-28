package luhn

import (
    "strings"
    "strconv"
)

func Valid (str string) bool {
    sum := 0
    n := 0
    str = strings.Replace(str, " ", "", -1)

    if _, err := strconv.Atoi(str); err == nil && len([]rune(str)) > 1 {
        for range str {
            toAdd, _ := strconv.Atoi(string(str[n]))
            sum += toAdd
            n += 2
        }
    }

    // if sum % 10 == 0 {
    //     return true
    // }
    return false
}
