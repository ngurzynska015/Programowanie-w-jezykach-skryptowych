const aInput = prompt("Podaj wartość a ");
const a = parseFloat(aInput);

const bInput = prompt("Podaj wartość b ");
const b = parseFloat(bInput);

const cInput = prompt("Podaj wartość c ");
const c = parseFloat(cInput);

if (isNaN(a) || isNaN(b) ){
    console.error("Błąd: Wprowadzono nieprawidłowe wartości");
    throw new Error("Wartości a i b muszą być liczbami");
}


const kwadrat_sumy = (a + b) ** 2; 
const kwadrat_roznicy = (a - b) ** 2;
const roznica_kwadratow = a ** 2 - b ** 2;
const szescian_sumy = (a + b) ** 3;
const szescian_roznicy = (a - b) ** 3;
const suma_szecianow = a ** 3 + b ** 3;
const roznica_szescianow = a ** 3 - b ** 3;
const kwadrat_sumy_trzech_skladnikow = (a + b + c) ** 2;



console.log(`Kwadrat sumy z ${a}, ${b} wynosi ${kwadrat_sumy}`)
console.log(`Kwadrat różnicy z ${a}, ${b} wynosi ${kwadrat_roznicy}`)
console.log(`Różnica kwadratów z ${a}, ${b} wynosi ${roznica_kwadratow}`)
console.log(`Sześcian sumy z ${a}, ${b} wynosi ${szescian_sumy}`)
console.log(`Sześcian roznicy z ${a}, ${b} wynosi ${szescian_roznicy}`)
console.log(`Suma sześcianów z ${a}, ${b} wynosi ${suma_szecianow}`)
console.log(`Różnica sześcianów z ${a}, ${b} wynosi ${roznica_szescianow}`)
console.log(`Kwadrat sumy trzech skladników z ${a}, ${b} oraz ${c} wynosi ${kwadrat_sumy_trzech_skladnikow}`)