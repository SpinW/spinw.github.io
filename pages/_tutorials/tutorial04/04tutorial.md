---
layout: tutorial
title: Tutorial 4
subtitle: Antiferromagnetic square lattice
---

<div class="content"><h1>Antiferromagnetic square lattice</h1><!--introduction--><p>We define a square lattice in the ab plane, with Cu+ ions with S=1 spin.</p><!--/introduction--><h2>Contents</h2><div><ul><li><a href="#1">Define the lattice</a></li><li><a href="#2">Couplings</a></li><li><a href="#3">Magnetic structure</a></li><li><a href="#4">Spin wave spectrum</a></li></ul></div><h2 id="1">Define the lattice</h2><pre class="codeinput">AFsq = spinw;
AFsq.genlattice(<span class="string">'lat_const'</span>,[3 3 6],<span class="string">'angled'</span>,[90 90 90],<span class="string">'spgr'</span>,0)
AFsq.addatom(<span class="string">'r'</span>,[0 0 0],<span class="string">'S'</span>, 1,<span class="string">'label'</span>,<span class="string">'Cu1'</span>,<span class="string">'color'</span>,<span class="string">'b'</span>)
AFsq.table(<span class="string">'atom'</span>)
plot(AFsq)
swplot.zoom(1.5)
</pre><pre class="codeoutput">
ans =

  1&times;4 table

    matom    idx    S        pos    
    _____    ___    _    ___________

    'Cu1'     1     1    0    0    0

</pre> <img vspace="5" hspace="5" src="/tutorial4_02.png" alt=""> <h2 id="2">Couplings</h2><p>We create first neighbor couplings in the ab plane and plot the bonds. You can click on the different bonds to get the value of the corresponding matrix.</p><pre class="codeinput">AFsq.gencoupling(<span class="string">'maxDistance'</span>,5)
AFsq.table(<span class="string">'bond'</span>,[])

AFsq.addmatrix(<span class="string">'label'</span>,<span class="string">'J1'</span>,<span class="string">'value'</span>,   1,<span class="string">'color'</span>,<span class="string">'red'</span>)
AFsq.addmatrix(<span class="string">'label'</span>,<span class="string">'J2'</span>,<span class="string">'value'</span>,-0.1,<span class="string">'color'</span>,<span class="string">'green'</span>)
AFsq.addcoupling(<span class="string">'mat'</span>,<span class="string">'J1'</span>,<span class="string">'bond'</span>,1)
AFsq.addcoupling(<span class="string">'mat'</span>,<span class="string">'J2'</span>,<span class="string">'bond'</span>,2)
plot(AFsq,<span class="string">'range'</span>,[2 2 0.5])
</pre><pre class="codeoutput">
ans =

  4&times;10 table

    idx    subidx         dl               dr          length    matom1    idx1    matom2    idx2        matrix    
    ___    ______    _____________    _____________    ______    ______    ____    ______    ____    ______________

     1       1       1     0     0    1     0     0        3     'Cu1'      1      'Cu1'      1      ''    ''    ''
     1       2       0     1     0    0     1     0        3     'Cu1'      1      'Cu1'      1      ''    ''    ''
     2       1       1    -1     0    1    -1     0    4.243     'Cu1'      1      'Cu1'      1      ''    ''    ''
     2       2       1     1     0    1     1     0    4.243     'Cu1'      1      'Cu1'      1      ''    ''    ''

</pre><img vspace="5" hspace="5" src="/tutorial4_03.png" alt=""> <h2 id="3">Magnetic structure</h2><p>For weak second neighbor ferromagnetic interaction the magnetic structure is Neel type, with the following parameters:</p><div><ul><li>ordering wave vector k = (1/2 1/2 0)</li><li>spin are in arbitrary plane, lets point along the S = (1 0 0) direction</li><li>normal to the spin vectors n = (0 0 1)</li><li>magnetic supercell is 2x2x1</li></ul></div><p>We use magnetic supercell, since the 2*k equal to a reciprocal lattice vector. In this case the spin wave code cannot use the incommensurate mode, thus we have to create a zero-k structure, that is a 2x2x1 magnetic supercell.Note that the spinw.genmagstr() automatically normalizes the spin vectors to the spin value of the magnetic atoms.</p><pre class="codeinput">AFsq.genmagstr(<span class="string">'mode'</span>,<span class="string">'helical'</span>,<span class="string">'k'</span>,[1/2 1/2 0],<span class="string">'n'</span>,[0 0 1], <span class="string">'S'</span>,[1; 0; 0],<span class="string">'nExt'</span>,[1 1 1]);
disp(<span class="string">'Magnetic structure:'</span>)
AFsq.table(<span class="string">'mag'</span>)

AFsq.energy
plot(AFsq,<span class="string">'range'</span>,[2 2 1])
</pre><pre class="codeoutput">Magnetic structure:

ans =

  1&times;8 table

    num    matom    idx    S     realFhat       imagFhat          pos              kvect      
    ___    _____    ___    _    ___________    ___________    ___________    _________________

     1     'Cu1'     1     1    1    0    0    0    1    0    0    0    0    0.5    0.5      0

Ground state energy: -2.200 meV/spin.
</pre><img vspace="5" hspace="5" src="/tutorial4_04.png" alt=""> <h2 id="4">Spin wave spectrum</h2><p>We calculate the spin wave spectrum and correlation function along several linear q-scans in reciprocal space defined by the Qcorner corner points. The last number in the cell defines the number of steps in each linear scan.</p><pre class="codeinput">Qcorner = {[0 0 0] [1/2 0 0] [1/2 1/2 0] [0 0 0] 200};
sqSpec = AFsq.spinwave(Qcorner, <span class="string">'hermit'</span>, false);
sqSpec = sw_neutron(sqSpec);
sqSpec = sw_egrid(sqSpec,<span class="string">'Evect'</span>,linspace(0,6.5,500));
figure
sw_plotspec(sqSpec,<span class="string">'mode'</span>,3,<span class="string">'dashed'</span>,true,<span class="string">'dE'</span>,0.4,<span class="string">'qLabel'</span>,{<span class="string">'\Gamma'</span> <span class="string">'X'</span> <span class="string">'M'</span> <span class="string">'\Gamma'</span>})
caxis([0 4])
</pre><pre class="codeoutput">Warning: The two times the magnetic ordering wavevector 2*km = G, reciproc
lattice vector, use magnetic supercell to calculate spectrum! 
</pre><img vspace="5" hspace="5" src="/tutorial4_05.png" alt=""> <pre>Written by
Bjorn Fak &amp; Sandor Toth
06-Jun-2014, 06-Feb-2017</pre><p class="footer"><br><a href="https://www.mathworks.com/products/matlab/">Published with MATLAB&reg; R2018b</a><br></p></div><!--
<literal>##### SOURCE BEGIN #####
%% Antiferromagnetic square lattice
% We define a square lattice in the ab plane, with Cu+ ions with S=1 spin.

%% Define the lattice
AFsq = spinw;
AFsq.genlattice('lat_const',[3 3 6],'angled',[90 90 90],'spgr',0)
AFsq.addatom('r',[0 0 0],'S', 1,'label','Cu1','color','b')
AFsq.table('atom')
plot(AFsq)
swplot.zoom(1.5)

%% Couplings
% We create first neighbor couplings in the ab plane and plot the bonds.
% You can click on the different bonds to get the value of the
% corresponding matrix.

AFsq.gencoupling('maxDistance',5)
AFsq.table('bond',[])

AFsq.addmatrix('label','J1','value',   1,'color','red')
AFsq.addmatrix('label','J2','value',-0.1,'color','green')
AFsq.addcoupling('mat','J1','bond',1)
AFsq.addcoupling('mat','J2','bond',2)
plot(AFsq,'range',[2 2 0.5])

%% Magnetic structure
% For weak second neighbor ferromagnetic interaction the magnetic structure
% is Neel type, with the following parameters:
%
% * ordering wave vector k = (1/2 1/2 0)
% * spin are in arbitrary plane, lets point along the S = (1 0 0) direction
% * normal to the spin vectors n = (0 0 1)
% * magnetic supercell is 2x2x1
%
% We use magnetic supercell, since the 2*k equal to a reciprocal lattice
% vector. In this case the spin wave code cannot use the incommensurate
% mode, thus we have to create a zero-k structure, that is a 2x2x1 magnetic
% supercell.Note that the spinw.genmagstr() automatically normalizes the spin
% vectors to the spin value of the magnetic atoms.

AFsq.genmagstr('mode','helical','k',[1/2 1/2 0],'n',[0 0 1], 'S',[1; 0; 0],'nExt',[1 1 1]);  
disp('Magnetic structure:')
AFsq.table('mag')

AFsq.energy
plot(AFsq,'range',[2 2 1])

%% Spin wave spectrum
% We calculate the spin wave spectrum and correlation function along
% several linear q-scans in reciprocal space defined by the Qcorner corner
% points. The last number in the cell defines the number of steps in each
% linear scan.

Qcorner = {[0 0 0] [1/2 0 0] [1/2 1/2 0] [0 0 0] 200};
sqSpec = AFsq.spinwave(Qcorner, 'hermit', false);
sqSpec = sw_neutron(sqSpec); 
sqSpec = sw_egrid(sqSpec,'Evect',linspace(0,6.5,500));
figure
sw_plotspec(sqSpec,'mode',3,'dashed',true,'dE',0.4,'qLabel',{'\Gamma' 'X' 'M' '\Gamma'})
caxis([0 4])

%%
%  Written by
%  Bjorn Fak & Sandor Toth
%  06-Jun-2014, 06-Feb-2017

##### SOURCE END #####</literal>
-->
