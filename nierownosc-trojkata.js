
function czyTrojkat(a, b, c) {
  if (a <= 0 || b <= 0 || c <= 0) return false;
  return a + b > c && a + c > b && b + c > a;
}
console.log('Czy z boków o tej długości można zrobić trójkąt?', czyTrojkat(3, 4, 5));