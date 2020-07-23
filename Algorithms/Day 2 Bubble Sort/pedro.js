// Bubble Sort by Pedro
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
  console.log('Sorted list: '+ arr);
};

// Hard-coded list
let list = [32, 92, 5, 23, 9, 54, 2, 14];

// User input list
let len = prompt('How long is your list going to be? ');
let usList = [];
for (let i = 0; i < len; i++) {
  let numb = prompt('Enter a number ');
  Number(numb);
  usList.push(numb);
};
usList = usList.map(Number); // This is because when I push the numbers into the array it turns them into strings and for some reason that broke the sorting

bubSort(usList);
