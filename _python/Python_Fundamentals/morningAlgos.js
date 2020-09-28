function reverseString(stringInput){
    var newstr = "";
    for (var i = stringInput.length -1 ; i>= 0; i--){
        newstr += stringInput[i]

    }
    return newstr

}

console.log(reverseString('Creature'))