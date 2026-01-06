const number = 2;

let isPrime = true;

for (let i = 2; i <= number / 2; i++) {
  if (number % i === 0) {
    isPrime = false;
    break;
  }
}

if (isPrime) {
  console.log("Liczba jest pierwsza");
} else {
  console.log("Liczba nie jest pierwsza");
}