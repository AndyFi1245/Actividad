class Calculadora:
  # Este método suma dos números. Es parte del requisito de QA y Shift-Left.
  def suma(self, a, b):
    return a + b
  def resta(self, a, b):
    return a - b
  def divide(self, a, b):
    if b == 0:
      raise ValueError("División por cero no permitida")
      return a / b
