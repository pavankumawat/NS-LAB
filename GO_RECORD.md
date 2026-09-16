# LOYOLA ACADEMY DEGREE & PG COLLEGE

**Old Alwal, Secunderabad-500010**  
*(An Autonomous Degree College Affiliated to Osmania University)*  
**Accredited By NAAC with ‘A’ Grade College with Potential for Excellence**

---

# Department of Cyber Security

## Practical Record in Go-Language Programming

### Certificate

This is to certify that this is the bonfire record of the work done during the practical lab for the **5th Semester** of the academic year **2026-2027**.

| Name | Class | UID |
|---|---|---|
| | | |

| Internal | External | Principal |
|---|---|---|
| | | |

---

# INDEX

| S.No | Topic | Page No. | Date | Signature |
|---:|---|---:|---|---|
| 1 | Installing and Setting Environment for GoLang | | | |
| 2 | Count Digits in a Number | | | |
| 3 | Product of Digits in a Number | | | |
| 4 | Positive and Negative Numbers in an Array | | | |
| 5 | ArrayItem in Even Index Position | | | |
| 6 | ArrayItem in ODD Index Position | | | |
| 7 | Sum of Each Row and Column of a Matrix | | | |
| 8 | Sum of Matrix Diagonal | | | |
| 9 | ASCII values of String Characters | | | |
| 10 | Concatenate Two Strings | | | |
| 11 | String Length, First Character, Last Character | | | |
| 12 | Demonstrate GoStructure | | | |

---

# 1. Installing and Setting Environment for GoLang

### Step 1

Go to <https://go.dev/dl/> to access the official website. Download the latest version of Go’s Windows installer according to your system.

### Step 2: Run Installer

Run the installer and select **“Next”** to allow the installer to install the Go-Language in your device.

### Step 3

Accept the End-User License Agreement and click on the **“CheckButton”** to accept the Agreement and then click on the **“Next”** button.

### Step 4: Choose Installation Location

By default, Go will be installed in `C:\Go`. The default path can be changed, but it’s preferable to leave it alone. To proceed, click the **“Next”** button.

### Step 5

Install the Go-Language by clicking on the **“Install”** button and wait for the installation then click on **“Finish”** button to complete the installation.

### Output

*Installation completed successfully.*

---

# 2. Count Digits in a Number

### Program

```go
package main
import "fmt"
func main() {
var n int
count := 0
fmt.Print("enter a number:-")
fmt.Scan(&n)
if n == 0 {
count = 1
}
for n!= 0 {
n /= 10
count++
}
fmt.Printf("number of digit %d\n", count)
}
```

### Output

```text
```

---

# 3. Products of Digits in a Number

### Program

```go
package main
import "fmt"
func main() {
var n, r, p int
fmt.Print("enter the number:")
fmt.Scanf("%d", &n)
for p = 1; n > 0; n = n / 10 {
r = n % 10
p = p * r
}
fmt.Println("Product:", p)
}
```

### Output

```text
```

---

# 4. Positive and Negative Numbers in an Array

### Program

```go
package main
import "fmt"
func main() {
 var a [5]int
 var count_pos int = 0
 var count_neg int = 0
 var i int
 fmt.Print("enter the values:-")
 for i = 0; i < 5; i++ {
 fmt.Scanf("%d/n", &a[i])
 }
 for i = 0; i < 5; i++ {
 if a[i] >= 0 {
 count_pos++
 } else {
 count_neg++
 }
 }
 fmt.Println("number of positive elements", count_pos)
 fmt.Println("number of negative elements", count_neg)
}
```

### Output

```text
```

---

# 5. ArrayItem in Even index Position

### Program

```go
package main
import "fmt"
func main() {
 var a [6]int
 var i int
 fmt.Println("Enter elements into the array:")
 for i = 0; i < 6; i++ {
 fmt.Scanf("%d\n", &a[i])
 }
 fmt.Println("THE EVEN INDEX ELEMENTS ARE:")
 for i = 0; i < 6; i = i + 2 {
 fmt.Printf("%d\n", a[i])
 }
}
```

### Output

```text
```

---

# 6. ArrayItem in Odd index Position

### Program

```go
package main
import "fmt"
func main() {
var a [6]int
var i int
fmt.Println("Enter elements into the array:")
for i = 0; i < 6; i++ {
fmt.Scanf("%d\n", &a[i])
}
fmt.Println("THE ODD INDEX ELEMENTS ARE:")
for i = 1; i < 6; i = i + 2 {
fmt.Printf("%d\n", a[i])
}
}
```

### Output

```text
```

---

# 7. Sum of Each Row and Column of a Matrix

### Program

```go
package main
import "fmt"
func main() {
var a [3][3]int
var i int
var j int
var row_sum int = 0
var col_sum int = 0
fmt.Println("Enter elements in an array:")
for i = 0; i < 3; i++ {
for j = 0; j < 3; j++ {
fmt.Scan(&a[i][j])
}
}
fmt.Println("Matrix:")
for i = 0; i < 3; i++ {
for j = 0; j < 3; j++ {
fmt.Printf("%d\t", a[i][j])
}
fmt.Println()
}
fmt.Println("\nRow sums:")
for i = 0; i < 3; i++ {
row_sum = 0
for j = 0; j < 3; j++ {
row_sum = row_sum + a[i][j]
}
fmt.Println("Sum of row", i+1, ":", row_sum)
}
fmt.Println("\nColumn sums:")
for i = 0; i < 3; i++ {
col_sum = 0
for j = 0; j < 3; j++ {
col_sum = col_sum + a[j][i]
}
fmt.Println("Sum of column", i+1, ":", col_sum)
}
}
```

### Output

```text
```

---

# 8. Sum of Matrix Diagonal

### Program

```go
package main
import "fmt"
func main(){
var a[3][3] int
var i int
var j int
var diag_sum int = 0
fmt.Println("Enter elements in an array:")
for i=0;i<3;i++ {
for j=0;j<3;j++ {
fmt.Scanf("%d\n",&a[i][j])
}
}
for i=0;i<3;i++{
for j=0;j<3;j++{
fmt.Printf("%d\t",a[i][j])
}
fmt.Printf("\n")
}
for i=0; i<3;i++ {
diag_sum=diag_sum+a[i][i]
}
fmt.Println("Sum of diagonal:", diag_sum)
}
```

### Output

```text
```

---

# 9. ASCII Values of String Characters

### Program

```go
package main
import "fmt"
func getASCIIValues(str string)[]int{
asciiValues:=[]int{}
for _, char := range str {
asciiValues=append(asciiValues,int(char))
}
return asciiValues
}
func main(){
inputString:= "WELCOME TO GO LANGUAGE"
asciiValues:= getASCIIValues(inputString)
fmt.Println("Given String =",inputString)
fmt.Println("ASCIIValues =",asciiValues)
}
```

### Output

```text
```

---

# 10. Concat Two Strings

### Program

```go
package main
import (
"fmt"
"strings"
)
func main() {
var str1, str2 string
fmt.Print("Enter the first string:")
fmt.Scanln(&str1)
fmt.Print("Enter the second string:")
fmt.Scanln(&str2)
// Method 1: Using + operator
result1 := str1 + "" + str2
fmt.Println("Concatenated string (Method1):", result1)
// Method 2: Using fmt.Sprintf
result2 := fmt.Sprintf("%s %s", str1, str2)
fmt.Println("Concatenated string (Method2):", result2)
// Using strings.Join to concatenate
result := strings.Join([]string{str1, str2}, "")
fmt.Println(result)
}
```

### Output

```text
```

---

# 11. String Length, First Character, Last Character

### Program

```go
package main
import "fmt"
func main() {
var str string
fmt.Print("Enter a string: ")
fmt.Scanln(&str)
// Find the length of the string
length := len(str)
fmt.Println("Length of the string:", length)
// Extract the first character using array index
firstChar := str[0]
fmt.Printf("First character: %c\n", firstChar)
// Extract the last character using array index
lastChar := str[length-1]
fmt.Printf("Last character: %c\n", lastChar)
}
```

### Output

```text
```

---

# 12. Demonstrate Go Structure

### Program

```go
package main
import "fmt"
// Define the Student struct
type Student struct {
UID int
Name string
Class string
}
func main() {
// Create a new Student instance
student := Student{
UID: 26,
Name: "Daya",
Class: "DCSCS",
}
// Display the student details
fmt.Println("Student Details:")
fmt.Println("UID:", student.UID)
fmt.Println("Name:", student.Name)
fmt.Println("Class:", student.Class)
fmt.Printf("Student %+v", student)
}
```

### Output

```text
```

---

# End of Practical Record
