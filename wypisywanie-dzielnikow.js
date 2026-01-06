
function dzielniki(n) {
  if (!Number.isInteger(n) || n === 0) throw new Error('n musi być niezerową liczbą całkowitą');
  n = Math.abs(n);
  const s = new Set();
  for (let i = 1; i * i <= n; i++) {
    if (n % i === 0) {
      s.add(i);
      s.add(n / i);
    }
  }
  return Array.from(s).sort((a, b) => a - b);
}
console.log('Dzielniki tej liczby to:', dzielniki(36));