---
{title: ndbase.pso, link: ndbase.pso, summary: particle swarm optimisation, keywords: sample,
  sidebar: sw_sidebar, permalink: ndbase_pso, folder: ndbase, mathjax: true}

---
 
[pOpt,fVal,stat] = NDBASE.PSO([],func,p0,'Option1','Value1',...)
 
[pOpt,fVal,stat] = NDBASE.PSO(dat,func,p0,'Option1','Value1',...)
 
 
PSO finds a minimum of a function of several variables using the particle
swarm optimization (PSO) algorithm originally introduced in 1995 by
Kennedy and Eberhart. This algorithm was extended by Shi and Eberhart in
1998 through the introduction of inertia factors to dampen the velocities
of the particles. In 2002, Clerc and Kennedy introduced a constriction
factor in PSO, which was later on shown to be superior to the inertia
factors. Therefore, the algorithm using a constriction factor was
implemented here.
 
The function has two different modes, depending on the first input
argument. If dat is empty, pso minimizes the cost function func, that has
the following header:
                          R2 = func(p)
 
If dat is a struct, the function optimizes the model defined by func via
least squares to the data stored in dat. In this case func has the
following header:
                          yModel = func(x,p)
And the least square deviation is defined by:
                      R2 = sum((yData-yModel).^2/errorData.^2)
 
 
Input:
 
dat       Either empty or contains data to be fitted stored in a
          structure with fields:
              dat.x   vector of N independent variables,
              dat.y   vector of N data values to be fitted,
              dat.e   vector of N standard deviation (positive numbers)
                      used to weight the fit. If zero or missing
                      1./dat.y^2 will be assigned to each point.
func      Function handle with one of the following definition:
              R2 = func(p)        if dat is empty,
              y  = func(x,p)      if dat is a struct.
          Here x is a vector of N independent variables, p are the
          M parameters to be optimized and y is the simulated model, R2
          is the value to minimize.
p0        Vector of M initial parameters.
 
Options:
 
lb        Vector with N elements, lower boundary of the parameters.
          Default value is -1e5.
ub        Vector with N elements, upper boundary of the parameters.
          Default value is 1e5.
MaxIter   Maximum number of iterations, default value is 100*M.
MaxFunEvals Maximum number of function evaluations, default value is
          1000*M. NOT IMPLEMENTED!
TolX      Convergence tolerance for parameters, default value is 1e-3.
Display   Level of information to print onto the Command Line during
          optimisation. Possible values are 'off', 'notify' and 'iter'.
          Default is 'off'.
TolFun    Convergence tolerance on the R2 value (return value of func or
          the weighted least square deviation from data). Default value
          is 1e-3.
SwarmC1   Swarm parameter, also called phi_p in the literature. Default
          value is 2.8.
SwarmC2   Swarm parameter, also called phi_g in the literature. Default
          value is 1.3.
k0        Swarm paramter, it can take values between 0 and 1, but is
          usually set to one (Montes de Oca et al., 2006). Default value
          is 1.
seed      Seed number for the random number generator, by default it is
          seeded from the system clock every time the function is called.
PopulationSize Size of the swarm, default value is 25.
autoTune  Determine the size of the swarm based on the number of free
          parameters (number of parameters that are not fixed by setting
          lb(i)==ub(i)). Default is false. The optimal swarm size is:
              PopulationSize = 25 + 1.4*Nf
          This value is based on the technical report:
              Good Parameters for Particle Swarm Optimization By Magnus Erik Hvass Pedersen Hvass Laboratories
              Technical Report no. HL1001
              http://www.hvass-labs.org/people/magnus/publications/pedersen10good-pso.pdf
tid       Setup time estimation with the following values:
              0   Do nothing (default).
              1   Text output to the Command Window. Default.
              2   Graphical output, using the waitbar() function.
             -1   Set the value from the SpinW preferences (needs SpinW
                  installed).
 
See also NDBASE.LM.
 

{% include links.html %}
