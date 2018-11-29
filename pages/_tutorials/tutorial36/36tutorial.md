---
layout: tutorial
title: Tutorial 36
subtitle: Anisotropic exchange on the FM chain
---

<div class="content"><h1>Anisotropic exchange on the FM chain</h1><!--introduction--><!--/introduction--><h2>Contents</h2><div><ul><li><a href="#1">Define the lattice</a></li><li><a href="#2">spin-spin correlation function</a></li><li><a href="#3">anisotropic exchange on the AFM chain</a></li><li><a href="#4">spin-spin correlation function</a></li><li><a href="#5">anisotropic exchange on the AFM chain</a></li><li><a href="#6">spin-spin correlation function</a></li></ul></div><h2 id="1">Define the lattice</h2><pre class="codeinput">fmch = spinw;
fmch.genlattice(<span class="string">'lat_const'</span>,[3 4 4])
fmch.addatom(<span class="string">'r'</span>,[  0 0 0],<span class="string">'S'</span>,1)

fmch.addmatrix(<span class="string">'label'</span>,<span class="string">'J_1'</span>,<span class="string">'value'</span>,diag(-[3 4 5]))

fmch.gencoupling
fmch.addcoupling(<span class="string">'mat'</span>,<span class="string">'J_1'</span>,<span class="string">'bond'</span>,1)


fmch.genmagstr(<span class="string">'mode'</span>,<span class="string">'helical'</span>,<span class="string">'S'</span>,[0 0 1]')
plot(fmch)
</pre> <img vspace="5" hspace="5" src="/tutorial36_02.png" alt=""> <h2 id="2">spin-spin correlation function</h2><pre class="codeinput">spec = fmch.spinwave({[0 0 0] [1 0 0] 501});
spec = sw_egrid(spec,<span class="string">'component'</span>,{<span class="string">'Sxx'</span> <span class="string">'Syy'</span> <span class="string">'Szz'</span>});

clf
sw_plotspec(spec,<span class="string">'mode'</span>,<span class="string">'int'</span>,<span class="string">'dE'</span>,0.5);
ylim([-0.05 0.8])
</pre><img vspace="5" hspace="5" src="/tutorial36_03.png" alt=""> <h2 id="3">anisotropic exchange on the AFM chain</h2><pre class="codeinput">afmch = spinw;
afmch.genlattice(<span class="string">'lat_const'</span>,[3 4 4])
afmch.addatom(<span class="string">'r'</span>,[  0 0 0],<span class="string">'S'</span>,1)

afmch.addmatrix(<span class="string">'label'</span>,<span class="string">'J_1'</span>,<span class="string">'value'</span>,diag([3 4 4.1]))

afmch.gencoupling
afmch.addcoupling(<span class="string">'mat'</span>,<span class="string">'J_1'</span>,<span class="string">'bond'</span>,1)


afmch.genmagstr(<span class="string">'mode'</span>,<span class="string">'helical'</span>,<span class="string">'S'</span>,[0 0 1]',<span class="string">'k'</span>,[1/2 0 0],<span class="string">'n'</span>,[1 0 0])
<span class="comment">%plot(afmch)</span>
</pre><h2 id="4">spin-spin correlation function</h2><pre class="codeinput">spec = afmch.spinwave({[0 0 0] [1 0 0] 501});
spec = sw_egrid(spec,<span class="string">'component'</span>,{<span class="string">'Sxx'</span> <span class="string">'Syy'</span> <span class="string">'Szz'</span>});

clf
sw_plotspec(spec,<span class="string">'mode'</span>,<span class="string">'disp'</span>,<span class="string">'linestyle'</span>,<span class="string">'-'</span>,<span class="string">'colormap'</span>,[0 0 0])
colorbar <span class="string">off</span>
legend <span class="string">off</span>
sw_plotspec(spec,<span class="string">'mode'</span>,<span class="string">'color'</span>,<span class="string">'dE'</span>,0.5,<span class="string">'axLim'</span>,[0 1]);
hold <span class="string">on</span>
hLegend = legend;
set(hLegend,<span class="string">'location'</span>,<span class="string">'southeast'</span>)
</pre><pre class="codeoutput">Warning: The two times the magnetic ordering wavevector 2*km = G, reciproc
lattice vector, use magnetic supercell to calculate spectrum! 
</pre><img vspace="5" hspace="5" src="/tutorial36_04.png" alt=""> <h2 id="5">anisotropic exchange on the AFM chain</h2><p>rotated anisotropy</p><pre class="codeinput">afmch = spinw;
afmch.genlattice(<span class="string">'lat_const'</span>,[3 4 4])
afmch.addatom(<span class="string">'r'</span>,[  0 0 0],<span class="string">'S'</span>,1)

R = sw_rotmatd([0 0 1],45);
J1 = diag([3 4 4.1]);
J1 = R*J1*R';

afmch.addmatrix(<span class="string">'label'</span>,<span class="string">'J_1'</span>,<span class="string">'value'</span>,J1)

afmch.gencoupling
afmch.addcoupling(<span class="string">'mat'</span>,<span class="string">'J_1'</span>,<span class="string">'bond'</span>,1)


afmch.genmagstr(<span class="string">'mode'</span>,<span class="string">'helical'</span>,<span class="string">'S'</span>,[0 0 1]',<span class="string">'k'</span>,[1/2 0 0],<span class="string">'n'</span>,[1 0 0],<span class="string">'nEXt'</span>,[2 1 1])
<span class="comment">%plot(afmch)</span>
</pre><h2 id="6">spin-spin correlation function</h2><pre class="codeinput">spec = afmch.spinwave({[0 0 0] [1 0 0] 501});
spec = sw_neutron(spec,<span class="string">'uv'</span>,{[1 1 0] [-1 1 0]},<span class="string">'pol'</span>,true);
spec = sw_egrid(spec,<span class="string">'component'</span>,{<span class="string">'Sxx+Sxy'</span> <span class="string">'Sxx-Sxy'</span>});

clf
sw_plotspec(spec,<span class="string">'mode'</span>,<span class="string">'disp'</span>,<span class="string">'linestyle'</span>,<span class="string">'-'</span>,<span class="string">'colormap'</span>,[0 0 0])
colorbar <span class="string">off</span>
legend <span class="string">off</span>
sw_plotspec(spec,<span class="string">'mode'</span>,<span class="string">'color'</span>,<span class="string">'dE'</span>,0.5,<span class="string">'axLim'</span>,[0 1]);
hold <span class="string">on</span>
hLegend = legend;
set(hLegend,<span class="string">'location'</span>,<span class="string">'southeast'</span>)
</pre><img vspace="5" hspace="5" src="/tutorial36_05.png" alt=""> <p class="footer"><br><a href="https://www.mathworks.com/products/matlab/">Published with MATLAB&reg; R2018b</a><br></p></div><!--
<literal>##### SOURCE BEGIN #####
%% Anisotropic exchange on the FM chain

%% Define the lattice
fmch = spinw;
fmch.genlattice('lat_const',[3 4 4])
fmch.addatom('r',[  0 0 0],'S',1)

fmch.addmatrix('label','J_1','value',diag(-[3 4 5]))

fmch.gencoupling
fmch.addcoupling('mat','J_1','bond',1)


fmch.genmagstr('mode','helical','S',[0 0 1]')
plot(fmch)

%% spin-spin correlation function

spec = fmch.spinwave({[0 0 0] [1 0 0] 501});
spec = sw_egrid(spec,'component',{'Sxx' 'Syy' 'Szz'});

clf
sw_plotspec(spec,'mode','int','dE',0.5);
ylim([-0.05 0.8])

%% anisotropic exchange on the AFM chain

afmch = spinw;
afmch.genlattice('lat_const',[3 4 4])
afmch.addatom('r',[  0 0 0],'S',1)

afmch.addmatrix('label','J_1','value',diag([3 4 4.1]))

afmch.gencoupling
afmch.addcoupling('mat','J_1','bond',1)


afmch.genmagstr('mode','helical','S',[0 0 1]','k',[1/2 0 0],'n',[1 0 0])
%plot(afmch)

%% spin-spin correlation function

spec = afmch.spinwave({[0 0 0] [1 0 0] 501});
spec = sw_egrid(spec,'component',{'Sxx' 'Syy' 'Szz'});

clf
sw_plotspec(spec,'mode','disp','linestyle','-','colormap',[0 0 0])
colorbar off
legend off
sw_plotspec(spec,'mode','color','dE',0.5,'axLim',[0 1]);
hold on
hLegend = legend;
set(hLegend,'location','southeast')


%% anisotropic exchange on the AFM chain
% rotated anisotropy

afmch = spinw;
afmch.genlattice('lat_const',[3 4 4])
afmch.addatom('r',[  0 0 0],'S',1)

R = sw_rotmatd([0 0 1],45);
J1 = diag([3 4 4.1]);
J1 = R*J1*R';

afmch.addmatrix('label','J_1','value',J1)

afmch.gencoupling
afmch.addcoupling('mat','J_1','bond',1)


afmch.genmagstr('mode','helical','S',[0 0 1]','k',[1/2 0 0],'n',[1 0 0],'nEXt',[2 1 1])
%plot(afmch)

%% spin-spin correlation function

spec = afmch.spinwave({[0 0 0] [1 0 0] 501});
spec = sw_neutron(spec,'uv',{[1 1 0] [-1 1 0]},'pol',true);
spec = sw_egrid(spec,'component',{'Sxx+Sxy' 'Sxx-Sxy'});

clf
sw_plotspec(spec,'mode','disp','linestyle','-','colormap',[0 0 0])
colorbar off
legend off
sw_plotspec(spec,'mode','color','dE',0.5,'axLim',[0 1]);
hold on
hLegend = legend;
set(hLegend,'location','southeast')





##### SOURCE END #####</literal>
-->