function bottleSong() {
  for (let numOfBeer = 99; numOfBeer >= 0; numOfBeer--){
    if (numOfBeer > 2) {
      console.log(`${numOfBeer} bottles of beer on the wall, ${numOfBeer} bottles of beer.`)
      console.log(`Take one down and pass it around, ${numOfBeer-1} bottles of beer on the wall.`)
    }
    else if (numOfBeer == 2) {
      console.log(`${numOfBeer} bottles of beer on the wall, ${numOfBeer} bottles of beer.`)
      console.log(`Take one down and pass it around, ${numOfBeer-1} bottle of beer on the wall.`)
    }
    else if (numOfBeer == 1){
      console.log(`${numOfBeer} bottle of beer on the wall, ${numOfBeer} bottle of beer.`)
      console.log(`Take one down and pass it around, no more bottles of beer on the wall.`)
    }
    else if (numOfBeer == 0) {
      console.log("No more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall.")
    }
  }
};

bottleSong();
