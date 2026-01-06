 function NWD (a, b) {
 a = Math.abs(a);
  b = Math.abs(b);

  while (b) { 
    let temp = b;
    b = a % b; 
    a = temp;    
  }
  return a; 
}

console.log(NWD(48, 18)); 
console.log(NWD(101, 103)); 