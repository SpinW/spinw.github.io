---
layout: MATLAB
title: SpinW class
toc: "headers: 'h2'"
---

<div id="toc"></div>

To perform calculation using the SpinW library, we need to create an object (sw class type). 
It stores all the necessary parameters for the calculation (crystal structure, interactions, magnetic structure, etc.). 
In the object oriented programming dictionary, the data stored in an object, are called properties. 
Beside the data, the object also has assigned functions that perform different computations on the object data. 
These functions are called methods and they take the object as first input argument. 
To create an sw class object you can simply type:

<pre class="codeinput">model1 = sw</pre>

<pre class="codeoutput">sw object (symbolic: off, symmetry: on, textoutput: "stdout")
lattice
         angle: [1x3 double]
     lat_const: [1x3 double]
           sym: [1x1 integer]
unit_cell
             r: [3xnAtom double]  nAtom=0
             S: [1xnAtom double]
         label: [1xnAtom char]
         color: [3xnAtom integer]
twin
           vol: [1xnTwin double]  nTwin=1
          rotc: [3x3xnTwin double]
matrix
           mat: [3x3xnJ double]  nJ=0
         color: [3xnJ integer]
         label: [1xnJ char]
single_ion
         aniso: [1xnMagAtom integer]  nMagAtom=0
             g: [1xnMagAtom integer]
         field: [1x3 double]
             T: [1x1 double]
coupling
            dl: [3xnCoupling integer]  nCoupling=0
         atom1: [1xnCoupling integer]
         atom2: [1xnCoupling integer]
       mat_idx: [3xnCoupling integer]Please note: The claim for Per-Diem and reimbursements must be submitted no later than 3 months after returning from the business trip, ESS-0183602, Rules for Travel Allowance.
           idx: [1xnCoupling integer]
mag_str
         N_ext: [1x3 integer]
             k: [1x3 double]
             S: [3xnMagExt double]  nMagExt=0
             n: [1x3 double]
unit
            kB: [1x1 double]
           muB: [1x1 double]
</pre>

## Properties

The output of the previous command shows all the data fields of model1. Each data field has an initial value and any of them can be modified directly:

<pre class="codeoutput"> ans = 

    int32 
</pre>

Thus if we want to change it directly, we need an integer number:

<pre class="codeinput">model1.lattice.sym = int32(5);</pre>

This will change the crystal space group to `C 2`. To avoid most common mistakes, there are several methods (functions) for modifying the above properties that also perform additional error checking and makes certain input conversions. For example all lattice related properties can be modified using the `genlattice()` function:

<pre class="language-matlab">model1 = genlattice(<span class="string">'lat_const'</span>,[3 5 5],<span class="string">'sym'</span>,<span class="string">'C 2'</span>,<span class="string">'angled'</span>,[90 90 90]) </pre>

The alternative usage of the above function is the following:

<pre class="language-matlab">genlattice(model1,<span class="string">'lat_const'</span>,[3 5 5],<span class="string">'sym'</span>,<span class="string">'C 2'</span>,<span class="string">'angled'</span>,[90 90 90])</pre>

This reflects better the input argument structure. The first argument is the sw object `model1`. After the first argument comes option name and value pairs. The first options is `lat_const` and the value it expects is a vector with 3 elements if the input vector has different length, the function throws an error. The second option is `sym` that also accepts string input (name of the space group) that is automatically converted to the index of the space group and stored in model1:

<pre class="codeinput">model1.lattice.sym
</pre>
<pre class="codeoutput">
ans = 5 </pre>

The last option is `angled` that requires a vector with three elements and defines the alpha, beta, gamma lattice angles in degree. This will be converted into radian and stored:

<pre class="codeinput">model1.lattice.angle</pre>

<pre class="codeoutput">ans =

    1.5708    1.5708    1.5708
</pre>

### Complete list of properties

There are eight public properties of sw each with several subfields: 

<div>
    <ul>
    <li><a href="/SWproperties#lattice">spinw.lattice</a></li>
    <li><a href="/SWproperties#unit_cell">spinw.unit_cell</a></li>
    <li><a href="/SWproperties#twin">spinw.twin</a></li>
    <li><a href="/SWproperties#matrix">spinw.matrix</a></li>
    <li><a href="/SWproperties#single_ion">spinw.single_ion</a></li>
    <li><a href="/SWproperties#coupling">spinw.coupling</a></li>
    <li><a href="/SWproperties#mag_str">spinw.mag_str</a></li>
    <li><a href="/SWproperties#unit">spinw.unit</a></li>
    </ul>
</div>

## Methods

In line with the above example the general argument structure of the method functions is one of the following:
<pre class="language-matlab"><span class="keyword">function</span>(obj,<span class="string">'Option1'</span>,Value1,<span class="string">'Option2'</span>,Value2,<span class="keyword">...</span><span class="comment">)</span>
<span class="keyword">function</span>(obj,Value1,Value2,<span class="keyword">...</span><span class="comment">)</span></pre>

The first type of argument list is used for functions that require variable number of input parameters with default values. The second type of argument structure is used for functions that require maximum up to three fixed input parameter. Every method has help that can be called by one of the following methods:

* selecting the function name in the Editor/Command Window and pressing F1
* in the Command Window typing for example:


<pre class="language-matlab">help <span class="string">sw.genlattice</span></pre>

This shows the help of the genlattice() function in the Command Window. To open the help in a separate window you need to write:

<pre class="language-matlab">doc <span class="string">sw.genlattice</span></pre>

To unambiguously identify the functions it is usefull to refer them as sw.function() this way matlab knows which function to select from several that has the same name. For example the plot() funcion is also defined for the sw class. However by writing:

<pre class="language-matlab">help <span class="string">plot</span></pre>

we get the help for the standard Matlab plot function. To get what we want use:

<pre class="language-matlab">help <span class="string">sw.plot</span></pre>

By the way this function is one of the most usefull ones. It can show effectively all information stored in the sw object by plotting crystal structure, couplings, magnetic structure etc. Calling it on an empty object shows only the unit cell:

<pre class="codeinput">plot(model1)</pre>

<img vspace="5" hspace="5" src="/img/gen_Swclass_01.png" alt=""></pre>

As you might noticed, there is an alternative calling of any method function: obj.function(...), this is just equivalent to the previous argument structures.

## Copy

The sw class belong to the so called handle class. It means in short that the model1 variable is just a pointer to the memory where the class is stored. Thus doing the following:

<pre class="language-matlab">model2 = model1;</pre>

It only copies the pointer. Thus if I change something on model1, model2 will change as well. Thus to clone the object (the equivalent of the usual '=' operation in Matlab) is the copy() function:

<pre class="language-matlab">model2 = copy(model1); </pre>


<script type="text/javascript">
$(document).ready(function() {
    $('#toc').toc();
});

</script>

<sript src="/js/toc.js"></sript>