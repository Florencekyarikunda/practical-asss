var sum=0;
for(x=0;x<1000;x++)
{
if(x%3==0 || x%5==0){
  sum+=x;
}
}
console.log(sum);

function FizBuzz(){
  for (var i=1; i<=100; i++){
    if(i%3===0 && i%5===0)
  {
    console.log(i+ 'FizzBuzz');
  }
  else if(i%3===0)
  {
    console.log(i+ "Fizz");

  }
  else if(i%5===0)
  {
    console.log(i+ "Buzz");
  }
  else{
    console.log(i);
  }
  }

}
FizBuzz();

// function largeRange(){
//   var generateNum=Math.max(1,9);
//   return generateNum;
// }
// largeRange();

var students=[['Dav',80],['vic',77],['Divy',88],['Isha',95],['Thomas',68]]; 

var Avgmarks=0;
for(var i=0; i<students.length; i++){
  Avgmarks+=students[i][1];
  var avg=(Avgmarks/students.length);
}
console.log('Average grade:' +(Avgmarks)/students.length);

    if(avg<60){
      console.log('Grade:F');

    }
    else if(avg>70){
      console.log("Grade :D");
    }else if(avg<80){
      console.log("Grade:B");

    }
    else if (avg<100){
      console.log("Grade:A");
    }

