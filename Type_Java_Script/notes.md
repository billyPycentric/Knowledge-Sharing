# TypeSCript Vs JavaScript   
# (Type vs Java)Script   
* Typescript is a superset of javascript meaning JS code is valid in TS  
* Typescript is javascript but with more features          
## Why was ts Developed    
Ts was developed to address several limitations and challenges of js associated with using js for large scale projects   
* Lack of static Typing - js is dynamically typed, which can lead to run time errors    
* Code maitainability - When projects grow bigger it becomes difficult to manage Js      
## What is Ts   
TypeScript is a programming language that supports both dynamic and static typing. It provides classes, visibility scopes, namespaces, inheritance, unions, interface   
# Configure config file   
~~~
tsc --init
~~~
### Demo   
~~~javascript
function area(width, height) {
  return width * height;
}

const calculatedArea = area(10, "20");
console.log(area); 
~~~   
from this we can see that accrding to the function , one can assume that the args are integers but if you use a var other than int you wont get the error , you will get it during runtime   
This can be avoided by ts:   
~~~JavaScript
function calculatedArea(width: number, height: number): number {
  return width * height;
}

const area = calculateArea(10, "20")
~~~   
Here the error will be caught at compile time   
### Benefits of static typing   
* Early Err Detection   
* improved code redability   
* IDE Support      


| Feature         | TypeScript                                    | JavaScript                               |
|-----------------|----------------------------------------------|------------------------------------------|
| Typing          | Provides static typing                       | Dynamically typed                        |
| Tooling         | Comes with IDEs and code editors             | Limited built-in tooling                 |
| Syntax          | Similar to JavaScript, with additional features | Standard JavaScript syntax               |
| Compatibility   | Backward compatible with JavaScript          | Cannot run TypeScript in JavaScript files |
| Debugging       | Stronger typing can help identify errors     | May require more debugging and testing   |
| Learning Curve  | Can take time to learn additional features   | Standard JavaScript syntax is familiar   |