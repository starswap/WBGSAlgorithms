//Seven Divisibility Checks by Pedro Cardoso, implemented in Javascript

// Part 1
const moduloSeven = n => {
  return (n%7 === 0)
};

// Part 2
const manualSeven = n => {
  n = n.toString();
  if (n.length > 1) {
    let tens = n[0]; // Stores the tens
    let unit = n[1]; // Stores the units 
    console.log(tens - 2*unit);
    switch(tens - 2*unit) { // The M-2R
      case -14: // The below are the possible outcomes
      case -7:
      case 0:
      case 7:
        return true;
        break;
      default: // If we don't get any of the above then the check failed
        return false;
    };
  } else {
    Number(n);
    if (n/7 === 1) { // There's only one 1 digit number that's divisible by seven
      return true;
    } else {
      return false;
    };
  };
};
// Not very robust tbh because if you use a 3 digit number then it doesn't work

// Extension using a while loop
const loopSeven = n => {
  flag = false;
    while (n != 0 && n != 7 && n != -7) { // This is to keep repeating the M-2R
      n = n.toString(); // So that .replace() works
      n = n.replace('-', ''); // Gets rid of the - sign
      let tens = n.slice(0, n.length-1); // Stores the tens
      let unit = n[n.length-1]; // Stores the units
      n = tens - 2*unit; // Replaces the old value with the new one from M-2R
      let check = n.toString(); 
      if (check.includes('-')) {
        check = check.replace('-', '');
      };
      if (check.length === 1) { // This is so we know when to stop if the number isn't 7
        if (flag == false) {
          flag = true;
        }
        else{
          return false
        };
      };
    };
    return true;
}

loopSeven(10)
