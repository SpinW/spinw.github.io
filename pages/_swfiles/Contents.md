---
{title: Functions in swfiles, link: Functions in swfiles, summary: general functions,
  keywords: sample, sidebar: sw_sidebar, permalink: swfiles, folder: swfiles, mathjax: true}

---
 
This folder contains all the spectral functions and general functions
that are related to SpinW.
 
### Files
 
#### Transforming and plotting calculated spin wave spectrum
 
These functions operate on the calculated spectra, which is the output of
[spinw.spinwave](spinw_spinwave) or [spinw.powspec](spinw_powspec) commands. They enable to post process
the calculated spin-spin correlation function, including instrumental
resolution, cross section calculation, binning etc.
 
* [sw_econtract](sw_econtract) converts (Q,E) values to Q values for diffraction instrument
* [sw_egrid](sw_egrid) calculates energy bins of a spectrum 
* [sw_filelist](sw_filelist) lists spinw objects in the Matlab workspace or in a .mat file
* [sw_instrument](sw_instrument) convolutes spectrum with resolution function
* [sw_magdomain](sw_magdomain) calculates the spin-spin correlation function for magnetic domains
* [sw_neutron](sw_neutron) calculates neutron scattering cross section
* [sw_omegasum](sw_omegasum) removes degenerate and ghost magnon modes from spectrum
* [sw_plotspec](sw_plotspec) plots spectrum
* [sw_xray](sw_xray) calculates x-ray scattering cross section
 
#### Generate list of vectors in reciprocal space
 
These two functions can generate a set of 3D points in reciprocal space
defining either a path made out of straigh lines or a volume.
 
* [sw_qgrid](sw_qgrid) creates a Q grid
* [sw_qscan](sw_qscan) creates continuous line between coordinates
 
#### Resolution claculation and convolution
 
These functions can import Energy resolution function and convolute it
with arbitrary multidimensional dataset
 
* [sw_res](sw_res) fits energy resolution with polynomial
* [sw_resconv](sw_resconv) convolution of a matrix and a Gaussian
* [sw_tofres](sw_tofres) convolutes the spectrum with a Q bin
 
#### SpinW model related functions
 
* [sw_extendlattice](sw_extendlattice) creates superlattice
* [sw_fstat](sw_fstat) calculates thermodynamical averages
* [sw_model](sw_model) creates predefined spin models
* [sw_bonddim](sw_bonddim) find dimensionality of a periodic bond network
 
#### Constraint functions
 
Contraint functions for [spinw.optmagstr](spinw_optmagstr).
 
* [gm_planar](gm_planar) planar magnetic structure constraint function 
* [gm_planard](gm_planard) planar magnetic structure constraint function 
* [gm_spherical3d](gm_spherical3d) magnetic structure constraint function with spherical parameterisation
* [gm_spherical3dd](gm_spherical3dd) magnetic structure constraint function with spherical parameterisation
 
#### Geometrical calculations
 
Basic geometrical calculators, functions to generatate rotation
operators, generate Cartesian coordinate system from a set of vectors,
calculate normal vector to a set of vector, etc.
 
* [sw_basismat](sw_basismat) determines allowed tensor components in a given point group symmetry
* [sw_cartesian](sw_cartesian) creates a right handed Cartesian coordinate system
* [sw_fsub](sw_fsub) simple graph vertex coloring
* [sw_mattype](sw_mattype) classifies square matrices
* [sw_nvect](sw_nvect) determines the best normal vector for the set of vectors
  sw_quadell  
* [sw_mirror](sw_mirror) mirrors a 3D vector
* [sw_rot](sw_rot) rotates vectorsin 3D
* [sw_rotmat](sw_rotmat) generates 3D rotation matrix
* [sw_rotmatd](sw_rotmatd) generates 3D rotation matrix
 
#### Text and graphical input/output for different high level commands
 
* [sw_multicolor](sw_multicolor) overlays monochrome maps into a single RGB map
* [sw_parstr](sw_parstr) parses input string
* [sw_timeit](sw_timeit) timer and remaining time estimator
 
#### Acessing the SpinW database
 
Functions to read the different data files that store information on
atomic properties, such as magnetic form factor, charge, etc.
  
* [sw_atomdata](sw_atomdata) returns information on chemical elements
* [sw_cff](sw_cff) returns the atomic charge form factor values for X-ray scattering
* [sw_mff](sw_mff) returns the magnetic form factor values and coefficients
* [sw_nb](sw_nb) returns the bound coherent neutron scattering length
 
#### Useful physics functions
 
The two functions can calculate the Bose factor and convert
energy/momentum units, both usefull for neutron and x-ray scattering.
 
* [sw_bose](sw_bose) coefficient for boson correlation functions
* [sw_converter](sw_converter) converts energy and momentum units for a given particle
 
#### Import functions
 
Functions to import tables in text format.
 
* [sw_import](sw_import) create SpinW object from .cif and FullProf Studio .fst files
* [sw_readspec](sw_readspec) read spin wave dispersion data from file
* [sw_readtable](sw_readtable) reads tabular data from text
 
#### Miscellaneous
 
* [swdoc](swdoc) opens the SpinW documentation
* [sw_freemem](sw_freemem) calculates the available memory
* [sw_readparam](sw_readparam) parse input arguments
* [sw_rootdir](sw_rootdir) path to the SpinW folder
* [sw_uniquetol](sw_uniquetol) returns the unique column vectors within tolerance
* [sw_update](sw_update) updates the SpinW installation from the internet
* [sw_version](sw_version) returns the installed version of SpinW
* [sw_mex](sw_mex) compiles and tests the mex files

{% include links.html %}
