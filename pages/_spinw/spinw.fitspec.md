---
{title: spinw.fitspec method, link: spinw.fitspec, summary: fits experimental spin
    wave data, keywords: sample, sidebar: sw_sidebar, permalink: spinw_fitspec, folder: spinw,
  mathjax: true}

---
  
### Syntax
  
`fitsp = fitspec(obj,Name,Value)`
  
### Description
`fitsp = fitspec(obj,Name,Value)` uses a heuristic method to fit spin
wave spectrum using a few simple rules to define the goodness (or
R-value) of the fit:
1. All calculated spin wave modes that are outside of the measured
   energy range will be omitted.
2. Spin wave modes that are closer to each other than the given energy
   bin will be binned together and considered as one mode in the fit.
3. If the number of calculated spin wave modes after applying rule 1&2 
   is larger than the observed number, the weakes simulated modes will
   be removed from the fit.
4. If the number of observed spin wave modes is larger than the observed
   number, fake spin wave modes are added with energy equal to the
   limits of the scan; at the upper or lower limit depending on which is
   closer to the observed spin wave mode.
 
After these rules the number of observed and simulated spin wave modes
will be equal. The R-value is defined as:
 
$$R = \sqrt{ \frac{1}{n_E} \cdot \sum_{i,q} \frac{1}{\sigma_{i,q}^2}\left(E_{i,q}^{sim} - E_{i,q}^{meas}\right)^2},$$
   
where $$(i,q)$$ indexing the spin wave mode and momentum respectively.
$$E_{sim}$$ and $$E_{meas}$$ are the simulated and measured spin wave
energies, sigma is the standard deviation of the measured spin wave
energy determined previously by fitting the inelastic peak. $$n_E$$ is the
number of energies to fit.
   
The R value is optimized using particle swarm algorithm to find the
global minimum.
  
### Name-Value Pair Arguments
  
`'func'`
: Function to change the Hamiltonian in `obj`, it needs to have the
  following header:
  ```matlab
  obj = @func(obj, x)
  ```
  
`'datapath'`
: Path to the file that stores the experimental data. For the
  input data format see [sw_readspec](sw_readspec).
  
`'Evect'`
: Column vector with $$n_E$$ elements that defines the energy binning of
  the calculated dispersion. Larger binning steps solve the issue of
  fitting unresolved modes.
  
`'xmin'`
: Lower limit of the optimisation parameters, optional.
  
`'xmax'`
: Upper limit of the optimisation parameters, optional.
  
`'x0'`
: Starting value of the optimisation parameters. If empty
 or undefined, random values are used within the given limits.
  
`'optimizer'`
: String that determines the type of optimizer to use, possible values:
  * `'pso'`       Particle-swarm optimizer, see [ndbase.pso](ndbase_pso),
                  default.
  * `'simplex'`   Matlab built-in simplex optimizer, see [fminsearch](www.mathworks.ch/help/matlab/ref/fminsearch.html).
  
`'nRun'`
: Number of consecutive fitting runs, each result is saved in the
  output `fitsp.x` and `fitsp.R` arrays. If the Hamiltonian given by the
  random `x` parameters is incompatible with the ground state,
  those `x` values will be omitted and new random `x` values will be
  generated instead. Default value is 1.
  
`'nMax'`
: Maximum number of runs, including the ones that produce error
  (due to incompatible ground state). Default value is 1000.
  
`'hermit'`
: Method for matrix diagonalization, for details see [spinw.spinwave](spinw_spinwave).
  
`'epsilon'`
: Small number that controls wether the magnetic structure is
  incommensurate or commensurate, default value is $$10^{-5}$$.
  
`'imagChk'`
: Checks that the imaginary part of the spin wave dispersion is
  smaller than the energy bin size. Default is `true`.
  
Parameters for visualizing the fit results:
  
`'plot'`
: If `true`, the measured dispersion is plotted together with the
  fit. Default is `true`.
  
`'iFact'`
: Factor of the plotted simulated spin wave intensity (red
  ellipsoids).
  
`'lShift'`
: Vertical shift of the `Q` point labels on the plot.
  
Optimizer options:
  
`'TolX'`
: Minimum change of` x` when convergence reached, default
  value is $$10^{-4}$$.
  
`'TolFun'`
: Minimum change of the R value when convergence reached,
  default value is $$10^{-5}$$.
  
`'MaxFunEvals'`
: Maximum number of function evaluations, default value is
  $$10^7$$.
  
`'MaxIter'`
: Maximum number of iterations for the [ndbse.pso] optimizer.
  Default value is 20.
  
### Output Arguments
  
Output `fitsp` is struct type with the following fields:
* `obj`   Copy of the input `obj`, with the best fitted
          Hamiltonian parameters.
* `x`     Final values of the fitted parameters, dimensions are
          $$[n_{run}\times n_{par}]$$. The rows of `x` are sorted according 
          to increasing R values.
* `redX2` Reduced $$\chi^2_\eta$$ value, goodness of the fit stored in a column 
          vector with $$n_{run}$$ number of elements, sorted in increasing 
          order. $$\chi^2_\eta$$ is defined as:
 
  $$\begin{align}
                  \chi^2_\eta &= \frac{\chi^2}{\eta},\\
                  \eta        &= n-m+1,
  \end{align}$$
  where η is the degree of freedom, $$n$$ number of
  observations and $$m$$ is the number of fitted parameters.
 
* `exitflag`  Exit flag of the `fminsearch` command.
* `output`    Output of the `fminsearch` command.
  
{% include note.html content=" As a rule of thumb when the variance of the measurement error is
known a priori, χ$$^2_\eta$$≫ 1 indicates a poor model fit. A
χ$$^2_\eta$$≫ 1 indicates that the fit has not fully captured the
data (or that the error variance has been underestimated). In principle,
a value of χ$$^2_\eta$$= 1 indicates that the extent of the match
between observations and estimates is in accord with the error variance.
A χ$$^2_\eta$$ < 1 indicates that the model is 'over-fitting' the data:
either the model is improperly fitting noise, or the error variance has
been overestimated." %}
 
Any other option used by [spinw.spinwave](spinw_spinwave) function are also accepted.
  
### See Also
  
[spinw.spinwave](spinw_spinwave) \| [spinw.matparser](spinw_matparser) \| [sw_egrid](sw_egrid) \| [sw_neutron](sw_neutron) \| [sw_readspec](sw_readspec)
 

{% include links.html %}
