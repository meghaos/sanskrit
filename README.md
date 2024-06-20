# Sanskrit Programming Language

This is a simple programming language based on Sanskrit, designed to demonstrate basic programming constructs such as arithmetic operations, conditionals, loops, and more. This project is a learning tool and a fun way to explore programming concepts using the ancient language of Sanskrit.

## Features

- **Arithmetic Operations**:
  - Addition: `योजयति`
  - Subtraction: `वियोजयति`
  - Multiplication: `गुणयति`
  - Division: `विभजति`
- **Variable Assignment**: `परिवर्तन`
- **Printing**: `प्रदर्शयति`
- **Comparison Operations**:
  - Equal to: `==`
  - Not equal to: `!=`
  - Less than: `<`
  - Greater than: `>`
  - Less than or equal to: `<=`
  - Greater than or equal to: `>=`
- **Conditional Statements**: `यदि` and `अन्यथा`
- **Loops**: `यावत्`
- **String Literals**
- **Block Statements**: `{}`

## Installation

To run the Sanskrit programming language interpreter, follow these steps:

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/SanskritLang.git
    cd SanskritLang
    ```

2. **Create and activate a virtual environment**:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

Create a file named `test.s` and write your Sanskrit code in it. Then run the interpreter to execute your code.

### Example Code

Here are some example codes to demonstrate the features of the language:

#### Arithmetic Operations

परिवर्तन(a, 10)
परिवर्तन(b, 20)
प्रदर्शयति(योजयति(a, b))  # 30
प्रदर्शयति(वियोजयति(b, a))  # 10
प्रदर्शयति(गुणयति(a, b))  # 200
प्रदर्शयति(विभजति(b, a))  # 2.0

##### Comparisons and Conditionals

परिवर्तन(x, 15)
परिवर्तन(y, 10)
यदि (x == y) प्रदर्शयति("x == y") अन्यथा प्रदर्शयति("x != y")  # x != y
यदि (x != y) प्रदर्शयति("x != y")  # x != y
यदि (x > y) प्रदर्शयति("x > y")  # x > y
यदि (x < y) प्रदर्शयति("x < y") अन्यथा प्रदर्शयति("x >= y")  # x >= y
यदि (x >= 15) प्रदर्शयति("x >= 15")  # x >= 15
यदि (y <= 10) प्रदर्शयति("y <= 10")  # y <= 10

###### Loops

परिवर्तन(i, 1)
यावत् (i <= 5) {
    प्रदर्शयति(i)
    परिवर्तन(i, योजयति(i, 1))
}

####### String Literals and Complex Conditions

परिवर्तन(x, 5)
प्रदर्शयति("Initial value of x is:")
प्रदर्शयति(x)  # 5

परिवर्तन(y, 10)
यदि (x < y) {
    प्रदर्शयति("x is less than y")
    परिवर्तन(x, योजयति(x, y))  # x = x + y = 15
}

प्रदर्शयति("New value of x is:")
प्रदर्शयति(x)  # 15

Running the Interpreter
Run your interpreter script:

sh
Copy code
python interpreter.py
Make sure the test.s file contains your Sanskrit code. The interpreter will read this file, parse the code, and execute it.

License
This project is licensed under the GNU General Public License Version 2. See the LICENSE file for details.

Contributing
Contributions are welcome! Please create a pull request with your changes and ensure that your code follows the existing coding style.

Acknowledgements
This project is inspired by the rich linguistic heritage of Sanskrit and is designed as a fun way to learn and explore programming concepts.