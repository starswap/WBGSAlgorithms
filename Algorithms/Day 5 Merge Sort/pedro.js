// Merge Sort implemented recursively in JS by Pedro
function merSort(arr){
  if (arr.length < 2){
    return arr; // Check's if the list has already been split 
  } else {
    let split = [];
    let sortLeft = merSort(arr.slice(0, Math.ceil((arr.length)/2))); // Performs the splitting on the left half
    let sortRight = merSort(arr.slice(Math.ceil((arr.length)/2))); // Performs the splitting on the right half
    while (sortLeft.length > 0 || sortRight.length > 0){
      if (sortLeft.length == 0){
        let len = sortRight.length; // Temporary store
        for (let i = 0;i < len;i++){
          split.push(sortRight.shift()); // This was needed because I don't think JavaScript has a function to concatenate arrays
        };
      } else if (sortRight.length == 0){
        let len = sortLeft.length; // Temporary store
        for (let i = 0;i < len;i++){
          split.push(sortLeft.shift()); // Same as the other for loop
        };
      } else if (sortRight[0] < sortLeft[0]){ // Using an else if here seemed to get rid of the need for breaks
        split.push(sortRight.shift()); // Adds the first value to the new list while removing it from the old one
      } else {
        split.push(sortLeft.shift()); // Same as above
      };
    };
    return split;
  };
};

// Hard-coded stuff 
let arr = [45, 1, 8000, 6, 65, 300];
console.log('Unsorted list: '+ arr);
console.log('Sorted list: '+ merSort(arr));

// Can't be bothered to ask for user inputs 
