
function pitagoras(a, b) {
  return Math.hypot(a, b); 
}

function czyProstokatny(a, b, c, { eps = 1e-12 } = {}) {
  const boky = [a, b, c].sort((x, y) => x - y);
  const [p, q, r] = boky;
  return Math.abs(r * r - (p * p + q * q)) < eps;
}
console.log('Pitagoras(3,4):', pitagoras(3, 4));
console.log('Czy prostokątny(3,4,5):', czyProstokatny(3, 4, 5));