// const number = 11

// if(number % 2==0){
//     console.log("this is an even number");
// }else{
//     console.log("this is an odd number")
// }


// const number = 5

// let fact  = 1

// for(let i = 1;i<=number;i++){
//     fact*=i
// }
// console.log(`the factorial  for ${number} is ${fact} .`)



// const n  = 5

// var count  = 0
//  for (var i=1;i<=n;i++)
// {
//     if(n%i==0)
//     {
//         count++;
//     }
// }
// console.log(count)



// const number = 5
// let fact = 1

// for(let i=1;i<=number;i++){
//     fact*=i
// }
// console.log(`the factorial form for ${number} is ${fact}.`)



// const n =5

// // let count =0;

// // for(var  i = 1;i<=n;i++){
// //     if(n%i==0){
// //         count++;
// //     }
// // }
// // if(count==2){
// //     console.log("this is an prime number")
// // }else{
// //     console.log("this is not an prime number")
// // }


// let a = 10;
// let b = 20;

// console.log(`before swapping: a=${a},b=${b}`);

// let temp = a
// a= b
// b = temp

// console.log(`after swaping: a=${a},b=${b}`)




// let a = 5;
// let b = 10;

// console.log(a,b)

// a = a+b // so here is the explanation a = 5  b=10 = 15 so a  =15
// b = a-b // here 15-10 so 5

// a = a-b //15 - 5 =10


// console.log(`the numbers are swapped ${a},${b}`)


// let year = 2024

// if((year%4===0&&year%100!==0)||(year%400===0))
//     console.log("this is an leap year");
// else
//     console.log("its not an leap year")

// let i = 1; // start
// while (i <= 5) {       // condition
//     console.log(i);    // print the number
//     i++;               // increase i by 1


// let num = 28
// let i = 1
// let sum = 0

// while (i<num) {
//     if(num%i===0){
//         sum+=i
//     }
//     i++
// }

// if(sum===num){
//     console.log("this is an perfect number")
// }else{
//     console.log("this is not an perfect number")
// }


let n = 10
let a = 0
let b = 1
let i = 1

console.log("fibronic series")


while (i<n) {
    console.log(a)

    let next = a+b 
    a = b
    b = next
    i++
}