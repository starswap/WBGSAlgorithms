//Fermat Test Procedure by Pedro. Note that in many implementations the JS exponentiation function is woefully inadequate for this type of task. It doesn't have enough memory to store all of the significant figures, so some rounding is used, but of course in modular arithmetic you absolutely must have the last few digits. This means the code will struggle, depending on your implementation, with anything above about 1000 for the random multiplier/500 for the prime.

function fermatTest(p){
  let primCount = 0;
  let compCount = 0;
  for (let i = 0; i < 100;i++){
    let settingUpA = false;
    let a = 0;
    while (settingUpA == false){
      a = Math.floor(Math.random()*100);
      if (a % p != 0){
        settingUpA = true;
      };
    };
    if (Math.pow(a,(p-1))%p == 1){
      primCount += 1;
    } else {
      compCount += 1;
    };
  };
  console.log('Successful primality tests: '+ primCount);
  console.log('Failed primality tests: '+ compCount);
};

fermatTest(7); 
