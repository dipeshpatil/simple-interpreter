# Simple Interpreter v 1.0
Simple Interpreter is an Interpreter which can calculate Mathematical Expressions based on rules and precedence

![Ex 1](https://i.ibb.co/RNC8Jt3/Code-Cogs-Eqn.png)

```LN (((25 * 4) + ((900 * 10 * 2 - 900 * 10) / 10)) LB 10)``` = ```1.0986122886681096```

![Ex 2](https://i.ibb.co/HgcyQhm/Code-Cogs-Eqn-1.png)

```((25 * 4) + ((900 * 10 * 2 - 900 * 10) / 10)) LB 10``` = ```3```

The following expressions can be evaluated using Simple Interpreter currently

# Arithmetic Operations

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
  
# Exponential
  
1. Pow ```**```
   - ```2 ** 3 => (2.0 ** 3.0) = 8.0```
   - ```2 ** (3 ** 2)``` => ```(2.0 ** (3.0 ** 2.0))``` = ```512.0```
   - Associativity: Left, Since Exponent is Right Associative we will have to use parenthesis for correct evaluation
  
# Square Root
  
1. N<sup>th</sup> Root ```#``` 
   - A # B => A<sup>1/B</sup>
   - ```25 # 2 => (25.0 # 2.0) = 5.0```
   - ```256 # 2 # 2``` => ```((256.0 # 2.0) # 2.0)``` = ```4.0```
   - Associativity: Left
   
# Logarithmic Functions
    
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
   
# Trigonometric Functions
   
1. Sin ```S``` 
   - ```S X``` => SIN(X)
   - ```S 30 => (S30.0)``` => Sin 30 = ```0.49999999999999994```
   - ```S 45 => (S45.0)``` => Sin 45 = ```0.7071067811865476```
   - Associativity: Right

1. Cos ```C``` 
   - ```C X``` => COS(X)
   - ```C 30 => (C30.0)``` => Cos 30 = ```0.8660254037844387```
   - ```C 45 => (C45.0)``` => Cos 45 = ```0.7071067811865476```
   - Associativity: Right
   
1. Tan ```T``` 
   - ```T X``` => TAN(X)
   - ```T 30 => (T30.0)``` => Tan 30 = ```0.5773502691896257```
   - ```T 45 => (T45.0)``` => Tan 45 = ```0.9999999999999999```
   - Associativity: Right
   
1. Cot ```1 / T``` 
   - ```1 / T X``` => 1 / TAN(X)
   - ```1 / T 30 => 1.0 / (T30.0)``` => Cot 30 = ```1.7320508075688774```
   - ```1 / T 45 => 1.0 / (T45.0)``` => Cot 45 = ```1.0000000000000002```
   - Associativity: Right
   
1. Sec ```1 / C``` 
   - ```1 / C X``` => 1 / COS(X)
   - ```1 / C 30 => 1.0 / (C30.0)``` => Sec 30 = ```1.1547005383792515```
   - ```1 / C 45 => 1.0 / (C45.0)``` => Sec 45 = ```1.414213562373095```
   - Associativity: Right
   
1. Cosec ```1 / S``` 
   - ```1 / S X``` => 1 / SIN(X)
   - ```1 / S 30 => 1.0 / (S30.0)``` => Cosec 30 = ```2.0000000000000004```
   - ```1 / S 45 => 1.0 / (S45.0)``` => Cosec 45 = ```1.414213562373095```
   - Associativity: Right
   
# Inverse Trigonometric Functions
   
1. Sin Inv ```SI``` 
   - ```SI V``` => SIN<sup>-1</sup>(V)
   - ```SI 0.5 => (SI0.5)``` => SIN<sup>-1</sup>(0.5) = ```30.000000000000004```
   - ```SI 0.707 => (SI0.707)``` => SIN<sup>-1</sup>(0.707) = ```44.991348337162016```
   - Associativity: Right

1. Cos Inv ```CI``` 
   - ```CI V``` => COS<sup>-1</sup>(V)
   - ```CI 0.5 => (CI0.5)``` => COS<sup>-1</sup>(0.5) = ```60.00000000000001```
   - ```CI 0.707 => (CI0.707)``` => COS<sup>-1</sup>(0.707) = ```44.991348337162016```
   - Associativity: Right

1. Tan Inv ```TI``` 
   - ```TI V``` => TAN<sup>-1</sup>(V)
   - ```TI 0.577 => (TI0.577)``` => TAN<sup>-1</sup>(0.577) = ```29.984946007397852```
   - ```TI 0.999 => (TI0.999)``` => TAN<sup>-1</sup>(0.999) = ```44.97133778152393```
   - Associativity: Right
  
Yet To Be Implemented
- COT INV
- SEC INV
- COSEC INV