# passwordGenerator
#### This is level based complx password generator for your
#### application to protect from unwanted mallicious hidden attacks.  

# Functionality Provides :

* #### Generate password according to your given length.
* #### Or you can provide level using argument string :


*   "l"   =   Low Protected password
*   "m"   =   Medium protected Password
*   "h"   =   High protected Password
*   "x"   =   Extra-complex Password

```
 >>> passGen("l", "m", "h", "x", length) 
```
Output Looks like for given length :
```
>>> passGen(8)

 n}TXdOZ^
```

Output Looks like for given string "l":
```
>>> passGen("l")

 BK-P%{LM5
```

Output Looks like for given string "m":
```
>>> passGen("m")

 T|8c,qO>Y7Af
```

Output Looks like for given string "h" :
```
>>> passGen("h")

 /8:Q\U5('o3VEd?Ca}
```

Output Looks like for given string "x" :
```
>>> passGen("x")

 ,|1j)V*?dm4l]'R\`}Qr5t"K8C
```
