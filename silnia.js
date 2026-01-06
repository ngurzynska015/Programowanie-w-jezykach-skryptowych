
function silniaBig(n) {
  if (!Number.isInteger(n) || n < 0) throw new Error('n musi być całkowite i ≥ 0');
  let r = 1n;
  for (let i = 2n; i <= BigInt(n); i++) r *= i;
  return r; // BigInt
}
console.log('Silnia(20) BigInt:', silniaBig(20).toString());