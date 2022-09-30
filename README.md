### Grey Wolf Optimizer

##### Reference: Mirjalili S, Mirjalili S M, Lewis A. Grey wolf optimizer[J]. Advances in Engineering Software, 2014, 69: 46-61.

| Variables   | Meaning                                              |
| ----------- | ---------------------------------------------------- |
| pop         | The number of population                             |
| lb          | List, the lower bound of the i-th component is lb[i] |
| ub          | List, the upper bound of the i-th component is ub[i] |
| iter        | The maximum number of iterations                     |
| dim         | The dimension, dim = len(lb) = len(ub)               |
| pos         | List, the position of each wolf                      |
| score       | List, the score of each wolf                         |
| iter_best   | List, the best so-far score of each iteration        |
| alpha_pos   | List, the position of the alpha wolf                 |
| alpha_score | The score of alpha wolf                              |
| beta_pos    | List, the position of the beta wolf                  |
| beta_score  | The score of the beta wolf                           |
| delta_pos   | List, the position of the delta wolf                 |
| delta_score | The score of the delta wolf                          |

#### Test problem: Pressure vessel design

![](https://github.com/Xavier-MaYiMing/Grey-Wolf-Optimizer/blob/main/Convergence%20curve.png)

$$
\text{min}\ f(x)=0.6224x_1x_3x_4+1.7781x_2x_3^2+3.1661x_1^2x_4+19.84x_1^2x_3,\\
\text{s.t.} &-x_1+0.0193x_3\leq0,\\
&-x_3+0.0095x_3\leq0,\\
&-\pi x_3^2x_4-\frac{4}{3}\pi x_3^3+1296000\leq0,\\
&x_4-240\leq0,\\
&0\leq x_1\leq99,\\
&0\leq x_2 \leq99,\\
&10\leq x_3 \leq 200,\\
&10\leq x_4 \leq 200.
$$


#### Example

```python
if __name__ == '__main__':
    pop = 200
    lb = [0, 0, 10, 10]
    ub = [99, 99, 200, 200]
    iter = 100
    print(main(pop, lb, ub, iter))
```

##### Output:

![](https://github.com/Xavier-MaYiMing/Grey-Wolf-Optimizer/blob/main/Pressure%20vessel%20design.png)

```python
{
    'best solution': [0.055032292491247664, 0.038525492744343255, 15.017885426149007, 83.0839394934081], 
    'best score': 9715.833118935214,
}
```


