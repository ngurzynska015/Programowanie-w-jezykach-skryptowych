
function bladBezwzgledny(measured, trueValue) {
  return Math.abs(measured - trueValue);
}
function bladWzgledny(measured, trueValue, { asPercent = true } = {}) {
  const abs = bladBezwzgledny(measured, trueValue);
  if (trueValue === 0) return Infinity; 
  const rel = abs / Math.abs(trueValue);
  return asPercent ? rel * 100 : rel;
}
console.log('Błąd abs/wzgl:', bladBezwzgledny(9.8, 10), bladWzgledny(9.8, 10));
