---
layout: tutorial
title: Tutorial 6
subtitle: Ferromagnetic kagome lattice
---

<div class="content"><h1>Ferromagnetic kagome lattice</h1><!--introduction--><p>We create the kagome lattice with up to 4th neighbor interactions. The symmetry related atoms are denoted by MCu1(i)_j, where i is the index of independent atomic positions, j is the index of the generated atomic positions of the i-th independent position.</p><!--/introduction--><h2>Contents</h2><div><ul><li><a href="#1">Define the lattice</a></li><li><a href="#2">Define Hamiltonian</a></li><li><a href="#3">Magnetic structure</a></li><li><a href="#4">Spin wave dispersion</a></li><li><a href="#5">Powder averaged spectrum</a></li></ul></div><h2 id="1">Define the lattice</h2><pre class="codeinput">kagome4 = spinw;
kagome4.genlattice(<span class="string">'lat_const'</span>,[6 6 8],<span class="string">'angled'</span>,[90 90 120],<span class="string">'spgr'</span>,<span class="string">'P -3'</span>);
kagome4.addatom(<span class="string">'r'</span>, [1/2 0 0],<span class="string">'S'</span>, 1,<span class="string">'label'</span>,<span class="string">'MCu1'</span>,<span class="string">'color'</span>,<span class="string">'r'</span>);
disp(<span class="string">'Atomic positions:'</span>)
kagome4.table(<span class="string">'atom'</span>)
plot(kagome4)
swplot.zoom(1.5)
</pre><pre class="codeoutput">Atomic positions:

ans =

  3&times;4 table

    matom     idx    S           pos       
    ______    ___    _    _________________

    'MCu1'     1     1    0.5      0      0
    'MCu1'     2     1      0    0.5      0
    'MCu1'     3     1    0.5    0.5      0

</pre> <img vspace="5" hspace="5" src="/tutorial6_02.png" alt=""> <h2 id="2">Define Hamiltonian</h2><p>We add couplings up to 4th neighbor interactions. If the generation of the bond tables would depend on distance, J3a, J3b and J3c would be equivalent. However using the 'P -3' space group the three type of bonds are inequivalent, as physically expected in real systems (J3a goes through an intermediate magnetic atom, while the other two bonds are not).</p><pre class="codeinput">kagome4.gencoupling(<span class="string">'maxDistance'</span>,7);
disp(<span class="string">'Bonds:'</span>)
kagome4.table(<span class="string">'bond'</span>,[])

kagome4.addmatrix(<span class="string">'label'</span>,<span class="string">'J1-'</span>,<span class="string">'value'</span>,-1.00,<span class="string">'color'</span>,<span class="string">'g'</span>)
kagome4.addmatrix(<span class="string">'label'</span>,<span class="string">'J2'</span>,<span class="string">'value'</span>, 0.10,<span class="string">'color'</span>,<span class="string">'r'</span>)
kagome4.addmatrix(<span class="string">'label'</span>,<span class="string">'J3a'</span>,<span class="string">'value'</span>, 0.00,<span class="string">'color'</span>,<span class="string">'orange'</span>)
kagome4.addmatrix(<span class="string">'label'</span>,<span class="string">'J3b'</span>,<span class="string">'value'</span>, 0.17,<span class="string">'color'</span>,<span class="string">'b'</span>)
kagome4.addmatrix(<span class="string">'label'</span>,<span class="string">'J3c'</span>,<span class="string">'value'</span>, 0.00,<span class="string">'color'</span>,<span class="string">'purple'</span>)

kagome4.addcoupling(<span class="string">'mat'</span>,<span class="string">'J1-'</span>,<span class="string">'bond'</span>,1);
kagome4.addcoupling(<span class="string">'mat'</span>,<span class="string">'J2'</span>,<span class="string">'bond'</span>,2);
kagome4.addcoupling(<span class="string">'mat'</span>,<span class="string">'J3a'</span>,<span class="string">'bond'</span>,3);
kagome4.addcoupling(<span class="string">'mat'</span>,<span class="string">'J3b'</span>,<span class="string">'bond'</span>,4);
kagome4.addcoupling(<span class="string">'mat'</span>,<span class="string">'J3c'</span>,<span class="string">'bond'</span>,5);

<span class="comment">% The first neighbor bonds will be shown as dashed lines. This is automatic</span>
<span class="comment">% when the matrix labels ends with a minus sign.</span>
plot(kagome4,<span class="string">'range'</span>,[2 2 1],<span class="string">'bondMode'</span>,<span class="string">'line'</span>,<span class="string">'bondLineWidth0'</span>,2)
</pre><pre class="codeoutput">Bonds:

ans =

  21&times;10 table

    idx    subidx          dl                   dr             length    matom1    idx1    matom2    idx2        matrix    
    ___    ______    ______________    ____________________    ______    ______    ____    ______    ____    ______________

     1       1        0     1     0       0     0.5       0        3     'MCu1'     3      'MCu1'     1      ''    ''    ''
     1       2        0    -1     0    -0.5    -0.5       0        3     'MCu1'     1      'MCu1'     2      ''    ''    ''
     1       3        0     0     0     0.5       0       0        3     'MCu1'     2      'MCu1'     3      ''    ''    ''
     1       4        0     0     0       0    -0.5       0        3     'MCu1'     3      'MCu1'     1      ''    ''    ''
     1       5        1     0     0     0.5     0.5       0        3     'MCu1'     1      'MCu1'     2      ''    ''    ''
     1       6       -1     0     0    -0.5       0       0        3     'MCu1'     2      'MCu1'     3      ''    ''    ''
     2       1        1    -1     0     0.5    -0.5       0    5.196     'MCu1'     1      'MCu1'     2      ''    ''    ''
     2       2        0     1     0     0.5       1       0    5.196     'MCu1'     2      'MCu1'     3      ''    ''    ''
     2       3       -1     0     0      -1    -0.5       0    5.196     'MCu1'     3      'MCu1'     1      ''    ''    ''
     2       4        0     0     0    -0.5     0.5       0    5.196     'MCu1'     1      'MCu1'     2      ''    ''    ''
     2       5       -1    -1     0    -0.5      -1       0    5.196     'MCu1'     2      'MCu1'     3      ''    ''    ''
     2       6        1     1     0       1     0.5       0    5.196     'MCu1'     3      'MCu1'     1      ''    ''    ''
     3       1        0     1     0       0       1       0        6     'MCu1'     1      'MCu1'     1      ''    ''    ''
     3       2       -1    -1     0      -1      -1       0        6     'MCu1'     2      'MCu1'     2      ''    ''    ''
     3       3        1     0     0       1       0       0        6     'MCu1'     3      'MCu1'     3      ''    ''    ''
     4       1        0     1     0       0       1       0        6     'MCu1'     2      'MCu1'     2      ''    ''    ''
     4       2       -1    -1     0      -1      -1       0        6     'MCu1'     3      'MCu1'     3      ''    ''    ''
     4       3        1     0     0       1       0       0        6     'MCu1'     1      'MCu1'     1      ''    ''    ''
     5       1        0     1     0       0       1       0        6     'MCu1'     3      'MCu1'     3      ''    ''    ''
     5       2       -1    -1     0      -1      -1       0        6     'MCu1'     1      'MCu1'     1      ''    ''    ''
     5       3        1     0     0       1       0       0        6     'MCu1'     2      'MCu1'     2      ''    ''    ''

</pre><img vspace="5" hspace="5" src="/tutorial6_03.png" alt=""> <h2 id="3">Magnetic structure</h2><p>For strong FM 1str neighbour and weak further neighbor interaction the ground state is ferromagnetic.</p><pre class="codeinput">kagome4.genmagstr(<span class="string">'mode'</span>,<span class="string">'helical'</span>,<span class="string">'k'</span>,[0 0 0],<span class="string">'n'</span>,[0 1 0],<span class="string">'S'</span>,[0 1 0]');
disp(<span class="string">'Magnetic structure:'</span>)
kagome4.table(<span class="string">'mag'</span>)
kagome4.energy
plot(kagome4,<span class="string">'range'</span>,[2 2 1],<span class="string">'bondMode'</span>,<span class="string">'line'</span>,<span class="string">'bondLineWidth0'</span>,3,<span class="keyword">...</span>
    <span class="string">'bondZero'</span>,false)
</pre><pre class="codeoutput">Magnetic structure:

ans =

  3&times;7 table

    num    matom     idx    S     realFhat             pos              kvect   
    ___    ______    ___    _    ___________    _________________    ___________

     1     'MCu1'     1     1    0    1    0    0.5      0      0    0    0    0
     2     'MCu1'     2     1    0    1    0      0    0.5      0    0    0    0
     3     'MCu1'     3     1    0    1    0    0.5    0.5      0    0    0    0

Ground state energy: -1.630 meV/spin.
</pre><img vspace="5" hspace="5" src="/tutorial6_04.png" alt=""> <h2 id="4">Spin wave dispersion</h2><pre class="codeinput">kag4Spec = kagome4.spinwave({[-1/2 0 0] [0 0 0] [1/2 1/2 0] 200});
kag4Spec = sw_neutron(kag4Spec);
kag4Spec = sw_egrid(kag4Spec,<span class="string">'Evect'</span>,linspace(0,6.5,100)) ;
figure
sw_plotspec(kag4Spec,<span class="string">'mode'</span>,1,<span class="string">'axLim'</span>,[0 8],<span class="string">'colorbar'</span>,false,<span class="string">'colormap'</span>,[0 0 0])
</pre><pre class="codeoutput">Warning: To make the Hamiltonian positive definite, a small omega_tol value was
added to its diagonal! 
</pre><img vspace="5" hspace="5" src="/tutorial6_05.png" alt=""> <h2 id="5">Powder averaged spectrum</h2><pre class="codeinput">kag4Pow = kagome4.powspec(linspace(0,2.5,100),<span class="string">'Evect'</span>,linspace(0,7,250),<span class="keyword">...</span>
    <span class="string">'nRand'</span>,1e3,<span class="string">'hermit'</span>,false);
figure
sw_plotspec(kag4Pow,<span class="string">'axLim'</span>,[0 0.2],<span class="string">'colorbar'</span>,true)
</pre><img vspace="5" hspace="5" src="/tutorial6_06.png" alt=""> <pre>Written by
Bjorn Fak &amp; Sandor Toth
06-Jun-2014, 06-Feb-2017</pre><p class="footer"><br><a href="https://www.mathworks.com/products/matlab/">Published with MATLAB&reg; R2018b</a><br></p></div><!--
<literal>##### SOURCE BEGIN #####
%% Ferromagnetic kagome lattice
% We create the kagome lattice with up to 4th neighbor interactions. The
% symmetry related atoms are denoted by MCu1(i)_j, where i is the index of
% independent atomic positions, j is the index of the generated atomic
% positions of the i-th independent position.

%% Define the lattice
kagome4 = spinw;
kagome4.genlattice('lat_const',[6 6 8],'angled',[90 90 120],'spgr','P -3');
kagome4.addatom('r', [1/2 0 0],'S', 1,'label','MCu1','color','r');
disp('Atomic positions:')
kagome4.table('atom')
plot(kagome4)
swplot.zoom(1.5)

%% Define Hamiltonian
% We add couplings up to 4th neighbor interactions. If the generation of
% the bond tables would depend on distance, J3a, J3b and J3c would be
% equivalent. However using the 'P -3' space group the three type of bonds
% are inequivalent, as physically expected in real systems (J3a goes through
% an intermediate magnetic atom, while the other two bonds are not).

kagome4.gencoupling('maxDistance',7);
disp('Bonds:')
kagome4.table('bond',[])

kagome4.addmatrix('label','J1-','value',-1.00,'color','g')
kagome4.addmatrix('label','J2','value', 0.10,'color','r')
kagome4.addmatrix('label','J3a','value', 0.00,'color','orange')
kagome4.addmatrix('label','J3b','value', 0.17,'color','b')
kagome4.addmatrix('label','J3c','value', 0.00,'color','purple')

kagome4.addcoupling('mat','J1-','bond',1);
kagome4.addcoupling('mat','J2','bond',2);
kagome4.addcoupling('mat','J3a','bond',3);
kagome4.addcoupling('mat','J3b','bond',4);
kagome4.addcoupling('mat','J3c','bond',5);

% The first neighbor bonds will be shown as dashed lines. This is automatic
% when the matrix labels ends with a minus sign.
plot(kagome4,'range',[2 2 1],'bondMode','line','bondLineWidth0',2)

%% Magnetic structure
% For strong FM 1str neighbour and weak further neighbor interaction the
% ground state is ferromagnetic.

kagome4.genmagstr('mode','helical','k',[0 0 0],'n',[0 1 0],'S',[0 1 0]');
disp('Magnetic structure:')
kagome4.table('mag')
kagome4.energy
plot(kagome4,'range',[2 2 1],'bondMode','line','bondLineWidth0',3,...
    'bondZero',false)

%% Spin wave dispersion

kag4Spec = kagome4.spinwave({[-1/2 0 0] [0 0 0] [1/2 1/2 0] 200});
kag4Spec = sw_neutron(kag4Spec);
kag4Spec = sw_egrid(kag4Spec,'Evect',linspace(0,6.5,100)) ;
figure
sw_plotspec(kag4Spec,'mode',1,'axLim',[0 8],'colorbar',false,'colormap',[0 0 0])

%% Powder averaged spectrum

kag4Pow = kagome4.powspec(linspace(0,2.5,100),'Evect',linspace(0,7,250),...
    'nRand',1e3,'hermit',false);
figure
sw_plotspec(kag4Pow,'axLim',[0 0.2],'colorbar',true)

%%
%  Written by
%  Bjorn Fak & Sandor Toth
%  06-Jun-2014, 06-Feb-2017
##### SOURCE END #####</literal>
-->
