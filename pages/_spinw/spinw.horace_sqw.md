---
{title: spinw.horace_sqw method, link: spinw.horace_sqw, summary: Calculate spectral
    weight from a spinW model for Horace. Uses disp2sqw, keywords: sample, sidebar: sw_sidebar,
  permalink: spinw_horace_sqw, folder: spinw, mathjax: true}

---
as the back-end function to calculate the convolution.
 
  >> weight = swobj.horace_sqw(qh,qk,ql,en,pars,swobj,pars,kwpars)
 
Input:
------
  qh,qk,ql,en Arrays containing points at which to evaluate sqw from the
              broadened dispersion
 
  pars        Arguments needed by the function.
              - pars = [model_pars scale_factor resolution_pars]
              - Should be a vector of parameters
              - The first N parameters relate to the spin wave dispersion
                and correspond to spinW matrices in the order defined by
                the 'mat' option [N=numel(mat)]
              - The next M parameters relate to the convolution parameters
                corresponding to the convolution function defined by the
                'resfun' option (either one or two parameters depending
                on function type.
              - The last parameter is a scale factor for the intensity
                If this is omitted, a scale factor of 1 is used;
 
  kwpars      - A series of 'keywords' and parameters. Specific to this
                function is:
 
              - 'resfun' - determines the convolution / resolution 
                   function to get S(q,w). It can be either a string: 
                     'gauss' - gaussian with single fixed (fittable) FWHM
                     'lor' - lorentzian with single fixed (fittable) FWHM
                     'voigt' - pseudo-voigt with single fixed (fittable) FWHM
                     @fun - a function handle satisfying the requirements of
                            the 'fwhm' parameter of disp2sqw.
                   NB. For 'gauss' and 'lor' only one fwhm parameter may be
                   specified. For 'voigt', fwhm = [width lorz_frac]
                   contains two parameters - the fwhm and lorentzian fraction  
                   [default: 'gauss']
              - 'partrans' - a function to transform the fit parameters
                   This transformation will be applied before each iteration
                   and the transformed input parameter vector passed to
                   spinW and the convolution function.
                   [default: @(y)y  % identity operation]
              - 'coordtrans' - a matrix to transform the input coordinates
                   (qh,qk,ql,en) before being sent to SpinW. 
                   [default: eye(4) % identity]
 
              In addition, the following parameters are used by this function                         
                   and will also be passed on to spinw.matparser which will
                   do the actual modification of spinW model parameters:
                   
              - 'mat' - A cell array of labels of spinW named 'matrix' or
                   matrix elements. E.g. {'J1', 'J2', 'D(3,3)'}. These will
                   be the model parameters to be varied in a fit, their
                   order in this cell array will be the same as in the
                   fit parameters vector.
                   [default: [] % empty matrix - no model parameters] 
 
                All other parameters will be passed to spinW. See the help
                   for spinw/spinwave, spinw/matparser and spinw/sw_neutron
                   for more information.
 
  swobj       The spinwave object which defines the magnetic system to be
              calculated.
 
Output:
-------
  weight      Array with spectral weight at the q,e points
              If q and en given:  weight is an nq x ne array, where nq
                                  is the number of q points, and ne the
                                  number of energy points
              If qw given together: weight has the same size and dimensions
                                    as q{1} i.e. qh
 
Example:
--------
 
tri = sw_model('triAF',[5 1]);                         % J1=5, J2=1 (AFM)
spinw_pars = {'mat', {'J1', 'J2'}, 'hermit', true, ...
              'useMex', true, 'optmem', 100};
[wf,fp] = fit_sqw(w1, @tri.horace_sqw, {[J1 J2 fwhm] spinw_pars});

{% include links.html %}
