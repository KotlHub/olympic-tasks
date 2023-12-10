function gcd(a, b) {
    return b === 0 ? a : gcd(b, a % b);
}
function timeToChase(A, B, V) {
    const distance = B - A;
    const halfOfWay = distance / (2 * V);
    const gcd = gcd(halfOfWay, 1);
    const numerator = halfOfWay / gcd;
    const denominator = 1 / gcd;
    
    return `${numerator} ${denominator}`;
}
const input = "1 2 1";
const [A, B, V] = input.split(" ").map(Number);
const result = timeToChase(A, B, V);
console.log(result);