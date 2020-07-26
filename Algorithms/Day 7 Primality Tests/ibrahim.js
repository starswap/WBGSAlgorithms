//Basic trial division primality test by Ibrahim (his first programming contribution - Congratulations!)
function isPrimeNumber(n) {

    if (Number.isInteger(n) && n > 1) {
        var r = [];

        for (var i = 2; i < n; i++) {
            r.push(n % i);
        }
    }

    console.log(!!r && !r.includes(0));
}
