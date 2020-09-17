// Descending Order
// Your task is to make a function that can take any non-negative integer as a argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.

// Examples:
// Input: 42145 Output: 54421

// Input: 145263 Output: 654321

// Input: 123456789 Output: 987654321

function descendingOrder(n){
    let arr = n.toString().split('');
    let arrNum = [];
    console.log(arr);
    for(var i = 0; i < arr.length; i++){
      arrNum.push(parseInt(arr[i]));
      console.log(arrNum)
    }
    
    let sorted = arrNum.sort(function(a, b){return b-a});
    let sorted2 = sorted.join('');
    return parseInt(sorted2);
  }
