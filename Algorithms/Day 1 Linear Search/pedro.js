// Linear Search - With timer extension by PedroCar
function linSearch(target, things) { // Takes the array and what you're looking for
  for (let counter = 0; counter < things.length; counter++){
    if (target === things[counter]) { // Checks the target against the current item
      console.log('found');
      break;
    } else if (counter === things.length -1) { // If it reaches the end of the list without finding a match then it's not in the list
      console.log('The thing you\'re looking for isn\'t in this list');
    };
  };
};

// Hard-coded list and target
let things = ['stuff', 'items', 'entities', 0, 32, 4219];
let target = 32;

// User inputs
let len = prompt('How long is your list going to be? '); // The length of the list
array = []; // Array to be filled
for (i = 0; i < len; i++){ // Repeats however many times the user asked for
  let item = prompt('Enter an item to put in your list ');
  array.push(item); // Adds the item to the end of the list
};
let goal = prompt('What\'s your target? ');

// An attempt at a timer
function timer(target, things, func) {
  let time = new Date();
  start = time.getDate();
  func(target, things);
  stop = time.getDate();
  console.log(stop - start); // This seems to keep printing 0 I don't know if that's because it's not working or because the search is just too quick
};

timer(goal, array, linSearch)
