---
layout: tutorial
title: Tutorial 2
subtitle: Antiferromagnetic nearest-neighbour spin chain
---

<div class="content"><h1>Antiferromagnetic nearest-neighbour spin chain</h1><!--introduction--><p>Definition of crystal structure, shortest bonds along the a-axis magnetic Cu+ atoms with S=1 spin.</p><!--/introduction--><h2>Contents</h2><div><ul><li><a href="#1">Define the lattice</a></li><li><a href="#2">Create antiferromagnetic interactions</a></li><li><a href="#3">Two ways of defining the magnetic structure</a></li><li><a href="#4">Define all spins</a></li><li><a href="#5">Define only one spin</a></li><li><a href="#6">Spin wave spectrum</a></li></ul></div><h2 id="1">Define the lattice</h2><pre class="codeinput">AFMchain = spinw;
AFMchain.genlattice(<span class="string">'lat_const'</span>,[3 8 8],<span class="string">'angled'</span>,[90 90 90],<span class="string">'spgr'</span>,0);
AFMchain.addatom(<span class="string">'r'</span>,[0 0 0],<span class="string">'S'</span>,1,<span class="string">'label'</span>,<span class="string">'MCu1'</span>,<span class="string">'color'</span>,<span class="string">'blue'</span>);
disp(<span class="string">'Magnetic lattice:'</span>)
AFMchain.table(<span class="string">'matom'</span>)
plot(AFMchain,<span class="string">'range'</span>,[3 1 1])
</pre><pre class="codeoutput">Magnetic lattice:

ans =

  1&times;4 table

    matom     idx    S        pos    
    ______    ___    _    ___________

    'MCu1'     1     1    0    0    0

</pre> <img vspace="5" hspace="5" src="/tutorial2_02.png" alt=""> <h2 id="2">Create antiferromagnetic interactions</h2><p>Ja = 1 meV, positive sign denotes antiferromagnetic interaction.</p><pre class="codeinput">AFMchain.gencoupling(<span class="string">'maxDistance'</span>,7)
AFMchain.table(<span class="string">'bond'</span>,[1 2])

AFMchain.addmatrix(<span class="string">'label'</span>,<span class="string">'Ja'</span>,<span class="string">'value'</span>,1,<span class="string">'color'</span>,<span class="string">'red'</span>);
AFMchain.addcoupling(<span class="string">'mat'</span>,<span class="string">'Ja'</span>,<span class="string">'bond'</span>,1);
disp(<span class="string">'After assigning a matrix to a bond:'</span>)
AFMchain.table(<span class="string">'bond'</span>,[1 2])
plot(AFMchain,<span class="string">'range'</span>,[3 0.9 0.9])
</pre><pre class="codeoutput">
ans =

  2&times;10 table

    idx    subidx        dl             dr         length    matom1    idx1    matom2    idx2        matrix    
    ___    ______    ___________    ___________    ______    ______    ____    ______    ____    ______________

     1       1       1    0    0    1    0    0      3       'MCu1'     1      'MCu1'     1      ''    ''    ''
     2       1       2    0    0    2    0    0      6       'MCu1'     1      'MCu1'     1      ''    ''    ''

After assigning a matrix to a bond:

ans =

  2&times;10 table

    idx    subidx        dl             dr         length    matom1    idx1    matom2    idx2         matrix     
    ___    ______    ___________    ___________    ______    ______    ____    ______    ____    ________________

     1       1       1    0    0    1    0    0      3       'MCu1'     1      'MCu1'     1      'Ja'    ''    ''
     2       1       2    0    0    2    0    0      6       'MCu1'     1      'MCu1'     1      ''      ''    ''

</pre><img vspace="5" hspace="5" src="/tutorial2_03.png" alt=""> <h2 id="3">Two ways of defining the magnetic structure</h2><h2 id="4">Define all spins</h2><p>We define a magnetic supercell 2x1x1 of the crystal cell and define both spin direction in the supercell with the following parameters:</p><div><ul><li>magnetic ordering wave vector k = (1/2 0 0)</li><li>spins pointing along +/- y direction: S = [[0 1 0]' [0 -1 0]']</li><li>normal to the spin vectors n = (1 0 0)</li></ul></div><pre class="codeinput">AFMchain.genmagstr(<span class="string">'mode'</span>,<span class="string">'direct'</span>,<span class="string">'k'</span>,[1/2 0 0],<span class="string">'n'</span>,[1 0 0],<span class="string">'S'</span>,[0 0; 1 -1;0 0],<span class="string">'nExt'</span>,[2 1 1]);
</pre><h2 id="5">Define only one spin</h2><p>We define the spin direction in the crystallographic unit cell and let the sw.genmagstr() function generate the other spin based on the magnetic ordering wave vector and normal vectors. This method is usefull for creating complex structures. Both methods gives the same magnetic structure, all stored values in the afchain.mag_str field are the same.</p><pre class="codeinput">AFMchain.genmagstr(<span class="string">'mode'</span>,<span class="string">'helical'</span>,<span class="string">'k'</span>,[1/2 0 0],<span class="string">'n'</span>,[1 0 0],<span class="string">'S'</span>,[0; 1; 0],<span class="string">'nExt'</span>,[2 1 1]);
disp(<span class="string">'Magnetic structure:'</span>)
AFMchain.table(<span class="string">'mag'</span>)

<span class="comment">% Ground state energy</span>
AFMchain.energy
plot(AFMchain,<span class="string">'range'</span>,[3 0.9 0.9],<span class="string">'cellMode'</span>,<span class="string">'none'</span>,<span class="string">'baseMode'</span>,<span class="string">'none'</span>)
</pre><pre class="codeoutput">Magnetic structure:

ans =

  2&times;8 table

    num    matom     idx    S      realFhat         imagFhat           pos              kvect      
    ___    ______    ___    _    _____________    _____________    ___________    _________________

     1     'MCu1'     1     1    0     1     0    0     0     1    0    0    0    0.5      0      0
     2     'MCu1'     1     1    0    -1     0    0     0    -1    1    0    0    0.5      0      0

Ground state energy: -1.000 meV/spin.
</pre><img vspace="5" hspace="5" src="/tutorial2_04.png" alt=""> <h2 id="6">Spin wave spectrum</h2><p>We calculate the spin wave spectrum and neutron scattering cross sections along the chain direction. The neutron scattering cross section is plotted together with the dispersion (black line).</p><pre class="codeinput">afcSpec = AFMchain.spinwave({[0 0 0] [1 0 0] 523}, <span class="string">'hermit'</span>,true);
figure
subplot(2,1,1)
sw_plotspec(afcSpec,<span class="string">'mode'</span>,4,<span class="string">'dE'</span>,0.2,<span class="string">'axLim'</span>,[0 3])

<span class="comment">% To calculate the intensity, we need to sum up the intensity of the two</span>
<span class="comment">% degenerate spin wave mode using the sw_omegasum() function. We plot the</span>
<span class="comment">% logarithm of the intensity.</span>

afcSpec = sw_neutron(afcSpec);
afcSpec = sw_egrid(afcSpec,<span class="string">'Evect'</span>,linspace(0,6.5,500),<span class="string">'component'</span>,<span class="string">'Sperp'</span>);
afcSpec = sw_omegasum(afcSpec,<span class="string">'zeroint'</span>,1e-6);
subplot(2,1,2)
sw_plotspec(afcSpec,<span class="string">'mode'</span>,2,<span class="string">'log'</span>,true,<span class="string">'axLim'</span>,[-4 10])

<span class="comment">% Position the figure on the screen, similarly how subplot() positions the</span>
<span class="comment">% axes on the figure.</span>
swplot.subfigure(1,3,1)
</pre><img vspace="5" hspace="5" src="/tutorial2_05.png" alt=""> <pre>Written by
Bjorn Fak &amp; Sandor Toth
06-Jun-2014, 06-Feb-2015</pre><p class="footer"><br><a href="https://www.mathworks.com/products/matlab/">Published with MATLAB&reg; R2018b</a><br></p></div><!--
<literal>##### SOURCE BEGIN #####
%% Antiferromagnetic nearest-neighbour spin chain
% Definition of crystal structure, shortest bonds along the a-axis magnetic
% Cu+ atoms with S=1 spin.

%% Define the lattice
AFMchain = spinw; 
AFMchain.genlattice('lat_const',[3 8 8],'angled',[90 90 90],'spgr',0);
AFMchain.addatom('r',[0 0 0],'S',1,'label','MCu1','color','blue');
disp('Magnetic lattice:')
AFMchain.table('matom')
plot(AFMchain,'range',[3 1 1])

%% Create antiferromagnetic interactions
% Ja = 1 meV, positive sign denotes antiferromagnetic interaction.

AFMchain.gencoupling('maxDistance',7)
AFMchain.table('bond',[1 2])

AFMchain.addmatrix('label','Ja','value',1,'color','red'); 
AFMchain.addcoupling('mat','Ja','bond',1);
disp('After assigning a matrix to a bond:')
AFMchain.table('bond',[1 2])
plot(AFMchain,'range',[3 0.9 0.9])

%% Two ways of defining the magnetic structure

%%% Define all spins
% We define a magnetic supercell 2x1x1 of the crystal cell and define both
% spin direction in the supercell with the following parameters:
%
% * magnetic ordering wave vector k = (1/2 0 0)
% * spins pointing along +/- y direction: S = [[0 1 0]' [0 -1 0]']
% * normal to the spin vectors n = (1 0 0)

AFMchain.genmagstr('mode','direct','k',[1/2 0 0],'n',[1 0 0],'S',[0 0; 1 -1;0 0],'nExt',[2 1 1]);

%%% Define only one spin
% We define the spin direction in the crystallographic unit cell and let
% the sw.genmagstr() function generate the other spin based on the magnetic
% ordering wave vector and normal vectors. This method is usefull for
% creating complex structures. Both methods gives the same magnetic
% structure, all stored values in the afchain.mag_str field are the same.

AFMchain.genmagstr('mode','helical','k',[1/2 0 0],'n',[1 0 0],'S',[0; 1; 0],'nExt',[2 1 1]); 
disp('Magnetic structure:')
AFMchain.table('mag')

% Ground state energy
AFMchain.energy
plot(AFMchain,'range',[3 0.9 0.9],'cellMode','none','baseMode','none')

%% Spin wave spectrum
% We calculate the spin wave spectrum and neutron scattering cross
% sections along the chain direction. The neutron scattering cross section
% is plotted together with the dispersion (black line).

afcSpec = AFMchain.spinwave({[0 0 0] [1 0 0] 523}, 'hermit',true);
figure
subplot(2,1,1)
sw_plotspec(afcSpec,'mode',4,'dE',0.2,'axLim',[0 3])

% To calculate the intensity, we need to sum up the intensity of the two
% degenerate spin wave mode using the sw_omegasum() function. We plot the
% logarithm of the intensity.

afcSpec = sw_neutron(afcSpec);
afcSpec = sw_egrid(afcSpec,'Evect',linspace(0,6.5,500),'component','Sperp');
afcSpec = sw_omegasum(afcSpec,'zeroint',1e-6);
subplot(2,1,2)
sw_plotspec(afcSpec,'mode',2,'log',true,'axLim',[-4 10])

% Position the figure on the screen, similarly how subplot() positions the
% axes on the figure.
swplot.subfigure(1,3,1)

%%
%  Written by
%  Bjorn Fak & Sandor Toth
%  06-Jun-2014, 06-Feb-2015
##### SOURCE END #####</literal>
-->
