import math

def calculate_f(x):
    try:
        numerator = math.log(math.cos(x))
        denominator = 2 - (x**2 + 1)**(1/3)
        result = 4**(2*x) - (numerator / denominator)
        return result
    except ValueError as e:
        return f"Error: {e}"

# Приклад виклику функції
x_value = 1  # Заміни на необхідне значення
print(f"f({x_value}) = {calculate_f(x_value)}")
import math

def calculate_Z(x, y, m):
    try:
        term1 = math.sqrt(x**3 + math.pi**2)
        term2 = (math.exp(y + 1) + math.sqrt(m) + math.tan(m)) / math.sqrt(m)
        result = term1 + term2
        return result
    except ValueError as e:
        return f"Error: {e}"

# Приклад виклику функції
x_value = 1  # Заміни на необхідне значення
y_value = 1  # Заміни на необхідне значення
m_value = 1  # Заміни на необхідне значення
print(f"Z = {calculate_Z(x_value, y_value, m_value)}")
