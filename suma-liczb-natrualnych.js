
function sumaNaturalnych(n) {
  if (!Number.isInteger(n) || n < 0) throw new Error('n musi być całkowite i ≥ 0');
  return n * (n + 1) / 2;
}
console.log('Suma 100 liczb naturalnych to', sumaNaturalnych(100));