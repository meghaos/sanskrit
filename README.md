# SanskritLang

SanskritLang is a programming language based on Sanskrit, designed for learning and implementing basic programming concepts. This language supports arithmetic operations, variable assignments, printing, comparisons, conditional statements, loops, string literals, and block statements.

## Features

### Arithmetic Operations
- **Addition**: `योजयति`
- **Subtraction**: `वियोजयति`
- **Multiplication**: `गुणयति`
- **Division**: `विभजति`

Example:
```sanskrit
परिवर्तन(a, 10)
परिवर्तन(b, 20)
प्रदर्शयति(योजयति(a, b))  # 30
प्रदर्शयति(वियोजयति(b, a))  # 10
प्रदर्शयति(गुणयति(a, b))  # 200
प्रदर्शयति(विभजति(b, a))  # 2.0

#### Variable Assignment
Use परिवर्तन to assign values to variables.
Example:

```sanskrit
Copy code
परिवर्तन(x, 5)
Printing
Use प्रदर्शयति to print values.

Example:

```sanskrit
Copy code
परिवर्तन(x, 5)
प्रदर्शयति(x)  # Prints 5

Comparison Operations
Equal to: ==
Not equal to: !=
Less than: <
Greater than: >
Less than or equal to: <=
Greater than or equal to: >=

Example:

```sanskrit
Copy code
परिवर्तन(x, 15)
परिवर्तन(y, 10)
यदि (x == y) प्रदर्शयति("x == y") अन्यथा प्रदर्शयति("x != y")
यदि (x != y) प्रदर्शयति("x != y")

Conditional Statements
Use यदि for if and अन्यथा for else.

Example:

```sanskrit
Copy code
परिवर्तन(x, 15)
परिवर्तन(y, 10)
यदि (x > y) प्रदर्शयति("x > y")
अन्यथा प्रदर्शयति("x <= y")

Loops
Use यावत् for while loops.

Example:

```sanskrit
Copy code
परिवर्तन(i, 1)
यावत् (i <= 5) {
    प्रदर्शयति(i)
    परिवर्तन(i, योजयति(i, 1))
}

String Literals
Strings are enclosed in double quotes.

Example:

```sanskrit
Copy code
परिवर्तन(message, "Hello, World!")
प्रदर्शयति(message)

Block Statements
Group multiple statements within {}.

Example:

sanskrit
Copy code
परिवर्तन(x, 1)
यावत् (x <= 5) {
    प्रदर्शयति(x)
    परिवर्तन(x, योजयति(x, 1))
}

Comprehensive Example
Here is a comprehensive example using all the features:

sanskrit
Copy code
परिवर्तन(x, 5)
परिवर्तन(y, 10)
परिवर्तन(z, योजयति(x, y))
प्रदर्शयति(z)  # 15
प्रदर्शयति(वियोजयति(y, x))  # 5
प्रदर्शयति(गुणयति(x, y))  # 50
प्रदर्शयति(विभजति(y, x))  # 2.0

यदि (x <= y) प्रदर्शयति(x) अन्यथा प्रदर्शयति(y)  # 5
यदि (x >= 5) प्रदर्शयति("x >= 5")  # "x >= 5"

यावत् (x <= 10) {
    परिवर्तन(x, योजयति(x, 1))
}
प्रदर्शयति(x)  # 11

Installation
Clone the repository:

bash
Copy code
git clone https://github.com/meghaos/Sanskrit.git
cd SanskritLang
Ensure you have Python 3 installed.

Run the interpreter:

bash
Copy code
python interpreter.py
Usage
Write your SanskritLang code in a file named test.s.

Run the interpreter:

bash
Copy code
python interpreter.py
The output will be printed to the console.

Contribution
Feel free to contribute to this project by submitting issues or pull requests. Any contributions are welcome!

License
This project is licensed under the MIT License.