const vowel = (str) => {
    let count = 0
    const  vowela =['a','e','i','o','u']
    for ( let char of str){
        if (vowela.includes(char))
        {
            count++

        }
    
    }
    console.log(count)
    return count
}
console.log (vowel("sfsdfsrfaio"))