
function skalaOcen(percent) {
  if (percent < 0 || percent > 100) throw new Error('Procent musi być w zakresie 0–100');
  if (percent < 40) return 1;        
  if (percent < 56) return 2;        
  if (percent < 71) return 3;        
  if (percent < 86) return 4;        
  if (percent < 96) return 5;        
  return 6;                          
}
console.log('Ocena za 83% to:', skalaOcen(83));