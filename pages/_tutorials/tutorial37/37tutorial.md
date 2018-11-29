---
layout: tutorial
title: Tutorial 37
subtitle: Dispersion of a triangular lattice
---

<div class="content"><h1>Dispersion of a triangular lattice</h1><!--introduction--><!--/introduction--><h2>Contents</h2><div><ul><li><a href="#1">Define the model and compute</a></li><li><a href="#2">constant resolution</a></li></ul></div><h2 id="1">Define the model and compute</h2><pre class="codeinput">spec = sw_egrid(spinwave(sw_model(<span class="string">'triAF'</span>,1),{[0 0 0] [1 1 0] 501}));
</pre><pre class="codeoutput">Warning: To make the Hamiltonian positive definite, a small omega_tol value was
added to its diagonal! 
</pre><h2 id="2">constant resolution</h2><pre class="codeinput">figure;

<span class="comment">% plot the constant resolution value</span>
dE = 0.3;
subplot(3,2,1)
plot([0 4],[dE dE],<span class="string">'r-'</span>)
title(<span class="string">'Constant resolution function'</span>)
xlabel(<span class="string">'Energy Transfer (meV)'</span>)
ylabel(<span class="string">'FWHM energy resolution (meV)'</span>)

<span class="comment">% apply constant resolution on the simulation</span>
subplot(3,2,2)
spec = sw_instrument(spec,<span class="string">'dE'</span>,0.3);
sw_plotspec(spec,<span class="string">'mode'</span>,<span class="string">'color'</span>);


<span class="comment">% fit and plot tabulated resoltuion values and apply to the simulation</span>
EN = [0       1   2    3   4]; <span class="comment">% meV</span>
dE = [0.05 0.05 0.05 0.3 0.4]; <span class="comment">% meV</span>
R  = [EN' dE'];

subplot(3,2,3)
spec = sw_instrument(spec,<span class="string">'dE'</span>,R,<span class="string">'polDeg'</span>,3,<span class="string">'plot'</span>,true);

subplot(3,2,4)
sw_plotspec(spec,<span class="string">'mode'</span>,<span class="string">'color'</span>);

<span class="comment">% resolution is defined by user provided function (anonymous or .m file)</span>
a = 0.01;
b = 1.0;
resFun = @(x)a+b*exp(-x);

<span class="comment">% plot the user defined resolution function</span>
xVal = linspace(0,5,501);
subplot(3,2,5)
plot(xVal,resFun(xVal),<span class="string">'r-'</span>)
title(<span class="string">'Resolution function'</span>)
xlabel(<span class="string">'Energy Transfer (meV)'</span>)
ylabel(<span class="string">'FWHM energy resolution (meV)'</span>)

<span class="comment">% apply the function to the simulation</span>
subplot(3,2,6)
spec = sw_instrument(spec,<span class="string">'dE'</span>,resFun);
sw_plotspec(spec,<span class="string">'mode'</span>,<span class="string">'color'</span>);
</pre><img vspace="5" hspace="5" src="/tutorial37_01.png" alt=""> <p class="footer"><br><a href="https://www.mathworks.com/products/matlab/">Published with MATLAB&reg; R2018b</a><br></p></div><!--
<literal>##### SOURCE BEGIN #####
%% Dispersion of a triangular lattice

%% Define the model and compute
spec = sw_egrid(spinwave(sw_model('triAF',1),{[0 0 0] [1 1 0] 501}));

%% constant resolution

figure;

% plot the constant resolution value
dE = 0.3;
subplot(3,2,1)
plot([0 4],[dE dE],'r-')
title('Constant resolution function')
xlabel('Energy Transfer (meV)')
ylabel('FWHM energy resolution (meV)')

% apply constant resolution on the simulation
subplot(3,2,2)
spec = sw_instrument(spec,'dE',0.3);
sw_plotspec(spec,'mode','color');


% fit and plot tabulated resoltuion values and apply to the simulation
EN = [0       1   2    3   4]; % meV 
dE = [0.05 0.05 0.05 0.3 0.4]; % meV
R  = [EN' dE'];

subplot(3,2,3)
spec = sw_instrument(spec,'dE',R,'polDeg',3,'plot',true);

subplot(3,2,4)
sw_plotspec(spec,'mode','color');

% resolution is defined by user provided function (anonymous or .m file)
a = 0.01;
b = 1.0;
resFun = @(x)a+b*exp(-x);

% plot the user defined resolution function
xVal = linspace(0,5,501);
subplot(3,2,5)
plot(xVal,resFun(xVal),'r-')
title('Resolution function')
xlabel('Energy Transfer (meV)')
ylabel('FWHM energy resolution (meV)')

% apply the function to the simulation
subplot(3,2,6)
spec = sw_instrument(spec,'dE',resFun);
sw_plotspec(spec,'mode','color');

##### SOURCE END #####</literal>
-->