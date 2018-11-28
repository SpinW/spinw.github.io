---
{title: sw_xray, link: sw_xray, summary: calculates x-ray scattering cross section,
  keywords: sample, sidebar: sw_sidebar, permalink: sw_xray, folder: swfiles, mathjax: true}

---
  
### Syntax
  
`spectra = sw_xray(spectra,Name,Value)`
  
### Description
  
`spectra = sw_xray(spectra,Name,Value)` calculates x-ray scattering
intensity for non-resonant inelastic x-ray scattering on phonons.
   
  
### Input Arguments
  
`spectra`
: Input structure that contains the displacement-displacement
  correlation function.
  
### Name-Value Pair Arguments
 
`'formfact'`
: If true, the magnetic form factor is included in the spin-spin
  correlation function calculation. The form factor coefficients are
  stored in `obj.unit_cell.ff(1,:,atomIndex)`. Default value is `false`.
 
`'formfactfun'`
: Function that calculates the magnetic form factor for given $$Q$$ value.
  value. Default value is `@sw_mff`, that uses a tabulated coefficients
  for the form factor calculation. For anisotropic form factors a user
  defined function can be written that has the following header:
  ```matlab
  F = formfactfun(atomLabel,Q)
  ```
  where the parameters are:
  * `F`           row vector containing the form factor for every input 
                  $$Q$$ value
  * `atomLabel`   string, label of the selected magnetic atom
  * `Q`           matrix with dimensions of $$[3\times n_Q]$$, where each
                  column contains a $$Q$$ vector in $$Å^{-1}$$ units.
 
`'fid'`
: Defines whether to provide text output. The default value is determined
  by the `fid` preference stored in [swpref](swpref). The possible values are:
  * `0`   No text output is generated.
  * `1`   Text output in the MATLAB Command Window.
  * `fid` File ID provided by the `fopen` command, the output is written
          into the opened file stream.
 
### Output Arguments
  
`spectra`
: Structure that is same as the input with the following additional
  fields:
  * `param`   Input parameters.
  * `Sperp`   $$S_\perp(i_{mode},\mathbf{Q})$$ x-ray scattering cross
              section, stored in a matrix with dimensions of
              $$[n_{mode n_{hkl}]$$.
  
### See Also
  
[spinw](spinw) \| [spinw.spinwave](spinw_spinwave) \| [sw_neutron](sw_neutron)
 

{% include links.html %}
