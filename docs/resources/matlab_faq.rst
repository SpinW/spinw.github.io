Matlab SpinW F.A.Q.
===================

Those common questions

.. container:: faq-question

   **Q.** When I calculate spin wave dispersion using ``spinw.spinwave()``,
   I get the following error message:
   ``Hamiltonian matrix is not positive definite, ...``. What is wrong?

The simple explanation is that the magnetic structure, stored in the
``spinw.mag_str`` field, is not the classical ground state of the magnetic
Hamiltonian defined in the ``spinw`` object. To solve this discrepancy, the
magnetic structure or the Hamiltonian has to be changed. There is the
``spinw.optmagstr()`` function, which can determine the right classical ground
state for certain simple cases. However, in complex lattices this is not a
trivial problem.

The ``spinw.spinwave()`` function can use two methods to solve the magnetic
Hamiltonian. The first method (J. H. P. Colpa, *Phys. A Stat. Mech. Its Appl.*
**93**, 327 (1978)) needs the exact ground state; otherwise the algorithm
produces an error. If necessary to correct for small numerical errors, a small
positive number is automatically added to the diagonal of the quadratic
expression of the Hamiltonian. However, in certain cases this is not
sufficient. In this case ``spinw.spinwave()`` can use the second method, which
can "solve" the Hamiltonian even if the magnetic ground state is wrong.
Setting the ``hermit`` option to ``false`` activates a second method
(S. R. White, M. Sparks, and I. Ortenburger, *Phys. Rev.* **139**, A450
(1965)). This gives imaginary values for the spin wave dispersion in case of a
wrong ground state. The size of the imaginary part of the dispersion can give
a hint how wrong the ground state is. The imaginary part of the dispersion can
be plotted using the ``sw_plotspec()`` function with the ``imag`` option set
to ``true`` and ``mode`` option set to one. This can help to judge whether the
imaginary part of the dispersion is due to numerical error or whether the
proposed ground state is wrong.

----

.. container:: faq-question

   **Q.** Why does the energy plot come up with positive and negative energy
   modes?

The positive/negative spin wave modes belong to the one-magnon
creation/annihilation processes. Thus every dispersion has a reflected version
in the negative-energy half plane (magnon annihilation side). You can just
ignore the negative energies in most cases. The number of the spin wave modes
on the positive-energy side should be equal to the number of magnetic atoms in
the magnetic supercell.

----

.. container:: faq-question

   **Q.** When generating the magnetic structure using ``spinw.genmagstr()``,
   the program gives the warning
   *"In the extended unit cell k is still larger than epsilon!"*. Should I
   worry?

If you use the ``nExt`` parameter of ``spinw.genmagstr()`` with a value that
is not equal to ``[1 1 1]`` and the ``mode`` option is set to ``helical``, the
code checks whether the generated magnetic supercell has the right size to
properly incorporate your helical magnetic structure. You can ignore the
warning if ``nExt./k`` is close enough to an integer for your needs. For spin
wave calculation in general you can use ``nExt = [1 1 1]``, except if you want
to do a spin wave calculation on a multi-k magnetic structure.
