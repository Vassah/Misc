import UIKit

let doFirst = false
let doSecond = false
let doThird = false

infix operator >> {
associativity left precedence 140
}
infix operator >>= {
associativity left precedence 140
}
infix operator >=> {
associativity left precedence 140
}

func >><T, S, Q>(left: (T -> S), right: (Q -> T))->(Q -> S) {
    return {(z: Q) -> S in
        left(right(z))
    }
}

infix operator << {
associativity left precedence 140
}

func << <T,S,Q> (left: T->S, right: S -> Q) -> T -> Q {
    return {(z: T) -> Q in
        right(left(z))
    }
}

infix operator |> {
associativity left precedence 140
}
func |> <T, S> (left: T, right: (T -> S)) -> S {
    return right(left)
}

infix operator <| {
associativity left precedence 140
}

func <| <T, S> ( left: T -> S, right: T) -> S {
    return left(right)
}

//Euler1
func isMod3(x: Int) -> Bool {
    return x % 3 == 0
}
func isMod5(x: Int) -> Bool {
    return x % 5 == 0
}

//Tests
isMod3(6)
isMod3(5)
isMod5(6)
isMod5(5)

func Euler1() -> Int {
    var answer = 0
    for number in 1..<1000 {
        if isMod3(number) || isMod5(number) {
            answer += number
        }
    }
    return answer
}
if doFirst == true {
    Euler1()
}


//Euler2
func nextFib(x: Int, y: Int) -> (Int, Int)  {
    return (y , x + y)
}

func Euler2() -> Int {
    var answer = 0
    var a = 0, b = 1, c: (Int, Int)
    while b < 4_000_000 {
        c = nextFib(a, b)
        a = c.0
        b = c.1
        answer += b
    }
    return answer
}

if doSecond == true {
    Euler2()
}

//Euler3
func Eratosthenes(n: Int) -> Array<Bool> {
    var poss: =[true]
    for i in 2...Int(sqrt(Double(n))) {
        poss.append(true)
    }
    for idx in poss {
        if poss[idx] == true {
            for m in 2...n {
                if idx*idx + m*idx > n {
                  break
                }
                poss[idx*idx + m*idx] = false
           }
        }
    }
    return poss
}

