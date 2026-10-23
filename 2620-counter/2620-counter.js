/**
 * @param {number} n
 * @return {Function} counter
 */
var createCounter = function(n) {
    let currentcount=n;
    return function() {
        let valueToReturn = currentcount;
        currentcount+=1;
        return valueToReturn;
    };
};

/** 
 * const counter = createCounter(10)
 * counter() // 10
 * counter() // 11
 * counter() // 12
 */

// Synced seamlessly with LeetHub Pro
// Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
// Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna