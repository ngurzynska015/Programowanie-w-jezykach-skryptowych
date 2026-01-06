
function cwiartka(x, y) {
  if (x === 0 && y === 0) return 'punkt (0,0)';
  if (x === 0) return 'oś Y';
  if (y === 0) return 'oś X';
  if (x > 0 && y > 0) return 'I ćwiartka';
  if (x < 0 && y > 0) return 'II ćwiartka';
  if (x < 0 && y < 0) return 'III ćwiartka';
  return 'IV ćwiartka';
}
console.log(cwiartka(2, -3));
