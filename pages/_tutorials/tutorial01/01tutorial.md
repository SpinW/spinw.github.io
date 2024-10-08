---
layout: tutorial
title: Tutorial 1
subtitle: Spin wave spectrum of the Heisenberg ferromagnetic nearest-neighbor spin chain
---

<div class="content"><h1>Spin wave spectrum of the Heisenberg ferromagnetic nearest-neighbor spin chain</h1><!--introduction--><p>The following tutorial shows every step necessary to calculate spin wave spectrum through the simple example of the ferromagnetic spin chain</p><!--/introduction--><h2>Contents</h2><div><ul><li><a href="#1">Define spin chain with magnetic atoms</a></li><li><a href="#2">Determine the list of bonds based on length</a></li><li><a href="#3">Defining the spin Hamiltonian</a></li><li><a href="#4">Definition of FM magnetic structure</a></li><li><a href="#5">The energy of the ground state per spin</a></li><li><a href="#6">Calculate spin wave dispersion and spin-spin correlation function</a></li><li><a href="#7">Calculate powder average spectrum</a></li></ul></div><h2 id="1">Define spin chain with magnetic atoms</h2><p>The shortest lattice parameter along the a-axis will give the first neighbor bonds along this axis. After defining the lattice, we add a magnetic Cu+ ion with spin S=1 at the origin of the unit cell and plot the lattice.</p><pre class="codeinput">FMchain = spinw;
FMchain.genlattice(<span class="string">'lat_const'</span>,[3 8 8],<span class="string">'angled'</span>,[90 90 90])
FMchain.addatom(<span class="string">'r'</span>, [0 0 0],<span class="string">'S'</span>, 1,<span class="string">'label'</span>,<span class="string">'MCu1'</span>,<span class="string">'color'</span>,<span class="string">'blue'</span>)
FMchain.plot(<span class="string">'range'</span>,[3 1 1])
</pre> <img vspace="5" hspace="5" src="/tutorial1_02.png" alt=""> <h2 id="2">Determine the list of bonds based on length</h2><p>To consider bonds up to 7 Angstrom length we use the sw.gencoupling() function. Since no symmetry operators are defined, it sorts all bonds according to increasing length, all bonds are equivalent that has the same length within an error bar (0.001 Angstrom by default).</p><pre class="codeinput">FMchain.gencoupling(<span class="string">'maxDistance'</span>,7)

<span class="comment">% list the 1st and 2nd neighbor bonds</span>
FMchain.table(<span class="string">'bond'</span>,1:2)
</pre><pre class="codeoutput">
ans =

  2&times;10 table

    idx    subidx        dl             dr         length    matom1    idx1    matom2    idx2        matrix    
    ___    ______    ___________    ___________    ______    ______    ____    ______    ____    ______________

     1       1       1    0    0    1    0    0      3       'MCu1'     1      'MCu1'     1      ''    ''    ''
     2       1       2    0    0    2    0    0      6       'MCu1'     1      'MCu1'     1      ''    ''    ''

</pre><h2 id="3">Defining the spin Hamiltonian</h2><p>We create a matrix with a label 'Ja', ferromagnetic heisenberg interaction, J = -1 meV and assing it to the first neghbor bonds as spin-spin exchange interaction: J*S(i)*S(i+1). And plot the crystal structure with the added bonds.</p><pre class="codeinput">FMchain.addmatrix(<span class="string">'value'</span>,-eye(3),<span class="string">'label'</span>,<span class="string">'Ja'</span>,<span class="string">'color'</span>,<span class="string">'green'</span>)
FMchain.addcoupling(<span class="string">'mat'</span>,<span class="string">'Ja'</span>,<span class="string">'bond'</span>,1);
plot(FMchain,<span class="string">'range'</span>,[3 0.2 0.2],<span class="string">'cellMode'</span>,<span class="string">'none'</span>,<span class="string">'baseMode'</span>,<span class="string">'none'</span>)
</pre><img vspace="5" hspace="5" src="/tutorial1_03.png" alt=""> <h2 id="4">Definition of FM magnetic structure</h2><p>The classical magnetic ground state of the previously defined Hamiltonian is where every spin have the same direction, the direction is arbitrary since the Hamiltonian is isotropic. We use the following parameters:</p><div><ul><li>magnetic ordering wave vector k = (0 0 0)</li><li>there is a single spin per unit cell S = [0 1 0]</li><li>an arbitrary normal vector to the spin n = [1 0 0]</li></ul></div><pre class="codeinput">FMchain.genmagstr(<span class="string">'mode'</span>,<span class="string">'direct'</span>, <span class="string">'k'</span>,[0 0 0],<span class="string">'n'</span>,[1 0 0],<span class="string">'S'</span>,[0; 1; 0]);

disp(<span class="string">'Magnetic structure:'</span>)
FMchain.table(<span class="string">'mag'</span>)
plot(FMchain,<span class="string">'range'</span>,[3 0.9 0.9],<span class="string">'baseMode'</span>,<span class="string">'none'</span>,<span class="string">'cellMode'</span>,<span class="string">'none'</span>)
</pre><pre class="codeoutput">Magnetic structure:

ans =

  1&times;7 table

    num    matom     idx    S     realFhat          pos           kvect   
    ___    ______    ___    _    ___________    ___________    ___________

     1     'MCu1'     1     1    0    1    0    0    0    0    0    0    0

</pre><img vspace="5" hspace="5" src="/tutorial1_04.png" alt=""> <h2 id="5">The energy of the ground state per spin</h2><p>The spinw.energy() function gives the ground state energy per spin, the value is dinamically calculated at every call.</p><pre class="codeinput">FMchain.energy
assert(FMchain.energy == -1)
</pre><pre class="codeoutput">Ground state energy: -1.000 meV/spin.
</pre><h2 id="6">Calculate spin wave dispersion and spin-spin correlation function</h2><p>We calculate spin wave dispersion and correlation function along the chain, momentum transfer value is Q = (H 0 0). Then we calculate the neutron scattering cross section and select 'Sperp' the neutron scattering intensity for plotting. Then we plot spin wave dispersion and the value of the correlation function with the 1-Q^2 neutron scattering cross section in units of hbar/spin.</p><pre class="codeinput">FMspec = FMchain.spinwave({[0 0 0] [1 0 0]},<span class="string">'hermit'</span>,false);
FMspec = sw_neutron(FMspec);
FMspec = sw_egrid(FMspec,<span class="string">'component'</span>,<span class="string">'Sperp'</span>);

figure;
subplot(2,1,1)
sw_plotspec(FMspec,<span class="string">'mode'</span>,1,<span class="string">'colorbar'</span>,false)
axis([0 1 0 5])
subplot(2,1,2)
sw_plotspec(FMspec,<span class="string">'mode'</span>,2)
axis([0 1 0 2])
swplot.subfigure(1,3,1)
</pre><img vspace="5" hspace="5" src="/tutorial1_05.png" alt=""> <h2 id="7">Calculate powder average spectrum</h2><p>We calculate powder spectrum for Q = 0:2.5 Angstrom^-1 100 steps resolution 1000 random Q points for every step. Then we plot the spectrum convoluted with 0.1 meV Gaussian along energy.</p><pre class="codeinput">FMpowspec = FMchain.powspec(linspace(0,2.5,100),<span class="string">'Evect'</span>,linspace(0,4.5,250),<span class="string">'nRand'</span>,1000,<span class="string">'hermit'</span>,false);
figure;
sw_plotspec(FMpowspec,<span class="string">'dE'</span>,0.1)
axis([0 2.5 0 4.5]);
caxis([0 .05]);
</pre><img vspace="5" hspace="5" src="/tutorial1_06.png" alt=""> <pre>Written by
Bjorn Fak &amp; Sandor Toth
06-June-2014, 06-Feb-2017</pre><p class="footer"><br><a href="https://www.mathworks.com/products/matlab/">Published with MATLAB&reg; R2018b</a><br></p></div><!--
<literal>##### SOURCE BEGIN #####
%% Spin wave spectrum of the Heisenberg ferromagnetic nearest-neighbor spin chain 
% The following tutorial shows every step necessary to calculate spin wave
% spectrum through the simple example of the ferromagnetic spin chain

%% Define spin chain with magnetic atoms
% The shortest lattice parameter along the a-axis will give the first
% neighbor bonds along this axis. After defining the lattice, we add a
% magnetic Cu+ ion with spin S=1 at the origin of the unit cell and plot
% the lattice.

FMchain = spinw; 
FMchain.genlattice('lat_const',[3 8 8],'angled',[90 90 90])
FMchain.addatom('r', [0 0 0],'S', 1,'label','MCu1','color','blue')
FMchain.plot('range',[3 1 1])

%% Determine the list of bonds based on length
% To consider bonds up to 7 Angstrom length we use the sw.gencoupling()
% function. Since no symmetry operators are defined, it sorts all bonds
% according to increasing length, all bonds are equivalent that has the
% same length within an error bar (0.001 Angstrom by default).

FMchain.gencoupling('maxDistance',7)

% list the 1st and 2nd neighbor bonds
FMchain.table('bond',1:2)

%% Defining the spin Hamiltonian
% We create a matrix with a label 'Ja', ferromagnetic heisenberg
% interaction, J = -1 meV and assing it to the first neghbor bonds as
% spin-spin exchange interaction: J*S(i)*S(i+1). And plot the crystal
% structure with the added bonds.
 
FMchain.addmatrix('value',-eye(3),'label','Ja','color','green')
FMchain.addcoupling('mat','Ja','bond',1);
plot(FMchain,'range',[3 0.2 0.2],'cellMode','none','baseMode','none')

%% Definition of FM magnetic structure
% The classical magnetic ground state of the previously defined Hamiltonian
% is where every spin have the same direction, the direction is arbitrary
% since the Hamiltonian is isotropic. We use the following parameters:
%
% * magnetic ordering wave vector k = (0 0 0)
% * there is a single spin per unit cell S = [0 1 0]
% * an arbitrary normal vector to the spin n = [1 0 0]
%

FMchain.genmagstr('mode','direct', 'k',[0 0 0],'n',[1 0 0],'S',[0; 1; 0]); 

disp('Magnetic structure:')
FMchain.table('mag')
plot(FMchain,'range',[3 0.9 0.9],'baseMode','none','cellMode','none')

%% The energy of the ground state per spin
% The spinw.energy() function gives the ground state energy per spin, the
% value is dinamically calculated at every call.

FMchain.energy
assert(FMchain.energy == -1)

%% Calculate spin wave dispersion and spin-spin correlation function
% We calculate spin wave dispersion and correlation function along the
% chain, momentum transfer value is Q = (H 0 0). Then we calculate the
% neutron scattering cross section and select 'Sperp' the neutron
% scattering intensity for plotting. Then we plot spin wave dispersion and
% the value of the correlation function with the 1-Q^2 neutron scattering
% cross section in units of hbar/spin.

FMspec = FMchain.spinwave({[0 0 0] [1 0 0]},'hermit',false);
FMspec = sw_neutron(FMspec); 
FMspec = sw_egrid(FMspec,'component','Sperp');

figure;
subplot(2,1,1)
sw_plotspec(FMspec,'mode',1,'colorbar',false)  
axis([0 1 0 5])
subplot(2,1,2)
sw_plotspec(FMspec,'mode',2)  
axis([0 1 0 2])
swplot.subfigure(1,3,1)

%% Calculate powder average spectrum
% We calculate powder spectrum for Q = 0:2.5 Angstrom^-1 100 steps
% resolution 1000 random Q points for every step. Then we plot the spectrum
% convoluted with 0.1 meV Gaussian along energy.

FMpowspec = FMchain.powspec(linspace(0,2.5,100),'Evect',linspace(0,4.5,250),'nRand',1000,'hermit',false);
figure;
sw_plotspec(FMpowspec,'dE',0.1)
axis([0 2.5 0 4.5]);
caxis([0 .05]);

%%
%  Written by
%  Bjorn Fak & Sandor Toth
%  06-June-2014, 06-Feb-2017
##### SOURCE END #####</literal>
-->
