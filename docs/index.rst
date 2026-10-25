.. rst-class:: home-title

SpinW
=====

.. rst-class:: home-intro

*SpinW* and *pySpinW* are libraries that can plot and numerically simulate
magnetic structures and excitations of a given spin Hamiltonian using
classical Monte Carlo simulation and linear spin-wave theory. SpinW and
pySpinW are written for MATLAB and Python respectively.

.. rst-class:: home-links

Quick links:
`Install SpinW <spinw/installation.html>`_ |
`Install pySpinW <pyspinw/installation.html>`_ |
`Report Issue <https://github.com/SpinW/spinw/issues>`_

The Projects
------------

.. container:: project-cards

   .. container:: project-card

      .. image:: _static/img/spinw3_logo.png
         :alt: SpinW logo
         :class: project-logo only-light

      .. image:: _static/img/spinw3_logo_dark.png
         :alt: SpinW logo
         :class: project-logo only-dark

      `SpinW <https://github.com/SpinW/spinw>`_

      Original SpinW written in MATLAB.

      .. container:: project-badges

         .. image:: https://img.shields.io/github/forks/spinw/SpinW.svg?style=social&label=Fork
            :alt: SpinW forks
            :target: https://github.com/spinw/SpinW/network/members

         .. image:: https://img.shields.io/github/stars/spinw/SpinW.svg?style=social&label=Stars
            :alt: SpinW stars
            :target: https://github.com/spinw/SpinW/stargazers

   .. container:: project-card

      .. image:: _static/img/pyspinw_logo.png
         :alt: pySpinW logo
         :class: project-logo only-light

      .. image:: _static/img/pyspinw_logo_dark.png
         :alt: pySpinW logo
         :class: project-logo only-dark

      `pySpinW <https://github.com/SpinW/pySpinW>`_

      Python implementation of SpinW.

      .. container:: project-badges

         .. image:: https://img.shields.io/github/forks/spinw/pySpinW.svg?style=social&label=Fork
            :alt: pySpinW forks
            :target: https://github.com/spinw/pySpinW/network/members

         .. image:: https://img.shields.io/github/stars/spinw/pySpinW.svg?style=social&label=Stars
            :alt: pySpinW stars
            :target: https://github.com/spinw/pySpinW/stargazers

Features
--------

SpinW can solve the following spin Hamiltonian using classical and
quasi-classical numerical methods:

.. math::

   H = \sum_{i,j} S_i J_{ij} S_j
       + \sum_i S_i A_i S_i
       + B \sum_i g_i S_i

where :math:`S_i` are spin vector operators, :math:`J_{ij}` are 3x3 matrices
describing pair coupling between spins, :math:`A_{i}` are 3x3 anisotropy
matrices, :math:`B` is the external magnetic field, and :math:`g_i` is the
g-tensor.

Crystal structures
~~~~~~~~~~~~~~~~~~

* Definition of crystal lattice with arbitrary unit cell, using space group or
  symmetry operators.
* Definition of non-magnetic atoms and magnetic atoms with arbitrary moment
  size.
* Publication-quality plotting of crystal structures, including atoms, labels,
  axes, polyhedra, anisotropy ellipsoids, and DM vectors.

Magnetic structures
~~~~~~~~~~~~~~~~~~~

* Definition of 1D, 2D, and 3D magnetic structures.
* Representation of incommensurate structures using a rotating coordinate
  system or complex basis vectors.
* Generation of magnetic structures on a magnetic supercell.
* Plotting of magnetic structures.

Magnetic interactions
~~~~~~~~~~~~~~~~~~~~~

* Assignment of magnetic interactions to neighbouring magnetic atoms based on
  distance.
* Heisenberg, Dzyaloshinskii-Moriya, anisotropic, and general 3x3 exchange
  tensors.
* Arbitrary single-ion anisotropy tensor, including easy-plane and easy-axis
  anisotropy.
* Zeeman energy in homogeneous magnetic field, including arbitrary g-tensor.
* Symmetry-allowed tensor elements calculated from the crystallographic space
  group.

Simulation of magnetic structures
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Classical energy minimization assuming a single-k magnetic structure for a
  fast and simple ground-state solution.
* Simulated annealing using the Metropolis algorithm on an arbitrarily large
  magnetic supercell.
* Thermodynamic equilibrium properties, including heat capacity and magnetic
  susceptibility.
* Magnetic structure factor calculation using FFT.
* Simulation of magnetic neutron diffraction and diffuse scattering.
* Magnetic excitations in commensurate and incommensurate structures using
  linear spin-wave theory.
* Spin-wave dispersion, spin-spin correlation functions, neutron scattering
  cross sections, and powder-averaged spectra.
* Polarized neutron scattering cross sections.
* Different moment sizes for different magnetic atoms.

Plotting spin-wave spectra
~~~~~~~~~~~~~~~~~~~~~~~~~~

* Plotting of dispersions, correlation functions, and convoluted spectra.
* Calculation and plotting of convoluted spectra for direct comparison with
  inelastic neutron scattering.
* Full integration into `Horace <http://horace.isis.rl.ac.uk>`_ for plotting
  and comparison with time-of-flight neutron data.

Fitting spin-wave spectra
~~~~~~~~~~~~~~~~~~~~~~~~~

* Any parameter in the Hamiltonian can be fitted.
* Fitting Hamiltonian parameters robustly against measured spectra.

Our Partners
------------

.. list-table::
   :widths: 1 1 1
   :header-rows: 0
   :class: partner-table

   * - .. image:: _static/img/ess_logo.png
          :alt: European Spallation Source
          :class: partner-logo
     - .. image:: _static/img/isis_logo.png
          :alt: ISIS, Science & Technology Facilities Council
          :class: partner-logo
     - .. image:: _static/img/psi_logo.png
          :alt: Paul Scherrer Institut
          :class: partner-logo
   * - .. image:: _static/img/hzb_logo.gif
          :alt: Helmholtz-Zentrum Berlin
          :class: partner-logo
     - .. image:: _static/img/nbia_logo.png
          :alt: Niels Bohr International Academy
          :class: partner-logo
     -

.. toctree::
   :maxdepth: 2
   :hidden:

   news
   spinw/index
   pyspinw/index
   resources/index
