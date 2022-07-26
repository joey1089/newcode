// Codesmith and youtuber recursive logics learnt
let counter = 0
function recursive(){
    if (counter === 3) return "Done!"
    counter++;
    return recursive()
}

recursive()
// Codesmith and youtuber recursive logics learnt
//CodeSmith method of recursive logic
// counter = 0
// function recursive(){
//     if (counter === 3) return "Done!"
//     counter++;
//     console.log(counter)
//     return recursive()
// }
// console.log(recursive())

//web made simple +++++++++++++++++++
// function recursion(n){
//   if (n <= 0){
//     console.log("Done with Recursion")
//     return
//   }
//   console.log(n)
//   console.log(recursion(n-1))    
// }
// recursion(3)
// Instead use for loop ++++++++++++
function countdown(n){
  for(let i = n; i > 0 ; i--){
    console.log(i)
  }
  console.log("Here we go")
  return n
}

countdown(3)