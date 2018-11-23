---
use_math: true
---
<div class="row text-center">
    <img src="{{ site.title-img }}" alt="SpinW Logo" style="width:65% !important" />
</div>

*SpinW* is a MATLAB library that can plot and numerically simulate magnetic structures and excitations of given spin Hamiltonian using classical Monte Carlo simulation and linear spin wave theory.

<h1 class="text-center">The Projects</h1>

<div class="spacer"></div>

<div class="row text-center">
  <div class="col-md-4 col-md-offset-0 col-sm-4 col-sm-offset-0 col-xs-12 col-xs-offset-0 text-center">
    <div class="project-card">
      {%- assign gh-user = "spinw"-%}
      {%- assign gh-project = "SpinW" -%}
      <a target="_blank" href="https://github.com/{{- gh-user -}}/{{- gh-project -}}" class="project-link" title="Go to Github Poject Page">
        <span class="fa-stack fa-4x">
          <i class="fas fa-square fa-stack-2x stack-color"></i>
          <i class="fas fa-code fa-stack-1x fa-inverse"></i>
        </span>
        <h4>{{- gh-project -}}</h4>
        <hr class="seperator">
        <p class="text-muted">Original SpinW written in MATLAB.</p>
        <hr class="seperator">
        <img src="https://img.shields.io/github/forks/{{- gh-user -}}/{{- gh-project -}}.svg?style=social&label=Fork" alt="Github" title="Github Forks">
        <img src="https://img.shields.io/github/stars/{{- gh-user -}}/{{- gh-project -}}.svg?style=social&label=Stars" alt="Github" title="Github Stars">
      </a>
    </div>
  </div>
  <div class="col-md-4 col-md-offset-0 col-sm-4 col-sm-offset-0 col-xs-12 col-xs-offset-0 text-center">
    <div class="project-card">
      {%- assign gh-project = "Models" -%}
      <a target="_blank" href="https://github.com/{{- gh-user -}}/{{- gh-project -}}" class="project-link" title="Go to Github Poject Page">
        <span class="fa-stack fa-4x">
          <i class="fas fa-square fa-stack-2x stack-color"></i>
          <i class="fas fa-stroopwafel fa-stack-1x fa-inverse"></i>
        </span>
        <h4>{{- gh-project -}}</h4>
        <hr class="seperator">
        <p class="text-muted">Model repository for SpinW</p>
        <hr class="seperator">
        <img src="https://img.shields.io/github/forks/{{- gh-user -}}/{{- gh-project -}}.svg?style=social&label=Fork" alt="Github" title="Github Forks">
        <img src="https://img.shields.io/github/stars/{{- gh-user -}}/{{- gh-project -}}.svg?style=social&label=Stars" alt="Github" title="Github Stars">
      </a>
    </div>
  </div>
  <div class="col-md-4 col-md-offset-0 col-sm-4 col-sm-offset-0 col-xs-12 col-xs-offset-0 text-center">
    <div class="project-card">
    {%- assign gh-project = "SpinWcore" -%}
      <a target="_blank" href="https://github.com/{{- gh-user -}}/{{- gh-project -}}" class="project-link" title="Go to Github Poject Page">
        <span class="fa-stack fa-4x">
          <i class="fas fa-square fa-stack-2x stack-color"></i>
          <i class="fas fa-desktop fa-stack-1x fa-inverse"></i>
        </span>
        <h4>{{- gh-project -}}</h4>
        <hr class="seperator">
        <p class="text-muted">SpinW written in C++</p>
        <hr class="seperator">
        <img src="https://img.shields.io/github/forks/{{- gh-user -}}/{{- gh-project -}}.svg?style=social&label=Fork" alt="Github" title="Github Forks">
        <img src="https://img.shields.io/github/stars/{{- gh-user -}}/{{- gh-project -}}.svg?style=social&label=Stars" alt="Github" title="Github Stars">
      </a>
    </div>
  </div>
</div>

## Features:

In short SpinW can solve the following spin Hamiltonian using classical and quasi classical numerical methods:

$$
    \mathcal{H}=\sum_{i,j}\mathbf{S}_iJ_{ij}\mathbf{S}_j + \sum_i \mathbf{S}_iA_i\mathbf{S}_i + \mathbf{B}\sum_i\mathbf{g}_i\mathbf{S}_i
$$

where $S_i$ are spin vector operators, $J_{ij}$ are 3x3 matrices describing pair coupling between spins, $A_{ij}$ are 3x3 anisotropy matrices, $B$ is external magnetic field and $g_i$ is the g-tensor.

### Crystal structures

   * definition of crystal lattice with arbitrary unit cell, using space group or symmetry operators
   * definition of non-magnetic atoms and magnetic atoms with arbitrary moment size
   * publication quality plotting of crystal structures (atoms, labels, axes, surrounding polyhedron, anisotropy ellipsoids, DM vector, etc.)

### Magnetic structures
   * definition of 1D, 2D and 3D magnetic structures
   * representation of incommensurate structures using rotating coordinate system or complex basis vectors
   * generation of magnetic structures on a magnetic supercell
   * plotting of magnetic structures

### Magnetic interactions
   * simple assignment of magnetic interactions to neighbouring magnetic atoms based on distance
   * possible interactions: Heisenberg, Dzyaloshinskii-Moriya, anisotropic and general 3x3 exchange tensor
   * arbitrary single ion anisotropy tensor (easy-plane, easy-axis, etc.)
   * Zeeman energy in homogeneous magnetic field including arbitrary g-tensor
   * calculation of symmetry allowed elements of the above tensors based on the crystallographic space group

### Simulation of magnetic structures
   * classical energy minimization assuming single-k magnetic structure for fast and simple solution for ground state magnetic structure
   * simulated annealing using the Metropolis algorithm on an arbitrary large magnetic supercell
   * calculating properties in thermodynamical equilibrium (heat capacity, magnetic susceptibility, etc.)
   * magnetic structure factor calculation using FFT
   * simulation of magnetic neutron diffraction and diffuse scattering
   * Simulation of magnetic excitations in general commensurate and incommensurate magnetic structures using linear spin-wave theory
   * calculation of spin wave dispersion, spin-spin correlation functions
   * calculation of neutron scattering cross section for unpolarized neutrons including the magnetic form factor
   * calculation of polarized neutron scattering cross sections
   * possible to include different moment sizes for different magnetic atoms
   * calculation of powder averaged spin wave spectrum

### Plotting of spin wave spectrum
   * plotting of dispersions and correlation functions
   * calculation and plotting of the convoluted spectra for direct comparison with inelastic neutron scattering
   * full integration into Horace for plotting and comparison with time of flight neutron data, see [http://horace.isis.rl.ac.uk](http://horace.isis.rl.ac.uk)

## Fitting spin wave spectra
   * possible to fit any parameter in the Hamiltonian
   * robust fitting, even when the number of simulated spin wave modes differs from the measured number of modes

Feel free to ask questions & requests!


<div class="container" style="justify-content:space-around">
  <div class="row">
    <div class="col-1-2">
        <div class="row">
            <img class='none' src="img/ess_logo.png" alt="European Spallation Source" width='250'/>
        </div>
        <div class="row">
            <img class='none' src="img/isis_logo.png" alt="ISIS, Science & Technology Facilities Council" width='250'/>
        </div>
        <div class="row">
            <img class='none' src="img/nbia_logo.png" alt="Niels Bohr International Academy" width='250'/>
        </div>  
    </div>
    <div class="col-1-2">
        <div class="row">
            <img class='none' src="img/psi_logo.png" alt="Paul Scherrer Institut" width='250' />
        </div>
        <div class="row">
            <img class='none' src="img/hzb_logo.gif" alt="Helmholtz-Zentrum Berlin" width='250' />
        </div>
        <div class="row">
        </div>
    </div>
  </div>
</div>

