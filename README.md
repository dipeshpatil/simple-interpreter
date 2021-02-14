# Simple Interpreter v 1.0
Simple Interpreter is an Interpreter which can calculate Mathematical Expressions based on rules and precedence

![Ex 1](https://i.ibb.co/RNC8Jt3/Code-Cogs-Eqn.png)

```LN (((25 * 4) + ((900 * 10 * 2 - 900 * 10) / 10)) LB 10)``` = ```1.0986122886681096```

![Ex 2](https://i.ibb.co/HgcyQhm/Code-Cogs-Eqn-1.png)

```((25 * 4) + ((900 * 10 * 2 - 900 * 10) / 10)) LB 10``` = ```3```

The following expressions can be evaluated using Simple Interpreter currently

1. Addition ```+```
   - ```2 + 3 => (2.0 + 3.0) = 5.0```
   - ```2 + 3 + 3``` => ```((2.0 + 3.0) + 3.0)``` = ```8.0```
   - Associativity: Left
    
1. Subtraction ```-```
   - ```5 - 2 => (5.0 - 2.0) = 3.0```
   - ```5 - 2 + 3``` => ```((5.0 - 2.0) + 3.0)``` = ```6.0```
   - Associativity: Left
    
1. Multiplication ```*```
   - ```5 * 2 => (5.0 * 2.0) = 10.0```
   - ```5 * 2 * 3``` => ```((5.0 * 2.0) * 3.0)``` = ```30.0```
   - Associativity: Left
    
1. Division ```/```
   - ```30 / 10 => (30.0 / 10.0) = 3.0```
   - ```300 / 30 / 5``` => ```((300.0 / 30.0) / 5.0)``` = ```2.0```
   - Associativity: Left
    
1. Integer Division ```//```
   - ```25 // 2 => (25.0 // 2.0) = 12.0```
   - ```237 // 20 // 3``` => ```((237.0 // 20.0) // 3.0)``` = ```3.0```
   - Associativity: Left
    
1. Mod ```%```
   - ```15 % 4 => (15.0 % 4.0) = 3.0```
   - ```5000 % 23 % 2``` => ```((5000.0 % 23.0) % 2.0)``` = ```1.0```
   - Associativity: Left
    
1. Pow ```**```
   - ```2 ** 3 => (2.0 ** 3.0) = 8.0```
   - ```2 ** (3 ** 2)``` => ```(2.0 ** (3.0 ** 2.0))``` = ```512.0```
   - Associativity: Right, Since Exponent is Right Associative we will have to use parenthesis for correct evaluation
    
1. N<sup>th</sup> Root```#``` 
   - A # B => A<sup>1/B</sup>
   - ```25 # 2 => (25.0 # 2.0) = 5.0```
   - ```256 # 2 # 2``` => ```((256.0 # 2.0) # 2.0)``` = ```4.0```
   - Associativity: Left
    
1. Log with Base ```LB``` 
   - A ```LB``` B => LOG<suB>B</sub>A
   - ```32 LB 2 => (32.0 LB 2.0)``` => LOG<sub>2</sub>32 = ```5.0```
   - ```1024 LB 2 LB 10``` => ```((1024.0 LB 2.0) LB 10.0)``` => LOG<sub>10</sub>LOG<sub>2</sub>(1024) = ```1.0```
   - Associativity: Left
   
1. Natural Log ```LN``` 
   - ```LN B``` => LOG<suB>e</sub>B
   - ```LN 10 => (LN10.0)``` => Ln 10 = ```2.302585092994046```
   - ```LN LN 10``` => ```(LN(LN10.0))``` => Ln Ln 10 = ```0.834032445247956```
   - Associativity: Right