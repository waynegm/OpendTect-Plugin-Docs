## Description
This External Attribute smooths the data by fitting a second order 3D polynomial to a region of data around each sample location using gaussian weighted least squares. For regularly sampled data the fit can be calculated very efficiently by convolution. As a filter it preserves steep dips and fault cuts better than a simple spatial average. 

There are 2 versions of the attribute:

* [ex_lpa.py](https://gist.github.com/waynegm/bff2e62490dda32a74b4) - which uses the 3D convolution filter included in scipy.ndimage

* [ex_lpa_numba.py](https://gist.github.com/waynegm/bff2e62490dda32a74b4) - which uses the [Numba JIT compiler](http://numba.pydata.org/) to dramatically speed up the convolution. This version is approximately 4 times faster.

## Examples
<div class="juxtapose" style="margin:0px;padding:0px" data-startingposition="50" data-showlabels="true" data-showcredits="false" data-animate="false" data-mode="horizontal">
<img src="./images/lpa_input.jpg" data-label="Input" data-credit="">
<img src="./images/lpa_5x5x5.jpg"  data-label="lpa 5x5x5 WF: 0.5" data-credit="">
</div>

## References
[Anisotropic Multidimensional Savitzky Golay kernels for Smoothing, Differentiation and Reconstruction](www.doc.ic.ac.uk/research/technicalreports/2006/DTR06-8.pdf)

[Polynomial Expansion for Orientation and Motion Estimation](www.diva-portal.org/smash/get/diva2:302485/FULLTEXT01.pdf)

