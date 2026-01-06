
function potegiDwojkiBig(k) {
  if (!Number.isInteger(k) || k < 0) throw new Error('k musi być liczbą całkowitą ≥ 0');
  const out = [];
  let p = 1n;
  for (let i = 0; i < k; i++) {
    out.push(p);
    p *= 2n;
  }
  return out;
}
console.log('Potęgi 2 (k=5):', potegiDwojkiBig(5));