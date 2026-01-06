
function rozwiazUklad2x2(a, b, e, c, d, f, { eps = 1e-12 } = {}) {
  const det = a * d - b * c;
  if (Math.abs(det) < eps) return null; // układ osobliwy: brak lub nieskończenie wiele rozwiązań
  const x = (e * d - b * f) / det;
  const y = (a * f - e * c) / det;
  return { x, y };
}
console.log('Uklad 2x2:', rozwiazUklad2x2(2, 1, 5, 1, -1, 1));