---
layout: tutorial
title: Tutorial 31
subtitle: Internal data structure of SpinW
---

<div class="content"><h1>Internal data structure of SpinW</h1><!--introduction--><p>Import the LiCrO2 crystal structure from a web link. It has space group R-3m, rhombohedrl crystal structure in hexagonal settings. What is the density? Where does all the data comes from? edit atom.dat</p><!--/introduction--><h2>Contents</h2><div><ul><li><a href="#1">Get the lattice</a></li><li><a href="#2">Check out internal data structure of SpinW</a></li><li><a href="#3">Test cordinate transformations</a></li><li><a href="#4">Rotate a vector</a></li><li><a href="#5">Magnetic atoms</a></li><li><a href="#6">Space groups</a></li><li><a href="#7">Bond symmetry</a></li><li><a href="#8">Lets do something crazy</a></li><li><a href="#9">Lets add a few matrices</a></li><li><a href="#10">Lets add some matrices and plot</a></li><li><a href="#11">Plot a single triangular layer from LiCrO2</a></li><li><a href="#12">Single ion properties</a></li><li><a href="#13">Magnetic structure</a></li><li><a href="#14">Rotating frame representation</a></li><li><a href="#15">Let's do some animation by rotating the moments</a></li><li><a href="#16">Check the spin wave dispersion</a></li><li><a href="#17">Case when the rotating frame representation fails</a></li></ul></div><h2 id="1">Get the lattice</h2><pre class="codeinput">licro = spinw(<span class="string">'https://raw.githubusercontent.com/SpinW/Models/master/cif/licro2.cif'</span>);

licro.formula
</pre><pre class="codeoutput">     Chemical formula:  Cr1Li1O2
     Formula mass:        90.936 g/mol
     Formula in cell:          3 units
     Cell volume:        105.178 &Aring;&sup3;
     Density:              4.307 g/cm&sup3;
</pre><h2 id="2">Check out internal data structure of SpinW</h2><p>What do you see?</p><pre class="codeinput">properties(spinw)

licro.lattice
</pre><pre class="codeoutput">
Properties for class spinw:

    lattice
    unit_cell
    twin
    matrix
    single_ion
    coupling
    mag_str
    unit
    cache


ans = 

  struct with fields:

        angle: [1.5708 1.5708 2.0944]
    lat_const: [2.9010 2.9010 14.4311]
          sym: [3&times;4&times;36 double]
       origin: [0 0 0]
        label: 'R -3 m H'

</pre><h2 id="3">Test cordinate transformations</h2><p>Convert (1,1,0) in the reciprocal lattice of LiCrO2 to A^-1 and convert (1,0,0) in lattice units to the crystal Descartes coordinate system (denoted by xyz in SpinW).</p><p>How are Trl and Tr related?</p><pre class="codeinput">Trl = licro.rl;
Q = [0 1 0];
QinvA = Q*Trl

Tl = licro.basisvector;
pos = [1;0;0];
RA = Tl*pos
</pre><pre class="codeoutput">
QinvA =

         0    2.5009   -0.0000


RA =

    2.9010
         0
         0

</pre><h2 id="4">Rotate a vector</h2><p>Using the rotation axis and Rotation angle in degree, the sw_rotmatd can generate the corresponding rotation matrix.</p><pre class="codeinput">R = sw_rotmatd([0 0 1],60);

<span class="comment">% Rotate polar vector</span>
R*pos
</pre><pre class="codeoutput">
ans =

    0.5000
    0.8660
         0

</pre><h2 id="5">Magnetic atoms</h2><p>Can you find the magnetic atom positions on the plot and connect them to the list in mAtom and in licro.unit_cell?</p><pre class="codeinput">plot(licro)
mAtom = licro.matom
</pre><pre class="codeoutput">
mAtom = 

  struct with fields:

      r: [3&times;3 double]
    idx: [2 2 2]
      S: [1.5000 1.5000 1.5000]

</pre><img vspace="5" hspace="5" src="/tutorial31_01.png" alt=""> <h2 id="6">Space groups</h2><p>Check out symmetry.dat: What does it mean P0~=P1? In case P0 the equivalent bonds are determined based on length, while for P1 (or any other space group), the equivalent bonds are determined based on the symmetry operators.</p><pre class="codeinput">edit <span class="string">symmetry.dat</span>
</pre><h2 id="7">Bond symmetry</h2><p>Generate the bond list of LiCrO2. Are the bonds generated usign the space group? What does it mean?</p><pre class="codeinput">licro.gencoupling

<span class="comment">% The first neighbor bonds</span>
licro.table(<span class="string">'bond'</span>,1)
</pre><pre class="codeoutput">
ans =

  9&times;10 table

    idx    subidx          dl                dr          length      matom1      idx1      matom2      idx2        matrix    
    ___    ______    ______________    ______________    ______    __________    ____    __________    ____    ______________

     1       1       -1    -1     0    -1    -1     0    2.901     'Cr1 Cr3+'     2      'Cr1 Cr3+'     2      ''    ''    ''
     1       2        0     1     0     0     1     0    2.901     'Cr1 Cr3+'     2      'Cr1 Cr3+'     2      ''    ''    ''
     1       3        1     0     0     1     0     0    2.901     'Cr1 Cr3+'     2      'Cr1 Cr3+'     2      ''    ''    ''
     1       4        1     1     0     1     1     0    2.901     'Cr1 Cr3+'     3      'Cr1 Cr3+'     3      ''    ''    ''
     1       5        0    -1     0     0    -1     0    2.901     'Cr1 Cr3+'     3      'Cr1 Cr3+'     3      ''    ''    ''
     1       6       -1     0     0    -1     0     0    2.901     'Cr1 Cr3+'     3      'Cr1 Cr3+'     3      ''    ''    ''
     1       7        1     1     0     1     1     0    2.901     'Cr1 Cr3+'     1      'Cr1 Cr3+'     1      ''    ''    ''
     1       8        0    -1     0     0    -1     0    2.901     'Cr1 Cr3+'     1      'Cr1 Cr3+'     1      ''    ''    ''
     1       9       -1     0     0    -1     0     0    2.901     'Cr1 Cr3+'     1      'Cr1 Cr3+'     1      ''    ''    ''

</pre><h2 id="8">Lets do something crazy</h2><p>Lets convert the hexagonal cell to the primitive cell and see what happens.</p><p>Why copy()? The spinw object is handle object, the copy() command creates a hard copy to avoid modifying the original object. Check spinw.formula() to see how much the new cell is smaller</p><pre class="codeinput">licroR = copy(licro);
T = licroR.newcell(<span class="string">'bvect'</span>,{[-1 1 1]/3 [2 1 1]/3 [-1 -2 1]/3})
plot(licroR,<span class="string">'cellMode'</span>,<span class="string">'outside'</span>)
swplot.zoom(1.5)
</pre><pre class="codeoutput">
T =

   -0.3333    0.3333    0.3333
    0.6667    0.3333    0.3333
   -0.3333   -0.6667    0.3333

</pre><img vspace="5" hspace="5" src="/tutorial31_02.png" alt=""> <h2 id="9">Lets add a few matrices</h2><p>What does the different input do? Check the result by inspecting the licro.matrix.mat array.</p><pre class="codeinput">licro.addmatrix(<span class="string">'label'</span>,<span class="string">'J'</span>,<span class="string">'value'</span>,1)
licro.addmatrix(<span class="string">'label'</span>,<span class="string">'D'</span>,<span class="string">'value'</span>,[0 1 0])
licro.addmatrix(<span class="string">'label'</span>,<span class="string">'A'</span>,<span class="string">'value'</span>,diag([1 0.5 0.5]))
</pre><h2 id="10">Lets add some matrices and plot</h2><p>Do both for the primitive and the hexagonal cell Are they the same?</p><pre class="codeinput">licroR.gencoupling
licroR.addmatrix(<span class="string">'label'</span>,<span class="string">'J'</span>,<span class="string">'value'</span>,1)
licroR.addcoupling(<span class="string">'bond'</span>,1,<span class="string">'mat'</span>,<span class="string">'J'</span>)
plot(licroR,<span class="string">'range'</span>,[3 3 3],<span class="string">'unit'</span>,<span class="string">'lu'</span>,<span class="string">'atomMode'</span>,<span class="string">'mag'</span>,<span class="string">'cellMode'</span>,<span class="string">'none'</span>,<span class="string">'atomLegend'</span>,false)
swplot.zoom(1.5)
</pre><img vspace="5" hspace="5" src="/tutorial31_03.png" alt=""> <h2 id="11">Plot a single triangular layer from LiCrO2</h2><pre class="codeinput">licro.addcoupling(<span class="string">'bond'</span>,1,<span class="string">'mat'</span>,<span class="string">'J'</span>)
plot(licro,<span class="string">'range'</span>,[15 15 5],<span class="string">'unit'</span>,<span class="string">'xyz'</span>,<span class="string">'atomMode'</span>,<span class="string">'mag'</span>,<span class="string">'cellMode'</span>,<span class="string">'none'</span>,<span class="string">'atomLegend'</span>,false)
</pre><img vspace="5" hspace="5" src="/tutorial31_04.png" alt=""> <h2 id="12">Single ion properties</h2><p>Assing the A matrix to single ion anisotropy.</p><pre class="codeinput">licro.addaniso(<span class="string">'A'</span>)
plot(licro)
</pre><img vspace="5" hspace="5" src="/tutorial31_05.png" alt=""> <h2 id="13">Magnetic structure</h2><p>Lets start with a simpler lattice: square lattice. Define a (1/2,1/2,0) magnetic structure using complex magnetization vectors.</p><p>What does [1-1i;1+1i;0] vector means? These are the complex magnetization vectors. SpinW 3.0 stores complex magnetization vectors internally and generates the real magnetic structure on the fly.</p><p>How is this stored in the spinw object? check spinw.mag_str and check spinw.magstr for the generated real structure.</p><p>Let's create a magnetic supercell! 2x2x1 cell What will be the k-vector now? (1/2,1/2,0) or (1,1,0)? They are indeed equivalent.</p><p>To check that we are doing the right thing, we will keep track of the enrgy of the system, after adding a J=1 meV Heisenberg exchange on the square lattice. To create Heisenberg Hamiltonian quickly we use square.quickham(1.25), to create the first neighbor bonds with J=1.25 meV.</p><p>What was the energy/spin for the original magnetic structure? S=1, J = 1.25 meV?</p><pre class="codeinput">square = sw_model(<span class="string">'squareAF'</span>);
plot(square,<span class="string">'range'</span>,[2 2 1/2])

square.genmagstr(<span class="string">'mode'</span>,<span class="string">'direct'</span>,<span class="string">'S'</span>,[1-1i;1+1i;0],<span class="string">'k'</span>,[1/2 1/2 0],<span class="string">'nExt'</span>,[1 1 1])
plot(square,<span class="string">'range'</span>,[2 2 1/2])

square.quickham(1)

square.energy

<span class="comment">% Create supercell, which k-vector is right? k is always in the units of</span>
<span class="comment">% the crystal reciprocal lattice!</span>

square.genmagstr(<span class="string">'mode'</span>,<span class="string">'direct'</span>,<span class="string">'S'</span>,[1 -1 -1 1;0 0 0 0;0 0 0 0],<span class="string">'nExt'</span>,[2 2 1],<span class="string">'k'</span>,[0 0 0])
square.energy

square.genmagstr(<span class="string">'mode'</span>,<span class="string">'direct'</span>,<span class="string">'S'</span>,[1 -1 -1 1;0 0 0 0;0 0 0 0],<span class="string">'nExt'</span>,[2 2 1],<span class="string">'k'</span>,[1/2 1/2 0])
square.energy
</pre><pre class="codeoutput">Ground state energy: -2.000 meV/spin.
Ground state energy: -2.000 meV/spin.
Ground state energy: -2.000 meV/spin.
</pre><img vspace="5" hspace="5" src="/tutorial31_06.png" alt=""> <h2 id="14">Rotating frame representation</h2><p>Let's generate a spiral using the J1-J2 model of a zig-zag chain. Check the spinw.mag_str and spinw.magstr and compare them.</p><pre class="codeinput">ch = spinw;
ch.genlattice(<span class="string">'lat_const'</span>,[3 5 4])
ch.addatom(<span class="string">'r'</span>,[0 .3 0],<span class="string">'S'</span>,1)
ch.addatom(<span class="string">'r'</span>,[1/2 0.7 0],<span class="string">'S'</span>,1)
ch.quickham([1 1/2])

ch.optmagk
ch.optmagsteep
ch.energy

plot(ch,<span class="string">'range'</span>,[5 1 1/2])
</pre><pre class="codeoutput">
ans = 

  struct with fields:

       k: [3&times;1 double]
       E: -0.7500
       F: [3&times;2 double]
    stat: [1&times;1 struct]

Warning: Some spins are coupled to themselves in the present magnetic cell! 
Ground state energy: -0.750 meV/spin.
</pre><img vspace="5" hspace="5" src="/tutorial31_07.png" alt=""> <h2 id="15">Let's do some animation by rotating the moments</h2><pre class="codeinput"><span class="keyword">for</span> ii = 1:100
    ch.genmagstr(<span class="string">'mode'</span>,<span class="string">'rotate'</span>,<span class="string">'n'</span>,[0 0 1],<span class="string">'phid'</span>,1)
    swplot.plotmag(<span class="string">'range'</span>,[5 1 1/2])
    drawnow
<span class="keyword">end</span>
</pre><img vspace="5" hspace="5" src="/tutorial31_08.png" alt=""> <h2 id="16">Check the spin wave dispersion</h2><pre class="codeinput">spec = ch.spinwave({[0 0 0] [1 0 0] 501});
spec = sw_egrid(spec);
spec = sw_instrument(spec,<span class="string">'dE'</span>,0.1);
figure
sw_plotspec(spec,<span class="string">'mode'</span>,<span class="string">'color'</span>)
legend <span class="string">off</span>

<span class="comment">% Plot the neutron scattering cross section per spin wave mode.</span>
figure
spec = sw_omegasum(spec,<span class="string">'zeroint'</span>,1e-5,<span class="string">'tol'</span>,1e-3);
sw_plotspec(spec,<span class="string">'mode'</span>,<span class="string">'int'</span>,<span class="string">'axLim'</span>,[0 5],<span class="string">'colormap'</span>,[0 0 0])
</pre><pre class="codeoutput">Warning: To make the Hamiltonian positive definite, a small omega_tol value was
added to its diagonal! 
</pre><img vspace="5" hspace="5" src="/tutorial31_09.png" alt=""> <img vspace="5" hspace="5" src="/tutorial31_10.png" alt=""> <h2 id="17">Case when the rotating frame representation fails</h2><p>We show here what happens when there are counterrotating spirals.</p><pre class="codeinput">ch = spinw;
ch.genlattice(<span class="string">'lat_const'</span>,[3 7 4])
ch.addatom(<span class="string">'r'</span>,[1/2 1/4 0],<span class="string">'S'</span>,1)
ch.addatom(<span class="string">'r'</span>,[1/2 3/4 0],<span class="string">'S'</span>,1)
ch.addmatrix(<span class="string">'label'</span>,<span class="string">'DM1'</span>,<span class="string">'value'</span>,[0  1 0])
ch.addmatrix(<span class="string">'label'</span>,<span class="string">'DM2'</span>,<span class="string">'value'</span>,[0 -1 0])

ch.gencoupling
ch.addcoupling(<span class="string">'mat'</span>,<span class="string">'DM1'</span>,<span class="string">'bond'</span>,1,<span class="string">'subIdx'</span>,1)
ch.addcoupling(<span class="string">'mat'</span>,<span class="string">'DM2'</span>,<span class="string">'bond'</span>,1,<span class="string">'subIdx'</span>,2)

optRes = ch.optmagk;
plot(ch,<span class="string">'range'</span>,[5 1 1/2])

<span class="comment">% Rotating frame representation fails!</span>
ch.magstr

<span class="comment">% Lets check how the structure would look like in a magnetic supercell.</span>
ch.magstr(<span class="string">'nExt'</span>,[4 1 1])

<span class="comment">% Let's generate this supercell and keep it.</span>
ch.genmagstr(<span class="string">'mode'</span>,<span class="string">'helical'</span>,<span class="string">'nExt'</span>,[4 1 1])

<span class="comment">% Let's check the energy if we are right, -1 meV/spin looks fine.</span>
ch.energy
</pre><pre class="codeoutput">Warning: Convergence is not reached! 
Warning: The stored magnetic structure does not have an exact representation in
the rotating frame formalism! 

ans = 

  struct with fields:

        S: [3&times;2 double]
        k: [0.7501 0 0]
        n: [0 1 0]
    N_ext: [1 1 1]
    exact: 0

Warning: The stored magnetic structure does not have an exact representation in
the rotating frame formalism! 

ans = 

  struct with fields:

        S: [3&times;8 double]
        k: [0.7501 0 0]
        n: [0 1 0]
    N_ext: [4 1 1]
    exact: 0

Warning: In the extended unit cell k is still larger than epsilon! 
Warning: The stored magnetic structure does not have an exact representation in
the rotating frame formalism! 
Ground state energy: -1.000 meV/spin.
</pre><img vspace="5" hspace="5" src="/tutorial31_11.png" alt=""> <img vspace="5" hspace="5" src="/tutorial31_12.png" alt=""> <p class="footer"><br><a href="https://www.mathworks.com/products/matlab/">Published with MATLAB&reg; R2018b</a><br></p></div><!--
<literal>##### SOURCE BEGIN #####
%% Internal data structure of SpinW
% Import the LiCrO2 crystal structure from a web link. It has space group
% R-3m, rhombohedrl crystal structure in hexagonal settings.
% What is the density?
% Where does all the data comes from? edit atom.dat
%

%% Get the lattice
licro = spinw('https://raw.githubusercontent.com/SpinW/Models/master/cif/licro2.cif');

licro.formula

%% Check out internal data structure of SpinW
% What do you see?

properties(spinw)

licro.lattice


%% Test cordinate transformations
% Convert (1,1,0) in the reciprocal lattice of LiCrO2 to A^-1 and convert
% (1,0,0) in lattice units to the crystal Descartes coordinate system
% (denoted by xyz in SpinW).
%
% How are Trl and Tr related?
%

Trl = licro.rl;
Q = [0 1 0];
QinvA = Q*Trl

Tl = licro.basisvector;
pos = [1;0;0];
RA = Tl*pos


%% Rotate a vector
% Using the rotation axis and Rotation angle in degree, the sw_rotmatd can
% generate the corresponding rotation matrix.

R = sw_rotmatd([0 0 1],60);

% Rotate polar vector
R*pos

%% Magnetic atoms
% Can you find the magnetic atom positions on the plot and connect them to
% the list in mAtom and in licro.unit_cell?
%

plot(licro)
mAtom = licro.matom

%% Space groups
% Check out symmetry.dat: What does it mean P0~=P1? In case P0 the
% equivalent bonds are determined based on length, while for P1 (or any
% other space group), the equivalent bonds are determined based on the
% symmetry operators.

edit symmetry.dat

%% Bond symmetry
% Generate the bond list of LiCrO2.
% Are the bonds generated usign the space group?
% What does it mean?

licro.gencoupling

% The first neighbor bonds
licro.table('bond',1)

%% Lets do something crazy
% Lets convert the hexagonal cell to the primitive cell and see what
% happens.
%
% Why copy()? The spinw object is handle object, the copy() command creates
% a hard copy to avoid modifying the original object.
% Check spinw.formula() to see how much the new cell is smaller

licroR = copy(licro);
T = licroR.newcell('bvect',{[-1 1 1]/3 [2 1 1]/3 [-1 -2 1]/3})
plot(licroR,'cellMode','outside')
swplot.zoom(1.5)

%% Lets add a few matrices
% What does the different input do? Check the result by inspecting the
% licro.matrix.mat array.

licro.addmatrix('label','J','value',1)
licro.addmatrix('label','D','value',[0 1 0])
licro.addmatrix('label','A','value',diag([1 0.5 0.5]))

%% Lets add some matrices and plot
% Do both for the primitive and the hexagonal cell
% Are they the same?

licroR.gencoupling
licroR.addmatrix('label','J','value',1)
licroR.addcoupling('bond',1,'mat','J')
plot(licroR,'range',[3 3 3],'unit','lu','atomMode','mag','cellMode','none','atomLegend',false)
swplot.zoom(1.5)

%% Plot a single triangular layer from LiCrO2

licro.addcoupling('bond',1,'mat','J')
plot(licro,'range',[15 15 5],'unit','xyz','atomMode','mag','cellMode','none','atomLegend',false)

%% Single ion properties
% Assing the A matrix to single ion anisotropy.

licro.addaniso('A')
plot(licro)

%% Magnetic structure
% Lets start with a simpler lattice: square lattice. Define a (1/2,1/2,0)
% magnetic structure using complex magnetization vectors.
%
% What does [1-1i;1+1i;0] vector means? These are the complex magnetization
% vectors. SpinW 3.0 stores complex magnetization vectors internally and
% generates the real magnetic structure on the fly.
%
% How is this stored in the spinw object? check spinw.mag_str and check
% spinw.magstr for the generated real structure.
%
% Let's create a magnetic supercell! 2x2x1 cell
% What will be the k-vector now? (1/2,1/2,0) or (1,1,0)? They are indeed
% equivalent.
%
% To check that we are doing the right thing, we will keep track of the
% enrgy of the system, after adding a J=1 meV Heisenberg exchange on the
% square lattice.
% To create Heisenberg Hamiltonian quickly we use square.quickham(1.25), to
% create the first neighbor bonds with J=1.25 meV.
%
% What was the energy/spin for the original magnetic structure? S=1, J =
% 1.25 meV?

square = sw_model('squareAF');
plot(square,'range',[2 2 1/2])

square.genmagstr('mode','direct','S',[1-1i;1+1i;0],'k',[1/2 1/2 0],'nExt',[1 1 1])
plot(square,'range',[2 2 1/2])

square.quickham(1)

square.energy

% Create supercell, which k-vector is right? k is always in the units of
% the crystal reciprocal lattice!

square.genmagstr('mode','direct','S',[1 -1 -1 1;0 0 0 0;0 0 0 0],'nExt',[2 2 1],'k',[0 0 0])
square.energy

square.genmagstr('mode','direct','S',[1 -1 -1 1;0 0 0 0;0 0 0 0],'nExt',[2 2 1],'k',[1/2 1/2 0])
square.energy

%% Rotating frame representation
% Let's generate a spiral using the J1-J2 model of a zig-zag chain. Check
% the spinw.mag_str and spinw.magstr and compare them.

ch = spinw;
ch.genlattice('lat_const',[3 5 4])
ch.addatom('r',[0 .3 0],'S',1)
ch.addatom('r',[1/2 0.7 0],'S',1)
ch.quickham([1 1/2])

ch.optmagk
ch.optmagsteep
ch.energy

plot(ch,'range',[5 1 1/2])

%% Let's do some animation by rotating the moments

for ii = 1:100
    ch.genmagstr('mode','rotate','n',[0 0 1],'phid',1)
    swplot.plotmag('range',[5 1 1/2])
    drawnow
end

%% Check the spin wave dispersion

spec = ch.spinwave({[0 0 0] [1 0 0] 501});
spec = sw_egrid(spec);
spec = sw_instrument(spec,'dE',0.1);
figure
sw_plotspec(spec,'mode','color')
legend off

% Plot the neutron scattering cross section per spin wave mode.
figure
spec = sw_omegasum(spec,'zeroint',1e-5,'tol',1e-3);
sw_plotspec(spec,'mode','int','axLim',[0 5],'colormap',[0 0 0])

%% Case when the rotating frame representation fails
% We show here what happens when there are counterrotating spirals.

ch = spinw;
ch.genlattice('lat_const',[3 7 4])
ch.addatom('r',[1/2 1/4 0],'S',1)
ch.addatom('r',[1/2 3/4 0],'S',1)
ch.addmatrix('label','DM1','value',[0  1 0])
ch.addmatrix('label','DM2','value',[0 -1 0])

ch.gencoupling
ch.addcoupling('mat','DM1','bond',1,'subIdx',1)
ch.addcoupling('mat','DM2','bond',1,'subIdx',2)

optRes = ch.optmagk;
plot(ch,'range',[5 1 1/2])

% Rotating frame representation fails!
ch.magstr

% Lets check how the structure would look like in a magnetic supercell.
ch.magstr('nExt',[4 1 1])

% Let's generate this supercell and keep it.
ch.genmagstr('mode','helical','nExt',[4 1 1])

% Let's check the energy if we are right, -1 meV/spin looks fine.
ch.energy


##### SOURCE END #####</literal>
-->