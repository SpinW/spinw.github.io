---
{title: ndbase.simplex, link: ndbase.simplex, summary: simplex optimisation, keywords: sample,
  sidebar: sw_sidebar, permalink: ndbase_simplex, folder: ndbase, mathjax: true}

---
 
### Syntax
 
`[pOpt,fVal,stat] = ndbase.simplex([],func,p0,Name,Value)`
 
`[pOpt,fVal,stat] = ndbase.simplex(dat,func,p0,Name,Value)`
 
### Description
  
`[pOpt,fVal,stat] = ndbase.simplex([],func,p0,Name,Value)` finds a
minimum of a function of several parameters using the constrained simplex
optimization algorithm by calling the unconstrained Matlab built-in
algorithm [fminsearch](https://www.mathworks.com/help/matlab/ref/fminsearch.html).
 
The function has two different modes, depending on the first input
argument. If `dat` is empty, `simplex` minimizes the cost function func,
that has the following header:
```matlab
R2 = func(p)
```
 
If `dat` is a struct, `simplex` optimizes the model defined by `func` via
least squares to the data stored in `dat`. In this case `func` has the
following header:
```matlab
yModel = func(x,p)
```
 
And the least square deviation is defined by:
 
$$R^2 = \sum \frac{(y_{dat}-y_{fit})^2}{\sigma_{dat}^2}$$
 
 {% include note.html content=" If options is supplied, then TolX will apply to the transformed
 variables. All other [fminsearch](https://www.mathworks.com/help/matlab/ref/fminsearch.html) parameters should be unaffected.
 
 Variables which are constrained by both a lower and an upper
 bound will use a $$\sin(x)$$ transformation. Those constrained by
 only a lower or an upper bound will use a quadratic
 transformation, and unconstrained variables will be left alone.
 
 Variables may be fixed by setting their respective bounds equal.
 In this case, the problem will be reduced in size for [fminsearch](https://www.mathworks.com/help/matlab/ref/fminsearch.html).
 
 The bounds are inclusive inequalities, which admit the
 boundary values themselves, but will not permit any function
 evaluations outside the bounds. These constraints are strictly
 followed.
 
 If your problem has an exclusive (strict) constraint which will
 not admit evaluation at the bound itself, then you must provide
 a slightly offset bound. An example of this is a function which
 contains the log of one of its parameters. If you constrain the
 variable to have a lower bound of zero, then `simplex` may
 try to evaluate the function exactly at zero." %}
 
### Examples
 
Example usage on the rosen function.
 
```matlab
rosen = @(x) (1-x(1)).^2 + 105*(x(2)-x(1).^2).^2
```
 
Unconstrained optimisation:
 
```matlab
fminsearch(rosen,[3 3])
```
*Output*
```
    1.0000    1.0000
```
 
 
Constrained optimisation:
 
```matlab
ndbase.simplex([],rosen,[3 3],'lb',[2 2],'ub',[])
```
*Output*
```
    2.0000    4.0000
```
 
 
### Input Arguments
 
`dat`
: Either empty or contains data to be fitted stored in a structure with
  fields:
  * `dat.x`   vector of $$N$$ independent variables,
  * `dat.y`   vector of $$N$$ data values to be fitted,
  * `dat.e`   vector of $$N$$ standard deviation (positive numbers)
              used to weight the fit. If zero or missing
              `1/dat.y^2` will be assigned to each point.
 
`func`
: Function handle with one of the following definition:
  * `R2 = func(p)`        if `dat` is empty,
  * `y  = func(x,p)`      if `dat` is a struct.
  Here `x` is a vector of $$N$$ independent variables, `p` are the
  $$M$$ parameters to be optimized and `y` is the simulated model, `R2`
  is the value to minimize.
 
### Name-Value Pair Arguments
 
`'lb'`
: Vector with $$N$$ elements, lower boundary of the parameters. Default
  value is -inf.
 
`'ub'`
: Vector with $$N$$ elements, upper boundary of the parameters. Default
  value is inf.
 
`'MaxIter'`
: Maximum number of iterations, default value is $$100M$$.
 
`'MaxFunEvals'`
: Maximum number of function evaluations, default value is
  $$1000M$$. NOT IMPLEMENTED!
 
`'TolX'`
: Convergence tolerance for parameters, default value is $$10^{-3}$$.
 
`'Display'`
: Level of information to print onto the Command Line during
  optimisation. Possible values are `'off'`, `'notify'` and `'iter'`.
  Default value is `'off'`.
 
`'TolFun'`
: Convergence tolerance on the `R2` value (return value of `func` or
  the weighted least square deviation from data). Default value is
  $$10^{-3}$$.
 
 
### See Also
 
[ndbase.lm](ndbase_lm) \| [ndbase.pso](ndbase_pso)

{% include links.html %}
