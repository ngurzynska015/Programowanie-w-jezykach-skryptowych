
function czyParzysta(n) {
  return Number.isInteger(n) && n % 2 === 0;
}
console.log('Czy liczba jest parzysta?', czyParzysta(12));