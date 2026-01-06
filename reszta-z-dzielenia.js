
function modulo(a, b) {
  if (b === 0) throw new Error('Modulo przez zero!');
  return ((a % b) + b) % b;
}
console.log('Reszta z dzielenia:', modulo(-3, 5));