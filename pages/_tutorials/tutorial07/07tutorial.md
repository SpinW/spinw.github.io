---
layout: tutorial
title: Tutorial 7
subtitle: k=0 Kagome antiferromagnet
---

<div class="content"><h1>k=0 Kagome antiferromagnet</h1><!--introduction--><p>We create a lattice with space group "P -3" where all first neighbor bonds are symmetry equivalent and add a magnetic Cr+ with S=1 spin.</p><!--/introduction--><h2>Contents</h2><div><ul><li><a href="#1">Define the lattice</a></li><li><a href="#2">Create bonds</a></li><li><a href="#3">Hamiltonian</a></li><li><a href="#4">Generate magnetic structure</a></li><li><a href="#5">Calculate spin wave dispersion</a></li><li><a href="#6">Powder spectrum</a></li></ul></div><h2 id="1">Define the lattice</h2><pre class="codeinput">AFkagome = spinw;
AFkagome.genlattice(<span class="string">'lat_const'</span>,[6 6 10],<span class="string">'angled'</span>,[90 90 120],<span class="string">'spgr'</span>,<span class="string">'P -3'</span>)
AFkagome.addatom(<span class="string">'r'</span>,[1/2 0 0],<span class="string">'S'</span>, 1,<span class="string">'label'</span>,<span class="string">'MCu1'</span>,<span class="string">'color'</span>,<span class="string">'r'</span>)
plot(AFkagome,<span class="string">'range'</span>,[2 2 1])
</pre> <img vspace="5" hspace="5" src="/tutorial7_02.png" alt=""> <h2 id="2">Create bonds</h2><p>Generate the list of bonds and lists them.</p><pre class="codeinput">AFkagome.gencoupling(<span class="string">'maxDistance'</span>,7)
disp(<span class="string">'Bonds:'</span>)
AFkagome.table(<span class="string">'bond'</span>,[])
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

</pre><h2 id="3">Hamiltonian</h2><p>We create AFM first neighbor interaction and weak 2nd neighbor AFM exchange.</p><pre class="codeinput">AFkagome.addmatrix(<span class="string">'label'</span>,<span class="string">'J1'</span>,<span class="string">'value'</span>,1.00,<span class="string">'color'</span>,<span class="string">'r'</span>)
AFkagome.addmatrix(<span class="string">'label'</span>,<span class="string">'J2'</span>,<span class="string">'value'</span>,0.11,<span class="string">'color'</span>,<span class="string">'g'</span>)
AFkagome.addcoupling(<span class="string">'mat'</span>,<span class="string">'J1'</span>,<span class="string">'bond'</span>,1)
AFkagome.addcoupling(<span class="string">'mat'</span>,<span class="string">'J2'</span>,<span class="string">'bond'</span>,2)
plot(AFkagome,<span class="string">'range'</span>,[3 3 1])
</pre><img vspace="5" hspace="5" src="/tutorial7_03.png" alt=""> <h2 id="4">Generate magnetic structure</h2><p>We create a k = (0 0 0) magnetic structure, with the three spin directions in the unit cell (120 degree between neighbors). The spin vector components are given in the coordinate system of the lattice vectors (abc).</p><pre class="codeinput">S0 = [1 -2 1; 2 -1 -1; 0 0 0];
AFkagome.genmagstr(<span class="string">'mode'</span>,<span class="string">'direct'</span>,<span class="string">'k'</span>,[0 0 0],<span class="string">'n'</span>,[0 0 1],<span class="string">'unit'</span>,<span class="string">'lu'</span>,<span class="string">'S'</span>,S0);
disp(<span class="string">'Magnetic structure:'</span>)
AFkagome.table(<span class="string">'mag'</span>)
AFkagome.energy

plot(AFkagome,<span class="string">'range'</span>,[3 3 1])
</pre><pre class="codeoutput">Magnetic structure:

ans =

  3&times;7 table

    num    matom     idx    S             realFhat                    pos              kvect   
    ___    ______    ___    _    __________________________    _________________    ___________

     1     'MCu1'     1     1         0         1         0    0.5      0      0    0    0    0
     2     'MCu1'     2     1    -0.866      -0.5         0      0    0.5      0    0    0    0
     3     'MCu1'     3     1     0.866      -0.5         0    0.5    0.5      0    0    0    0

Ground state energy: -1.110 meV/spin.
</pre><img vspace="5" hspace="5" src="/tutorial7_04.png" alt=""> <h2 id="5">Calculate spin wave dispersion</h2><pre class="codeinput">afkSpec = AFkagome.spinwave({[-1/2 0 0] [0 0 0] [1/2 1/2 0] 100},<span class="string">'hermit'</span>,false);
figure
sw_plotspec(afkSpec,<span class="string">'mode'</span>,1,<span class="string">'axLim'</span>,[0 3],<span class="string">'colorbar'</span>,false,<span class="string">'colormap'</span>,[0 0 0],<span class="string">'dashed'</span>,true)
</pre><img vspace="5" hspace="5" src="/tutorial7_05.png" alt=""> <h2 id="6">Powder spectrum</h2><pre class="codeinput">afkPow = AFkagome.powspec(linspace(0,2.5,150),<span class="string">'Evect'</span>,linspace(0,3,250),<span class="keyword">...</span>
    <span class="string">'nRand'</span>,1e3,<span class="string">'hermit'</span>,false,<span class="string">'imagChk'</span>,false);

figure
sw_plotspec(afkPow,<span class="string">'axLim'</span>,[0 0.2])
</pre><img vspace="5" hspace="5" src="/tutorial7_06.png" alt=""> <pre>Written by
Bjorn Fak &amp; Sandor Toth
06-Jun-2014, 06-Feb-2016</pre><p class="footer"><br><a href="https://www.mathworks.com/products/matlab/">Published with MATLAB&reg; R2018b</a><br></p></div><!--
<literal>##### SOURCE BEGIN #####
%% k=0 Kagome antiferromagnet
% We create a lattice with space group "P -3" where all first neighbor
% bonds are symmetry equivalent and add a magnetic Cr+ with S=1 spin.

%% Define the lattice
AFkagome = spinw;
AFkagome.genlattice('lat_const',[6 6 10],'angled',[90 90 120],'spgr','P -3')
AFkagome.addatom('r',[1/2 0 0],'S', 1,'label','MCu1','color','r')
plot(AFkagome,'range',[2 2 1])

%% Create bonds
% Generate the list of bonds and lists them.

AFkagome.gencoupling('maxDistance',7) 
disp('Bonds:')
AFkagome.table('bond',[])

%% Hamiltonian
% We create AFM first neighbor interaction and weak 2nd neighbor AFM
% exchange.

AFkagome.addmatrix('label','J1','value',1.00,'color','r')
AFkagome.addmatrix('label','J2','value',0.11,'color','g')
AFkagome.addcoupling('mat','J1','bond',1)
AFkagome.addcoupling('mat','J2','bond',2)
plot(AFkagome,'range',[3 3 1])

%% Generate magnetic structure
% We create a k = (0 0 0) magnetic structure, with the three spin directions
% in the unit cell (120 degree between neighbors). The spin vector
% components are given in the coordinate system of the lattice vectors
% (abc).

S0 = [1 -2 1; 2 -1 -1; 0 0 0];
AFkagome.genmagstr('mode','direct','k',[0 0 0],'n',[0 0 1],'unit','lu','S',S0); 
disp('Magnetic structure:')
AFkagome.table('mag')
AFkagome.energy

plot(AFkagome,'range',[3 3 1])

%% Calculate spin wave dispersion

afkSpec = AFkagome.spinwave({[-1/2 0 0] [0 0 0] [1/2 1/2 0] 100},'hermit',false);
figure
sw_plotspec(afkSpec,'mode',1,'axLim',[0 3],'colorbar',false,'colormap',[0 0 0],'dashed',true)

%% Powder spectrum

afkPow = AFkagome.powspec(linspace(0,2.5,150),'Evect',linspace(0,3,250),...
    'nRand',1e3,'hermit',false,'imagChk',false);

figure
sw_plotspec(afkPow,'axLim',[0 0.2])

%%
%  Written by
%  Bjorn Fak & Sandor Toth
%  06-Jun-2014, 06-Feb-2016

##### SOURCE END #####</literal>
-->
