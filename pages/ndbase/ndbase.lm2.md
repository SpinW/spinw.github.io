---
{title: ndbase.lm2, link: ndbase.lm2, summary: optimization of parameters using the
    Levenberg Marquardt method, keywords: sample, sidebar: sw_sidebar, permalink: ndbase_lm2,
  folder: ndbase, mathjax: true}

---
 
[pOpt,fVal,stat] = NDBASE.LM([],func,p0,'Option1','Value1',...)
 
Levenberg Marquardt curve-fitting function, minimizes the return value of
a given function.
 
Input:
 
func      Function handle with the following definition:
              R = func(p)
          where p are the M parameters to be optimized.
p0        Vector of M initial parameters.
 
Options:
 
Options can be given using the modified output of optimset() or as option
name string option value pairs.
 
dp        Vector with N or 1 element, defines the fractional increment of
          'p' when calculating the Jacobian matrix dFunc(x,p)/dp:
              dp(j)>0     central differences calculated,
              dp(j)<0     one sided 'backwards' differences calculated,
              dp(j)=0     sets corresponding partials to zero, i.e. holds
                          p(j) fixed.
          Default value if 1e-3.
vary      Vector with N elements, if an element is false, the
          corresponding parameter will be fixed. Default value is
          false(1,N).
lb        Vector with N elements, lower boundary of the parameters.
          Default value is -inf.
ub        Vector with N elements, upper boundary of the parameters.
          Default value is inf.
MaxIter   Maximum number of iterations, default value is 10*M.
MaxFunEvals Maximum number of function evaluations, default value is
          100*M.
TolX      Convergence tolerance for parameters, defines the maximum of
          the relative chande of any parameter value. Default value is
          1e-3.
eps1      Convergence tolerance for gradient, default value is 1e-3.
eps2      Convergence tolerance for reduced Chi-square, default value is
          1e-2.
eps3      Determines acceptance of a L-M step, default value is 0.1.
lambda0   Initial value of L-M paramter, default value is 1e-2.
nu0       Value that determines the speed of convergence. Default value
          is 10. It should be larger than 1.
 
Output:
 
pOpt      Value of the M optimal parameters.
fVal      Value of the model function calculated with the optimal
          parameters at the N independent values of x.
 
stat      Structure, storing the detailed output of the calculation with
          the following fields:
              p       Least-squares optimal estimate of the parameter
                      values.
              redX2   Reduced Chi squared error criteria, its value
                      should be close to 1. If the value is larger, the
                      model is not a good description of the data. If the
                      value is smaller, the model is overparameterized
                      and fitting the statistical error of the data.
              sigP    Asymptotic standard error of the parameters.
              sigY    Asymptotic standard error of the curve-fit.
              corrP   Correlation matrix of the parameters.
              Rsq     R-squared cofficient of multiple determination.
              cvgHst  Convergence history.
              exitFlag The reason, why the code stopped:
                          1       convergence in r.h.s. ("JtWdy"),
                          2       convergence in parameters,
                          3       convergence in reduced Chi-square,
                          4       maximum Number of iterations reached
                                  without convergence
              message String, one of the above messages.
              nIter   The number of iterations executed during the fit.
              nFunEvals The number of function evaluations executed
                      during the fit.
 
See also NDBASE.PSO.
 

{% include links.html %}
