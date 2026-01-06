
function znakLiczby(x) {
  // -1 dla ujemnych, 0 dla zera, 1 dla dodatnich, NaN zostaje NaN
  return Math.sign(x);
}
function znakJakoTekst(x) {
  if (Number.isNaN(x)) return 'nie liczba (NaN)';
  if (x > 0) return 'dodatnia';
  if (x < 0) return 'ujemna';
  return 'zero';
}
console.log('Znak(-2):', znakLiczby(-2), znakJakoTekst(-2));