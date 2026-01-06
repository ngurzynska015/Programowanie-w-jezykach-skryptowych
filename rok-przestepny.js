
function czyRokPrzestepny(year) {
  if (!Number.isInteger(year)) throw new Error('Rok musi być liczbą całkowitą');
  return (year % 4 === 0) && (year % 100 !== 0 || year % 400 === 0);
}
console.log('Czy rok jest przestępny?', czyRokPrzestepny(2024));