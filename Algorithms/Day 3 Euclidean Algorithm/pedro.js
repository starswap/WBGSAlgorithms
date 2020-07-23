//Prime factorisation function courtesy of Pedro (fixed by me)
function primeFactorise(a){
  let b = 6
  let p = 2
  let aPrimes = [];
  while (p <= (a/2)+1){
      flag = false
    for (let i = 2; i<= Math.sqrt(p); i++){
      if (p % i == 0){
        console.log(p);
        p += 1; //current p is not prime
        flag = true;
        break;
      };
    };
    if (flag == true) {
        continue;
    }
    if (a%p == 0){
        temp = a;
        while (a%p == 0) {
              aPrimes.push(p);
            a = a/p;
          }
          p += 1;
        a = temp;
    } else {
      p += 1;
    };
  };
  return aPrimes;
};

console.log(primeFactorise(48));

//HCF function using the Euclidean Algorithm produced entirely by Pedro:
function hcf(){
  let a = 144;
  let b = 96;
  while (b > 0){
    let temp = a;
    a = b;
    b = temp%b;
  };
  console.log('The highest common factor is: '+ a);
};

hcf();
