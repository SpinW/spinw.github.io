---
layout: tutorial
title: Tutorial 9
subtitle: k=0 Kagome antiferromagnet with DM interaction
---

<div class="content"><h1>k=0 Kagome antiferromagnet with DM interaction</h1><!--introduction--><p>We create the lattice with 'P -3' space group and magnetic Cu+ with S=1 spin.</p><!--/introduction--><h2>Contents</h2><div><ul><li><a href="#1">Define the lattice</a></li><li><a href="#2">Create bonds and Hamiltonian</a></li><li><a href="#3">Generate magnetic structure</a></li><li><a href="#4">Calculate spin wave dispersion</a></li><li><a href="#5">Powder spectrum</a></li></ul></div><h2 id="1">Define the lattice</h2><pre class="codeinput">DMkag = spinw;
DMkag.genlattice(<span class="string">'lat_const'</span>,[6 6 40],<span class="string">'angled'</span>,[90 90 120],<span class="string">'spgr'</span>,<span class="string">'P -3'</span>)
DMkag.addatom(<span class="string">'r'</span>, [1/2 0 0],<span class="string">'S'</span>,1,<span class="string">'label'</span>, <span class="string">'Cu1'</span>, <span class="string">'color'</span>,<span class="string">'r'</span>)
plot(DMkag,<span class="string">'range'</span>,[2 2 1])
swplot.zoom(4)
</pre> <img vspace="5" hspace="5" src="/tutorial9_02.png" alt=""> <h2 id="2">Create bonds and Hamiltonian</h2><p>Generate the list of bonds and assign a Heisenberg exchange and weak Dzyaloshinskii-Moriya interaction to the fisrt neighbor bonds. The DM interaction vector can be easily created using the spinw.setmatrix function. The corresponding spinw.getmatrix method determines the symmetry allowed components of the DM vector. On the structure plot, the DM interaction vector is symbolized by a vector in the middle of the bond, pointing in the direction of the DM vector. Also important that the bonds are directional, that is shown by the arrows pointing from one atom to another. If one changes the direction of a bond, the corresponding DM vector has to be flipped as well.</p><pre class="codeinput">DMkag.gencoupling(<span class="string">'maxDistance'</span>,7)
DMkag.addmatrix(<span class="string">'label'</span>,<span class="string">'DM1'</span>,<span class="string">'value'</span>,1,<span class="string">'color'</span>,<span class="string">'b'</span>)
DMkag.addmatrix(<span class="string">'label'</span>,<span class="string">'J1'</span>,<span class="string">'value'</span>,1,<span class="string">'color'</span>,<span class="string">'g'</span>)
DMkag.addcoupling(<span class="string">'mat'</span>,<span class="string">'DM1'</span>,<span class="string">'bond'</span>,1)
DMkag.addcoupling(<span class="string">'mat'</span>,<span class="string">'J1'</span>,<span class="string">'bond'</span>,1)
DMkag.setmatrix(<span class="string">'mat'</span>,<span class="string">'DM1'</span>,<span class="string">'pref'</span>,{[0 0 -0.08]});
plot(DMkag,<span class="string">'range'</span>,[3 3 1/2])
swplot.zoom(1.2)
DMkag.table(<span class="string">'mat'</span>)
</pre><pre class="codeoutput">
ans =

  2&times;6 table

    matrix            Mx                      My                 Mz              type          assigned
    ______    ___________________    ____________________    ___________    _______________    ________

    'DM1'     0    -0.08        0    0.08       0       0    0    0    0    'antisymmetric'     'bond' 
    'J1'      1        0        0       0       1       0    0    0    1    'Heisenberg'        'bond' 

</pre><img vspace="5" hspace="5" src="/tutorial9_03.png" alt=""> <h2 id="3">Generate magnetic structure</h2><p>We create a k = (0 0 0) magnetic structure, with the three spin directions in the unit cell (120 degree between neighbors). The spin vector components are given in the coordinate system of the lattice vectors (abc) and spinw.genmagstr normalizes the moment length to the previously given spin quantum number in the spinw.addatom method.</p><pre class="codeinput">S0 = [1 -2 1; 2 -1 -1; 0 0 0];
DMkag.genmagstr(<span class="string">'mode'</span>,<span class="string">'direct'</span>,<span class="string">'k'</span>,[0 0 0],<span class="string">'n'</span>,[0 0 1],<span class="string">'unit'</span>,<span class="string">'lu'</span>, <span class="string">'S'</span>,S0);
DMkag.energy

plot(DMkag,<span class="string">'range'</span>,[3 3 1/2])
</pre><pre class="codeoutput">Ground state energy: -1.139 meV/spin.
</pre><img vspace="5" hspace="5" src="/tutorial9_04.png" alt=""> <h2 id="4">Calculate spin wave dispersion</h2><pre class="codeinput">Qlist = {[-1/2 0 0] [0 0 0] [1/2 1/2 0] 100};
dmkSpec = DMkag.spinwave(Qlist,<span class="string">'hermit'</span>,false);
figure
sw_plotspec(dmkSpec,<span class="string">'mode'</span>,1,<span class="string">'axLim'</span>,[0 3],<span class="string">'colorbar'</span>,false,<span class="keyword">...</span>
    <span class="string">'colormap'</span>,[0 0 0],<span class="string">'dashed'</span>,true)
</pre><img vspace="5" hspace="5" src="/tutorial9_05.png" alt=""> <h2 id="5">Powder spectrum</h2><p>The flat mode that is the zero energy mode lifted by the DM interaction is well visible on the powder spectrum.</p><pre class="codeinput">dmkPow = DMkag.powspec(linspace(0,2.5,150),<span class="string">'Evect'</span>,linspace(0,3,250),<span class="keyword">...</span>
    <span class="string">'nRand'</span>,1e3,<span class="string">'hermit'</span>,false,<span class="string">'imagChk'</span>,false);
figure
sw_plotspec(dmkPow,<span class="string">'axLim'</span>,[0 0.5],<span class="string">'dE'</span>,0.02)
</pre><img vspace="5" hspace="5" src="/tutorial9_06.png" alt=""> <pre>Written by
Bjorn Fak &amp; Sandor Toth
06-Jun-2014, 06-Feb-2017</pre><p class="footer"><br><a href="https://www.mathworks.com/products/matlab/">Published with MATLAB&reg; R2018b</a><br></p></div><!--
<literal>##### SOURCE BEGIN #####
%% k=0 Kagome antiferromagnet with DM interaction
% We create the lattice with 'P -3' space group and magnetic Cu+ with S=1
% spin.

%% Define the lattice
DMkag = spinw;
DMkag.genlattice('lat_const',[6 6 40],'angled',[90 90 120],'spgr','P -3')
DMkag.addatom('r', [1/2 0 0],'S',1,'label', 'Cu1', 'color','r')
plot(DMkag,'range',[2 2 1])
swplot.zoom(4)

%% Create bonds and Hamiltonian
% Generate the list of bonds and assign a Heisenberg exchange and weak
% Dzyaloshinskii-Moriya interaction to the fisrt neighbor bonds. The DM
% interaction vector can be easily created using the spinw.setmatrix
% function. The corresponding spinw.getmatrix method determines the
% symmetry allowed components of the DM vector. On the structure plot, the
% DM interaction vector is symbolized by a vector in the middle of the
% bond, pointing in the direction of the DM vector. Also important that the
% bonds are directional, that is shown by the arrows pointing from one atom
% to another. If one changes the direction of a bond, the corresponding DM
% vector has to be flipped as well.

DMkag.gencoupling('maxDistance',7)
DMkag.addmatrix('label','DM1','value',1,'color','b')
DMkag.addmatrix('label','J1','value',1,'color','g')
DMkag.addcoupling('mat','DM1','bond',1)
DMkag.addcoupling('mat','J1','bond',1)
DMkag.setmatrix('mat','DM1','pref',{[0 0 -0.08]});
plot(DMkag,'range',[3 3 1/2])
swplot.zoom(1.2)
DMkag.table('mat')

%% Generate magnetic structure
% We create a k = (0 0 0) magnetic structure, with the three spin
% directions in the unit cell (120 degree between neighbors). The spin
% vector components are given in the coordinate system of the lattice
% vectors (abc) and spinw.genmagstr normalizes the moment length to the
% previously given spin quantum number in the spinw.addatom method.

S0 = [1 -2 1; 2 -1 -1; 0 0 0];
DMkag.genmagstr('mode','direct','k',[0 0 0],'n',[0 0 1],'unit','lu', 'S',S0); 
DMkag.energy

plot(DMkag,'range',[3 3 1/2])

%% Calculate spin wave dispersion

Qlist = {[-1/2 0 0] [0 0 0] [1/2 1/2 0] 100};
dmkSpec = DMkag.spinwave(Qlist,'hermit',false);
figure
sw_plotspec(dmkSpec,'mode',1,'axLim',[0 3],'colorbar',false,...
    'colormap',[0 0 0],'dashed',true)


%% Powder spectrum
% The flat mode that is the zero energy mode lifted by the DM interaction
% is well visible on the powder spectrum.

dmkPow = DMkag.powspec(linspace(0,2.5,150),'Evect',linspace(0,3,250),...
    'nRand',1e3,'hermit',false,'imagChk',false);
figure
sw_plotspec(dmkPow,'axLim',[0 0.5],'dE',0.02)

%%
%  Written by
%  Bjorn Fak & Sandor Toth
%  06-Jun-2014, 06-Feb-2017
##### SOURCE END #####</literal>
-->
