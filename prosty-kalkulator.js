
function kalkulator(a, op, b) {
  switch (op) {
    case '+': return a + b;
    case '-': return a - b;
    case '*': return a * b;
    case '/':
      if (b === 0) throw new Error('Dzielenie przez zero!');
      return a / b;
    case '%': return a % b; // uwaga: w JS to reszta (z zachowaniem znaku dzielnej)
    case '^': return a ** b; // potęgowanie
    default: throw new Error(`Nieznany operator: ${op}`);
  }
}
console.log('Kalkulator 6 / 3 =', kalkulator(6, '/', 3));