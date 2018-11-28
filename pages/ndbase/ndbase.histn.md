---
{title: ndbase.histn, link: ndbase.histn, summary: calculates histogram of arbitrary
    dimensional data, keywords: sample, sidebar: sw_sidebar, permalink: ndbase_histn,
  folder: ndbase, mathjax: true}

---
 
function [Ysum, Nsum, Cbin] = NDBASE.HISTN(X,Y,bin1,bin2,...,'option1',value1)
 
Any data point with NaN X or Y value is omitted from the binning. Works
for non-uniform bins and also optimised for uniform bins with significant
speedup.
 
Input:
 
X         Array with size of [nPoint nDim], that represents
          positions in the nDim dimensional space (R^nDim).
Y         Column vector with nPoint element, that represents values at
          the points defined in X. {X,Y} defines a scalar field in the
          nDim dimensional space. If Y contains multiple columns, each
          column will be binned independently and saved into Ysum in
          separate columns, this can represent vector field at X. The
          dimensions of the vector field is nField, if the size of Y is
          [nPoint nField].
binI      Row vectors that define BIN EDGES along the I-th dimension.
          It goes from 1 to nDim. Each vector has to have at least two
          elements. The number of bins along the I-th dimension is equal
          to the number of elements in the binI vector minus one. Thus:
              nBinI = numel(binI)-1
 
Options:
 
emptyval  Value for empty bins in Ysum and Nsum:
              emptyval = [emptyY emptyN]
          Default value is [NaN 0].
 
Output:
 
Ysum      Array with size of [nBin1 nBin2 nBin3 ... nField]. Each pixel
          contains the sum of the elements of Y that are within the
          given bin boundaries:
              bin1(i1) <= X(:,i1) < bin1(i1+1) and
              	...
              binN(iN) <= X(:,iN) < binN(iN+1)
          Points of X, that are outside of the bin boundaries are
          omitted. Empty pixels will contain NaN by default.
Nsum      Column vector with the same number of rows as Ysum, contains
          the number of points that are contributing to the pixel. Only
          calculated if two output is expected. Empty pixels will contain
          the value 0 by default. To make it possible to calculate the
          average value of each pixel, set the default value to 1, then
          devide Ysum with Nsum element vise:
              Yavg = bsxfun(@rdivide,Ysum,Nsum);
Cbin      Center bin positions, if nDim=1 the values are stored in a row
          vector. If nDim>1 the center bin vectors are packed into a
          cell.
 
Example:
 
Random points in 2D.
 
nPoint = 1e3;
nDim   = 2;
bin = linspace(0,1,101);
 
X = rand(nPoint,nDim);
Y = sin(X(:,1)*2*pi);
[Ysum,Nsum] = ndbase.histn(X,Y,bin,bin);
figure
imagesc(Ysum./Nsum);
 
 
Create points on a square lattice.
 
[xx,yy] = ndgrid(1:0.5:10,1:0.5:10);
 
bin = linspace(0,11,101);
 
[Ysum,Nsum] = ndbase.histn([xx(:) yy(:)],sin(xx(:)),bin,bin);
figure
imagesc(Ysum./Nsum);
 
Oversample the sine function defined on a finite point.
xx = 0:0.5:10;
bin = linspace(0,11,101);
 
Ysum = ndbase.histn([xx(:)],sin(xx(:)),bin);
figure
plot(Ysum,'o-');
 
See also accumarray, interp1.

{% include links.html %}
