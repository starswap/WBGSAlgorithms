// Binary Search and some extension work by Pedro
function binSearch(arr, target){
  while (arr.length > 0){
    let mid = Math.floor((arr.length-1)/2); // Quotient
    if (target > arr[mid]){
      arr = arr.filter(i => {
        return i > arr[mid]; // Discards the lower half of the list
      });
    } else if (target < arr[mid]){
      arr = arr.filter(i => {
        return i < arr[mid]; // Discards the upper half of the list
      });
    } else {
      console.log('found');
      break;
    };
  };
};

// Bubble Sort
function bubSort(arr){
  let change = false;
  while (change == false){
    change = true;
    for (let count = 0; count < arr.length-1; count++){
      if (arr[count] > arr[count+1]){
        let temp = arr[count];
        arr[count] = arr[count+1];
        arr[count+1] = temp;
        change = false;
      };
    };
  };
  return arr;
};

// Hard-coded
let list = [3, 6, 12, 43, 67, 90];
let goal = 7;

// User inputs
let stuff = [];
let len = prompt('How long is your list? ');
for (let i = 0;i < len;i++){
  stuff.push(prompt('Enter a number: ')); // Adds to the array
};
stuff = stuff.map(Number); // To turn the items in the array into numbers
let targ = prompt('What\'s the target? ');

// Descisions
let dec = prompt('Is your list ordered? (Input Y or N) ');
switch(dec){
  case 'Y':
    binSearch(stuff, targ);
    break;
  case 'N':
    bubSort(stuff)
    binSearch(stuff, targ);
    break;
  default:
    console.log('Enter Y or N next time you vermin');
};
// Not very robust but I don't care
