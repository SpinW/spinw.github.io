---
layout: tutorial
title: Tutorial 33
subtitle: Introduction to Plotting Chemistry
---

<div class="content"><h1>Introduction to Plotting Chemistry</h1><!--introduction--><p>We don't care what is this model, we just test the plotting capabilities of SpinW.</p><!--/introduction--><h2>Contents</h2><div><ul><li><a href="#1">Define the lattice</a></li><li><a href="#2">Customizing the plot 1.</a></li><li><a href="#3">Customizing the plot 2.</a></li><li><a href="#4">Overplotting a polyhedron</a></li></ul></div><h2 id="1">Define the lattice</h2><pre class="codeinput">symStr = <span class="string">'-z, y+3/4, x+3/4; z+3/4, -y, x+3/4; z+3/4, y+3/4, -x; y+3/4, x+3/4, -z; x+3/4, -z, y+3/4; -z, x+3/4, y+3/4'</span>;
model = spinw;
a = 10.0307;
model.genlattice(<span class="string">'lat_const'</span>,[a a a],<span class="string">'angled'</span>,[90 90 90],<span class="string">'spgr'</span>,symStr,<span class="string">'label'</span>,<span class="string">'F d -3 m Z'</span>)
model.addatom(<span class="string">'label'</span>,<span class="string">'Yb3+'</span>,<span class="string">'r'</span>,[1/2 1/2 1/2],<span class="string">'S'</span>,1/2)
model.addatom(<span class="string">'label'</span>,<span class="string">'Ti4+'</span>,<span class="string">'r'</span>,[0 0 0])
model.addatom(<span class="string">'label'</span>,<span class="string">'O2-'</span>,<span class="string">'r'</span>,[0.3318 1/8 1/8])
model.addatom(<span class="string">'label'</span>,<span class="string">'O2-'</span>,<span class="string">'r'</span>,[3/8 3/8 3/8])
model.gencoupling
model.addmatrix(<span class="string">'label'</span>,<span class="string">'J1'</span>,<span class="string">'value'</span>,1)
model.addmatrix(<span class="string">'label'</span>,<span class="string">'g0'</span>,<span class="string">'value'</span>,1);
model.addcoupling(<span class="string">'mat'</span>,<span class="string">'J1'</span>,<span class="string">'bond'</span>,1)
model.addg(<span class="string">'g0'</span>)
model.matrix.mat(:,:,2) =  -0.84*ones(3)+4.32*eye(3);
model.getmatrix(<span class="string">'mat'</span>,<span class="string">'J1'</span>);
J1 = -0.09; J2 = -0.22; J3 = -0.29; J4 = 0.01;
model.setmatrix(<span class="string">'mat'</span>,<span class="string">'J1'</span>,<span class="string">'pref'</span>,[J1 J3 J2 -J4]);
</pre><h2 id="2">Customizing the plot 1.</h2><p>We setup the number of triangular faces to be produced by the plot command using swpref. Each atom is an icosahedron, where each face is subdivided into triangles nmesh-times (see swplot.icomesh function). Thus nmnesh=3 will make all sphere to have 1280 faces. npatch determines the number of subdivision of the circle that is used to generate cylinders an arrows (swplot.arrow and swplot.cylinder).</p><pre class="codeinput">pref = swpref;
pref.set({<span class="string">'nmesh'</span>, <span class="string">'npatch'</span>}, {3, 50})

<span class="comment">% The high level spinw.plot command calls lower level commands</span>
<span class="comment">% (swplot.plotatom, swplot.plotion, swplot.plotbond, etc). For details</span>
<span class="comment">% check the documentation of spinw.plot or any of the lower level</span>
<span class="comment">% functions. Any option of the lower level functions can be controlled by</span>
<span class="comment">% making new options as: lowlevelfunname + lowlevelfunoption, for example</span>
<span class="comment">% to set the color option of the swplot.plotatom function set 'atomColor'</span>
<span class="comment">% option in the spinw.plot method as in the example below. The low level</span>
<span class="comment">% functions can be also called separately.</span>

plot(model,<span class="string">'tooltip'</span>,false,<span class="string">'atomMode'</span>,<span class="string">'mag'</span>,<span class="string">'atomColor'</span>,<span class="string">'gold'</span>)

<span class="comment">% Move the atoms by shifting positions by 10 Angstrom to the right.</span>
swplot.plotatom(<span class="string">'shift'</span>,[10 0 0]',<span class="string">'mode'</span>,<span class="string">'mag'</span>,<span class="string">'replace'</span>,true)
</pre><img vspace="5" hspace="5" src="/tutorial33_01.png" alt=""> <h2 id="3">Customizing the plot 2.</h2><p>We show only the bonds and the atoms and changing colors.</p><pre class="codeinput">model.plot(<span class="string">'atomMode'</span>,<span class="string">'mag'</span>,<span class="string">'bondMode'</span>,<span class="string">'cylinder'</span>,<span class="keyword">...</span>
    <span class="string">'bondLinewidth0'</span>,3,<span class="string">'bondColor'</span>,<span class="string">'orange'</span>,<span class="string">'bondMode2'</span>,<span class="string">'none'</span>,<span class="keyword">...</span>
    <span class="string">'atomColor'</span>,<span class="string">'pink'</span>,<span class="string">'legend'</span>,false,<span class="string">'baseLabel'</span>,false,<span class="keyword">...</span>
    <span class="string">'cellMode'</span>,<span class="string">'none'</span>,<span class="string">'tooltip'</span>,true)
</pre><img vspace="5" hspace="5" src="/tutorial33_02.png" alt=""> <h2 id="4">Overplotting a polyhedron</h2><p>We overplot a tetrahedron between 4 magnetic atoms. The positions are in lattice units. Also Angstrom can be used by setting the 'unit' option of swplot.plot function to 'xyz'.</p><pre class="codeinput">R =[1/2 3/4 3/4;<span class="keyword">...</span>
    1/2 1/2 1/2;<span class="keyword">...</span>
    3/4 3/4 1/2;<span class="keyword">...</span>
    3/4 1/2 3/4];

swplot.plot(<span class="string">'type'</span>,<span class="string">'polyhedron'</span>,<span class="string">'position'</span>,permute(R,[2 3 1]))
</pre><img vspace="5" hspace="5" src="/tutorial33_03.png" alt=""> <p class="footer"><br><a href="https://www.mathworks.com/products/matlab/">Published with MATLAB&reg; R2018b</a><br></p></div><!--
<literal>##### SOURCE BEGIN #####
%% Introduction to Plotting Chemistry
% We don't care what is this model, we just test the plotting capabilities
% of SpinW.

%% Define the lattice
symStr = '-z, y+3/4, x+3/4; z+3/4, -y, x+3/4; z+3/4, y+3/4, -x; y+3/4, x+3/4, -z; x+3/4, -z, y+3/4; -z, x+3/4, y+3/4';
model = spinw;
a = 10.0307;
model.genlattice('lat_const',[a a a],'angled',[90 90 90],'spgr',symStr,'label','F d -3 m Z')
model.addatom('label','Yb3+','r',[1/2 1/2 1/2],'S',1/2)
model.addatom('label','Ti4+','r',[0 0 0])
model.addatom('label','O2-','r',[0.3318 1/8 1/8])
model.addatom('label','O2-','r',[3/8 3/8 3/8])
model.gencoupling
model.addmatrix('label','J1','value',1)
model.addmatrix('label','g0','value',1);
model.addcoupling('mat','J1','bond',1)
model.addg('g0')
model.matrix.mat(:,:,2) =  -0.84*ones(3)+4.32*eye(3);
model.getmatrix('mat','J1');
J1 = -0.09; J2 = -0.22; J3 = -0.29; J4 = 0.01;
model.setmatrix('mat','J1','pref',[J1 J3 J2 -J4]);

%% Customizing the plot 1.
% We setup the number of triangular faces to be produced by the plot
% command using swpref. Each atom is an icosahedron, where each face is
% subdivided into triangles nmesh-times (see swplot.icomesh function). Thus
% nmnesh=3 will make all sphere to have 1280 faces. npatch determines the
% number of subdivision of the circle that is used to generate cylinders an
% arrows (swplot.arrow and swplot.cylinder).
pref = swpref;
pref.set({'nmesh', 'npatch'}, {3, 50})

% The high level spinw.plot command calls lower level commands
% (swplot.plotatom, swplot.plotion, swplot.plotbond, etc). For details
% check the documentation of spinw.plot or any of the lower level
% functions. Any option of the lower level functions can be controlled by
% making new options as: lowlevelfunname + lowlevelfunoption, for example
% to set the color option of the swplot.plotatom function set 'atomColor'
% option in the spinw.plot method as in the example below. The low level
% functions can be also called separately.

plot(model,'tooltip',false,'atomMode','mag','atomColor','gold')

% Move the atoms by shifting positions by 10 Angstrom to the right.
swplot.plotatom('shift',[10 0 0]','mode','mag','replace',true)

%% Customizing the plot 2.
% We show only the bonds and the atoms and changing colors.

model.plot('atomMode','mag','bondMode','cylinder',...
    'bondLinewidth0',3,'bondColor','orange','bondMode2','none',...
    'atomColor','pink','legend',false,'baseLabel',false,...
    'cellMode','none','tooltip',true)

%% Overplotting a polyhedron
% We overplot a tetrahedron between 4 magnetic atoms. The positions are in
% lattice units. Also Angstrom can be used by setting the 'unit' option of
% swplot.plot function to 'xyz'.

R =[1/2 3/4 3/4;...
    1/2 1/2 1/2;...
    3/4 3/4 1/2;...
    3/4 1/2 3/4];

swplot.plot('type','polyhedron','position',permute(R,[2 3 1]))


##### SOURCE END #####</literal>
-->