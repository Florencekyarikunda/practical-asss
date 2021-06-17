const items=[
    {name:'Potatoes', price:100},
    {name:'Munete', price:2300},
    {name:'JUmper', price:100},
    {name:'tv', price:50}

];
const filteredItems=items.filter (items=>items.price<100)

console.log(filteredItems)

var num=[677809,890]
console.log(num.reverse())


var today=new Date();
var day=today.getDay();
var daylist=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"];
console.log("Today is: "+daylist[day]+ ".");

let hour = today.getHours()
var minute=today.getMinutes();
var second=today.getSeconds();

let prepand=(hour>12)? "PM":"AM";
hour=(hour>=12)? hour-12: hour;

if(hour===0 && prepand==='PM')
{
if(minute===0 && second===0)
{
        hours=12;
        prepand='Noon';
}
else{
hour=12;
prepand='PM';
}
}
if(hour===0 && prepand==='PM')
{
if(minute===0 && second===0)
{
hours=12;
prepand=' Midnight';

}   
else
{
        hour=12;
        prepand=' AM';
    }
}
    console.log(`Current time: ${hour}${prepand},${minute}:${second}`);

function flo(x,y,z){
    var res=[x,y,z];
    res.sort(function(a,b){b-a});
    return console.log(res);

};

console.log(flo(-10,-3,0));

var number=15
for (var x=0; x<=15;x++){
    if(x===0){
        console.log(x + "is even");
    }
    else if(x!==0){
console.log(x + "is not odd");
    }else{
        console.log("is odd");
    }
}

let objOne={first: "JS"};
let objTwo={last:"Startup"};

let newObj=Object.assign(objOne,objTwo);

newObj['first']='NodeJS';
newObj['last']='ReactJS';

console.log(objOne['first']);
console.log(objTwo['last']);