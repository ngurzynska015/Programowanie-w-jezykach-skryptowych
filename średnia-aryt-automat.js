const oceny = [4.5, 3.5, 5.0, 5.0];
const suma = oceny.reduce((acc, ocena) => acc + ocena, 0 );

const średnia = suma / oceny.length;

oceny.forEach((ocena, index) => {
console.log(`ocena ${index + 1}: ${ocena}`)

});

console.log(`średnia arytmetyczna: (${oceny.join(` + `)}) / ${oceny.length} = ${średnia.toFixed(2)}`);
