---
title: SpinW class properties
use_math: true
toc: "headers: 'h2'"
---
The spinw object properties store all the information necessary for the spin wave calculation. It has 8 fields with several subfields, see below.

<div id="toc"></div>

## lattice

stores the unit cell parameters
        
### Sub fields
        
* `lat_const`
         : Lattice constants in a $[1\times 3]$ vector in units defined in
           [spinw.unit] (default value is \\ang).
        
* `angle`
         : `[\\alpha,\\beta,\\gamma]` angles in a $[1\times 3]$ vector in
           radian units.
        
* `sym`
         : Symmetry operators stored in matrix with dimensions of
           $[3\times 4 \times n_{op}]$.
        
* `origin`
         : Origin of the cell in lattice units.
         
* `label`
         : Label of the space group.



## unit_cell

Stores the atoms in the crystallographic unit cell        

### Sub fields
        
* `r`
         : Positions of the atoms in the unit cell, stored in a
           matrix with dimensions of $[3\times n_{atom}]$, values are
           in lattice units.
        
* `S`
         : Spin quantum number of the atoms, stored in a row vector with
           $n_{atom}$ number of elements, non-magnetic atoms have `S=0`.
        
* `label`
         : Label of the atom, strings stored in a $[1\times n_{atom}]$
           cell.
        
* `color`
         : Color of the atom stored in a matrix with dimensions of $[3\times n_{atom}]$, where every
           column defines an RGB color with values between 0 and 255.
        
* `ox`
         : Oxidation number of the atom, stored in a $[1\times n_{atom}]$
           matrix.
        
* `occ`
         : Site occupancy in a $[1\times n_{atom}]$ matrix.
        
* `b`
         : Scattering length of the atoms for neutron and x-ray
           stored in a $[2\times n_{atom}]$ matrix, first row is neutron,
           second row is for x-ray.
        
* `ff`
         : Form factor of the site stored in a $[2\times 9\times
           n_{atom}]$ matrix, first row is the magnetic form factor for
           neutrons, the second row is the charge form factor for x-ray
           cross section.
        
* `Z`
         : Atomic number in a row vector.
        
* `A`
         : Atomic mass (N+Z) for isotopes and -1 for natural
           distribution of isotopes stored in a row vector.
        
* `biso`
         : Isotropic displacement factors in units of \\ang$^2$.
           Definition is the same as in
           [FullProf](https://www.ill.eu/sites/fullprof/), defining the
           Debye-Waller factor as $W(d) = 1/8*b_{iso}/d^2$ which is
           included in the structure factor as $\exp(-2W(d))$.
        

## twin

stores the crystal twin parameters
        
### Sub fields
        
* `rotc`
         : Rotation matrices in the $xyz$ coordinate system for
           every twin, stored in a matrix with dimensions of $[3\times
           3\times n_{twin}]$.
        
* `vol`
         : Volume ratio of the different twins, stored in a
            row vector with $n_{twin}$ elements.
        
## matrix

stores 3x3 matrices for using them in the Hamiltonian
        
### Sub fields
        
* `mat`
         : Stores the actual values of 3x3 matrices, in a matrix with
         dimensions of $[3\times 3\times n_{matrix}]$, if assigned for a 
         bond, the unit of energy is stored in [spinw.unit] (default value 
         is meV).
        
* `color`
         : Color assigned for every matrix, stored in a
           matrix with dimensions of $[3\times n_{matrix}]$, with each
           column defining an RGB value.
        
* `label`
         : Label for every matrix, stored as string in a cell with
           dimensions of $[1\times n_{matrix}]$.
        
## single_ion

stores single ion terms of the Hamiltonian
        
### Sub fields
        
* `aniso`
         : Row vector that contains $n_{magatom}$ integers, each integer
           assignes one of the matrices from the [spinw.matrix] property
           to a magnetic atom in the generated [spinw.matom] list as a single
           ion anisotropy. Zero value of `aniso` means no single ion
           anisotropy for the corresponding magnetic atom.
* `g`
         : Row vector with $n_{magatom}$ integers, each integer
           assignes one of the matrices from the [spinw.matrix] property
           to a magnetic atom in the spinw.matom list as a
           g-tensor. Zero value of `g` means a default g-value of 2 for
           the corresponding atoms.
        
* `field`
         : External magnetic field stored in a row vector with 3 elements,
           unit is defined in [spinw.unit] (default unit is Tesla).
        
* `T`
         : Temperature, scalar, unit is defined in [spinw.unit] (default
           unit is Kelvin).
        
## coupling

stores the list of bonds
        
### Sub fields
        
* `dl`
         : Distance between the unit cells of two interacting
           spins, stored in a $[3\times n_{coupling}]$ matrix.
        
* `atom1`
         : First magnetic atom, pointing to the list of
           magnetic atoms in the list generated by `spinw.matom`, stored in a
           row vector with $n_{coupling}$ element.
        
* `atom2`
         : Second magnetic atom, same as `atom1`.
        
* `mat_idx`
         : Stores pointers to matrices for every coupling in a
           $[3\times n_{coupling}]$ matrix, maximum three matrix per
           coupling (zeros for no coupling) is allowed.
        
* `idx`
         : Neighbor index, increasing indices for the equivalent
           couplings, starting with 1,2,... which means first and second
           neighbor bonds, respectively.
        
* `type`
         : Type of coupling corresponding to `mat_idx` matrices.
           Default is 0 for quadratic exchange, `type = 1` for
           biquadratic exchange.
         
* `sym`
         : If `true` the bond symmetry operators will be applied
           on the assigned matrix.
         
* `rdip`
         : Maximum distance until the dipolar interaction is
           calculated. Zero value means no dipolar interactions
           are considered.
         
* `nsym`
         : The largest bond `idx` value that is generated
           using the space group operators. Typically very long bonds for
           dipolar interactions won't be calculated using space group
           symmetry.
        
## mag_str

stores the magnetic structure
        
### Sub fields
        
* `F`
         : Complex magnetization (strictly speaking complex
           spin expectation value) for every spin in the magnetic
           cell, represented by a matrix with dimensions of $[3\times
           n_{magext}\times n_k]$,
           where `nMagExt = nMagAtom*prod(N_ext)` and $n_k$ is the number
           of the magnetic propagation vectors.
        
* `k`
         : Magnetic propagation vectors stored in a matrix with dimensions
           of $[3\times n_k]$.
        
* `N_ext`
         : Size of the magnetic supercell in lattice units, default value
           is `[1 1 1]` emaning that the magnetic cell is identical to the
           crystallographic cell. The $[1\times 3]$ vector extends the cell
           along the $a$, $b$ and $c$ axes.
        
## unit

stores the physical units for the Hamiltonian
        
Default values are meV, T, $\unicode{x212B}$ and K for energy, magnetic
         field, length and temperature, respectively.
        
### Sub fields
        
* `kB`
         : Boltzmann constant, default value is 0.0862 meV/K.
        
* `muB`
         : Bohr magneton, default values is 0.0579 meV/T.
        
* `mu0`
         : Vacuum permeability, default value is 201.335431 T$^2\unicode{x212B}^3$/meV.
        
* `label`
         : Labels for distance, energy, magnetic field and temperature
         stored in a cell with dimensions $[1\times 4]$.
        
* `nformula`
         : Number of formula units in the unit cell.
        
* `qmat`
         : Transformation matrix that converts the given $Q$ values into
         the internal reciprocal lattice. The matrix has dimensions of
         $[3\times 3]$.
        
## cache

stores temporary values
        
This property should be only used to check consistency of the code.
        
{% include warning.html content="Changing these values is strongly discouraged as it can break the code!" %}
         
### Sub fields
        
* `matom`
         : Generated data of the magnetic unit cell.
        
* `symop`
         : Generated symmetry operators for each bond.
        