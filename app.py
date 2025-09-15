from flask import Flask, render_template, request
import math

app = Flask(__name__)

class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None
    
    def is_empty(self):
        return len(self.items) == 0

class ScientificCalculator:
    def __init__(self):
        self.stack = Stack()
    
    def evaluate(self, expression):
        tokens = expression.split()
        for token in tokens:
            if token in ('+', '-', '*', '/', '^'):
                b = float(self.stack.pop())
                a = float(self.stack.pop())
                if token == '+':
                    self.stack.push(a + b)
                elif token == '-':
                    self.stack.push(a - b)
                elif token == '*':
                    self.stack.push(a * b)
                elif token == '/':
                    self.stack.push(a / b)
                elif token == '^':
                    self.stack.push(a ** b)
            elif token == 'sin':
                a = float(self.stack.pop())
                self.stack.push(math.sin(math.radians(a)))
            elif token == 'cos':
                a = float(self.stack.pop())
                self.stack.push(math.cos(math.radians(a)))
            elif token == 'tan':
                a = float(self.stack.pop())
                self.stack.push(math.tan(math.radians(a)))
            elif token == 'log':
                a = float(self.stack.pop())
                self.stack.push(math.log10(a))
            else:
                self.stack.push(token)
        
        return self.stack.pop()

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        expression = request.form['expression']
        calc = ScientificCalculator()
        try:
            result = calc.evaluate(expression)
        except Exception as e:
            result = f"Error: {str(e)}"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
