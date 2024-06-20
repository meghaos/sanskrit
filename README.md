# Sanskrit Programming Language

This is a simple programming language based on Sanskrit, designed to demonstrate basic programming constructs such as arithmetic operations, conditionals, loops, and more. This project came from the claim that NASA has conducted research on Sanskrit in the context of AI is widely spread. While it cannot be definitively confirmed, In 1985, NASA associate scientist Rick Briggs published a research paper in the spring issue of Artificial Intelligence magazine entitled “Vedic Science — ‘Knowledge Representation in Sanskrit and Artificial Intelligence.’” The article argued that natural languages are the best option to be converted into the computing program for robotic control and artificial intelligence technology.

 Briggs also argued that Sanskrit is particularly well-suited for this task because of its highly structured grammar and its ability to express complex ideas in a concise and unambiguous way He even went so far as to suggest that Sanskrit could one day be used as the primary programming language for artificial intelligence.

For example, in 2017, a team of researchers at the Indian Institute of Technology Bombay developed a Sanskrit natural language processing toolkit called SanskritNLP. This toolkit can be used to perform a variety of natural language processing tasks, such as text classification, sentiment analysis, and machine translation.

In 2018, a team of researchers at the University of California, Berkeley developed a Sanskrit-English machine translation system that was shown to be more accurate than existing state-of-the-art systems. 

These are just a few examples of the growing interest in using Sanskrit for natural language processing and artificial intelligence applications. It is possible that Sanskrit could one day be used in coding as it is more efficient in complex algorithms as well but more research is needed to develop the necessary technologies. This is my initiative to explore programming concepts using the ancient language of Sanskrit. I invite all coding enthusiat

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
- **String Literals**: `""` Strings are enclosed in double quotes.
- **Block Statements**: `{}`

## Installation

To run the Sanskrit programming language interpreter, follow these steps:

1. **Clone the repository**:
    ```sh
    git clone https://github.com/meghaos/Sanskrit.git
    cd Sanskrit
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
```sanskrit
परिवर्तन(a, 10)
परिवर्तन(b, 20)
प्रदर्शयति(योजयति(a, b))  # 30
प्रदर्शयति(वियोजयति(b, a))  # 10
प्रदर्शयति(गुणयति(a, b))  # 200
प्रदर्शयति(विभजति(b, a))  # 2.0
```

#### Comparisons and Conditionals
```sanskrit
परिवर्तन(x, 15)
परिवर्तन(y, 10)
यदि (x == y) प्रदर्शयति("x == y") अन्यथा प्रदर्शयति("x != y")  # x != y
यदि (x != y) प्रदर्शयति("x != y")  # x != y
यदि (x > y) प्रदर्शयति("x > y")  # x > y
यदि (x < y) प्रदर्शयति("x < y") अन्यथा प्रदर्शयति("x >= y")  # x >= y
यदि (x >= 15) प्रदर्शयति("x >= 15")  # x >= 15
यदि (y <= 10) प्रदर्शयति("y <= 10")  # y <= 10
```
#### Loops
```sanskrit
परिवर्तन(i, 1)
यावत् (i <= 5) {
    प्रदर्शयति(i)
    परिवर्तन(i, योजयति(i, 1))
}
```
#### String Literals and Complex Conditions
```sanskrit
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
```
#### Running the Interpreter
Run your interpreter script:
```sh
python interpreter.py
```

Make sure the test.s file contains your Sanskrit code. The interpreter will read this file, parse the code, and execute it.

License:
This project is licensed under the GNU General Public License Version 2. See the LICENSE file for details.

Contributing:
Contributions are welcome! Please create a pull request with your changes and ensure that your code follows the existing coding style.

Acknowledgements:
This project is inspired by the rich linguistic heritage of Sanskrit and is designed as a fun way to learn and explore programming concepts.