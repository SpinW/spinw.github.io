---
layout: tutorial
title: Tutorial 3
subtitle: Frustrated J1-J2 AFM chain
---

<div class="content"><h1>Frustrated J1-J2 AFM chain</h1><!--introduction--><p>Crystal structure, shortest bond along a-axis, Cu+ magnetic atoms with S=1 spin.</p><!--/introduction--><h2>Contents</h2><div><ul><li><a href="#1">Define the lattice</a></li><li><a href="#2">Couplings</a></li><li><a href="#3">Magnetic structure is a helix</a></li><li><a href="#4">Direct input</a></li><li><a href="#5">We optimise the helix pitch angle</a></li><li><a href="#6">Spin wave spectrum</a></li></ul></div><h2 id="1">Define the lattice</h2><pre class="codeinput">J1J2chain = spinw;
J1J2chain.genlattice(<span class="string">'lat_const'</span>,[3 8 10],<span class="string">'angled'</span>,[90 90 90],<span class="string">'spgr'</span>,0);
J1J2chain.addatom(<span class="string">'r'</span>,[0 0 0],<span class="string">'S'</span>,1,<span class="string">'label'</span>,<span class="string">'Cu1'</span>,<span class="string">'color'</span>,<span class="string">'blue'</span>);
disp(<span class="string">'Magnetic lattice:'</span>)
J1J2chain.table(<span class="string">'atom'</span>)
plot(J1J2chain,<span class="string">'range'</span>,[3 1 1],<span class="string">'zoom'</span>,0.5)
</pre><pre class="codeoutput">Magnetic lattice:

ans =

  1&times;4 table

    matom    idx    S        pos    
    _____    ___    _    ___________

    'Cu1'     1     1    0    0    0

</pre> <img vspace="5" hspace="5" src="/tutorial3_02.png" alt=""> <h2 id="2">Couplings</h2><p>First and second neighbor antiferromagnetic couplings. If the name of the matrix ends with '-' the bond is plotted with dashed line.</p><pre class="codeinput">J1J2chain.gencoupling(<span class="string">'maxDistance'</span>,7);
disp(<span class="string">'Bonds:'</span>)
J1J2chain.table(<span class="string">'bond'</span>,[])

J1J2chain.addmatrix(<span class="string">'label'</span>,<span class="string">'J1'</span>, <span class="string">'value'</span>,-1,<span class="string">'color'</span>,<span class="string">'r'</span>);
J1J2chain.addmatrix(<span class="string">'label'</span>,<span class="string">'J2-'</span>,<span class="string">'value'</span>, 2,<span class="string">'color'</span>,<span class="string">'g'</span>);

J1J2chain.addcoupling(<span class="string">'mat'</span>,<span class="string">'J1'</span>,<span class="string">'bond'</span>,1);
J1J2chain.addcoupling(<span class="string">'mat'</span>,<span class="string">'J2-'</span>,<span class="string">'bond'</span>,2);
plot(J1J2chain,<span class="string">'range'</span>,[3 0.9 0.9],<span class="string">'bondMode'</span>,<span class="string">'line'</span>,<span class="string">'bondLinewidth0'</span>,3)
</pre><pre class="codeoutput">Bonds:

ans =

  2&times;10 table

    idx    subidx        dl             dr         length    matom1    idx1    matom2    idx2        matrix    
    ___    ______    ___________    ___________    ______    ______    ____    ______    ____    ______________

     1       1       1    0    0    1    0    0      3       'Cu1'      1      'Cu1'      1      ''    ''    ''
     2       1       2    0    0    2    0    0      6       'Cu1'      1      'Cu1'      1      ''    ''    ''

</pre><img vspace="5" hspace="5" src="/tutorial3_03.png" alt=""> <h2 id="3">Magnetic structure is a helix</h2><p>We use two different methods to define the ground state magnetic structure:</p><h2 id="4">Direct input</h2><p>If we would know the exact solution of the spin Hamiltonian we can input that, assuming a helix with the following parameters:</p><div><ul><li>magnetic ordering wave vector k = (1/4 0 0)</li><li>spins lying in arbitrary plane, first spin S = (1 0 0)</li><li>normal to the plane of the spin helix has to be perpendicular to S, we choose it n = (0 0 1)</li><li>we won't use a magnetic supercell, not necessary</li></ul></div><pre class="codeinput">J1J2chain.genmagstr(<span class="string">'mode'</span>,<span class="string">'helical'</span>, <span class="string">'k'</span>,[0.25 0 0], <span class="string">'n'</span>,[0 0 1], <span class="string">'S'</span>,[1; 0; 0], <span class="string">'nExt'</span>,[1 1 1])
disp(<span class="string">'Magnetic structure:'</span>)
J1J2chain.table(<span class="string">'mag'</span>)
disp(<span class="string">'Ground state energy before optimization:'</span>)
J1J2chain.energy

plot(J1J2chain,<span class="string">'range'</span>,[3 0.9 0.9])
</pre><pre class="codeoutput">Magnetic structure:

ans =

  1&times;8 table

    num    matom    idx    S     realFhat       imagFhat          pos               kvect        
    ___    _____    ___    _    ___________    ___________    ___________    ____________________

     1     'Cu1'     1     1    1    0    0    0    1    0    0    0    0    0.25       0       0

Ground state energy before optimization:
Ground state energy: -2.000 meV/spin.
</pre><img vspace="5" hspace="5" src="/tutorial3_04.png" alt=""> <h2 id="5">We optimise the helix pitch angle</h2><p>We are unsure about the right pitch angle of the helix, thus we want to calculate it. The sw.optmagstr() is able to determine the magnetic ground state. It uses a constraint function (@gm_planar in this case) to reduce the number of paramteres that has to be optimised. It works well if the number of free parameters are low. we will find the the right k-vector is 0.2301.</p><pre class="codeinput"><span class="comment">%     Phi1 k_x k_y k_z nTheta nPhi</span>
x1 = [0      0   0   0      0    0];
x2 = [0    1/2   0   0      0    0];
optRes = J1J2chain.optmagstr(<span class="string">'func'</span>,@gm_planar,<span class="string">'xmin'</span>,x1,<span class="string">'xmax'</span>,x2,<span class="string">'nRun'</span>,10);
disp(<span class="string">'Ground state energy after optimization'</span>)
J1J2chain.energy
disp(<span class="string">'Optimized magnetic structure:'</span>)
J1J2chain.table(<span class="string">'mag'</span>)

plot(J1J2chain,<span class="string">'range'</span>,[3 0.9 0.9],<span class="string">'bondMode'</span>,<span class="string">'line'</span>,<span class="string">'bondLineWidth0'</span>,3)
</pre><pre class="codeoutput">Ground state energy after optimization
Ground state energy: -2.062 meV/spin.
Optimized magnetic structure:

ans =

  1&times;8 table

    num    matom    idx    S     realFhat       imagFhat          pos                    kvect            
    ___    _____    ___    _    ___________    ___________    ___________    _____________________________

     1     'Cu1'     1     1    1    0    0    0    1    0    0    0    0    0.23005          0          0

</pre><img vspace="5" hspace="5" src="/tutorial3_05.png" alt=""> <h2 id="6">Spin wave spectrum</h2><p>We calculate the spin wave spectrum, the code automatically uses the method that enables the spin wave calculation of incommensurate structures withouth creating a magnetic supercell. There are three spin wave modes, these are omega(Q), omega(Q+/-k). The two shifted ones are due to the incommensurate structure.</p><pre class="codeinput">J1J2spec= J1J2chain.spinwave({[0 0 0] [1 0 0] 400}, <span class="string">'hermit'</span>,false);
J1J2spec = sw_neutron(J1J2spec);
J1J2spec = sw_egrid(J1J2spec, <span class="string">'Evect'</span>,linspace(0,6.5,100));
figure
sw_plotspec(J1J2spec, <span class="string">'mode'</span>,1,<span class="string">'colorbar'</span>,false)
axis([0 1 0 6])
</pre><pre class="codeoutput">Warning: Eigenvectors of defective eigenvalues cannot be orthogonalised at some
q-point! 
</pre><img vspace="5" hspace="5" src="/tutorial3_06.png" alt=""> <pre>Written by
Bjorn Fak &amp; Sandor Toth
06-Jun-2014, 06-Feb-2017</pre><p class="footer"><br><a href="https://www.mathworks.com/products/matlab/">Published with MATLAB&reg; R2018b</a><br></p></div><!--
<literal>##### SOURCE BEGIN #####
%% Frustrated J1-J2 AFM chain
% Crystal structure, shortest bond along a-axis, Cu+ magnetic atoms with
% S=1 spin.

%% Define the lattice
J1J2chain = spinw; 
J1J2chain.genlattice('lat_const',[3 8 10],'angled',[90 90 90],'spgr',0);
J1J2chain.addatom('r',[0 0 0],'S',1,'label','Cu1','color','blue');
disp('Magnetic lattice:')
J1J2chain.table('atom')
plot(J1J2chain,'range',[3 1 1],'zoom',0.5)

%% Couplings
% First and second neighbor antiferromagnetic couplings. If the name of the
% matrix ends with '-' the bond is plotted with dashed line.

J1J2chain.gencoupling('maxDistance',7); 
disp('Bonds:')
J1J2chain.table('bond',[])

J1J2chain.addmatrix('label','J1', 'value',-1,'color','r');
J1J2chain.addmatrix('label','J2-','value', 2,'color','g'); 

J1J2chain.addcoupling('mat','J1','bond',1);
J1J2chain.addcoupling('mat','J2-','bond',2);
plot(J1J2chain,'range',[3 0.9 0.9],'bondMode','line','bondLinewidth0',3)

%% Magnetic structure is a helix
% We use two different methods to define the ground state magnetic
% structure:
%%% Direct input
% If we would know the exact solution of the spin Hamiltonian we can input
% that, assuming a helix with the following parameters:
%
% * magnetic ordering wave vector k = (1/4 0 0)
% * spins lying in arbitrary plane, first spin S = (1 0 0)
% * normal to the plane of the spin helix has to be perpendicular to S, we
% choose it n = (0 0 1)
% * we won't use a magnetic supercell, not necessary
%

J1J2chain.genmagstr('mode','helical', 'k',[0.25 0 0], 'n',[0 0 1], 'S',[1; 0; 0], 'nExt',[1 1 1])
disp('Magnetic structure:')
J1J2chain.table('mag')
disp('Ground state energy before optimization:')
J1J2chain.energy

plot(J1J2chain,'range',[3 0.9 0.9])

%% We optimise the helix pitch angle
% We are unsure about the right pitch angle of the helix, thus we want to
% calculate it. The sw.optmagstr() is able to determine the magnetic ground
% state. It uses a constraint function (@gm_planar in this case) to reduce
% the number of paramteres that has to be optimised. It works well if the
% number of free parameters are low. we will find the the right k-vector is
% 0.2301.

%     Phi1 k_x k_y k_z nTheta nPhi
x1 = [0      0   0   0      0    0];
x2 = [0    1/2   0   0      0    0];
optRes = J1J2chain.optmagstr('func',@gm_planar,'xmin',x1,'xmax',x2,'nRun',10);
disp('Ground state energy after optimization')
J1J2chain.energy
disp('Optimized magnetic structure:')
J1J2chain.table('mag')

plot(J1J2chain,'range',[3 0.9 0.9],'bondMode','line','bondLineWidth0',3)

%% Spin wave spectrum
% We calculate the spin wave spectrum, the code automatically uses the
% method that enables the spin wave calculation of incommensurate
% structures withouth creating a magnetic supercell. There are three spin
% wave modes, these are omega(Q), omega(Q+/-k). The two shifted ones are
% due to the incommensurate structure.

J1J2spec= J1J2chain.spinwave({[0 0 0] [1 0 0] 400}, 'hermit',false);
J1J2spec = sw_neutron(J1J2spec); 
J1J2spec = sw_egrid(J1J2spec, 'Evect',linspace(0,6.5,100));
figure
sw_plotspec(J1J2spec, 'mode',1,'colorbar',false)  
axis([0 1 0 6])

%%
%  Written by
%  Bjorn Fak & Sandor Toth
%  06-Jun-2014, 06-Feb-2017
##### SOURCE END #####</literal>
-->
