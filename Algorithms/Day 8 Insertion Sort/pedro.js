//Insertion and Selection Sort routines by Pedro.

// Selection Sort
function selecSort(list){
  let index = 0;
  for(let i = 0;i < list.length;i++){ // We know we have to pass through the list the same amount of times as its length
    let min = 100000000000000; // Very big number
    for(let j = i;j < list.length;j++){ // This is so we start from a position where numbers haven't been sorted
      if (list[j] < min){
        min = list[j];
        index = j;
      };
    };
    list[index] = list[i]; // Swapping values around
    list[i] = min;
  };
  console.log(list);
};

// Insertion Sort - Still needs a little bit of fixing
function inserSort(list){
  for(let i = 1;i < list.length;i++){
    let inserted = false;
    for(let j = i-1;j > -1;j--){
      if(list[i] > list[j]){ // Need to do concatenations below but I don't know how 
        inserted = true;
      };
    };
    if(inserted == false){
      let temp = list[i];
      list.splice(i, 1);
      list.unshift(temp); // This adds the item to the beginning of the list
    };
  };
  console.log(list);
};

let numbers = [89, 8, 34, 6, 12, 78, 66, 3, 2];
inserSort(numbers);

