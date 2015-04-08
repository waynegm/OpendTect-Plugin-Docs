## Description
This External Attribute smooths the data by fitting a second order 3D polynomial to a region of data around each sample location using gaussian weighted least squares. For regularly sampled data the fit can be calculated very efficiently by convolution. As a filter it preserves steep dips and fault cuts better than a simple spatial average. 

There are 2 versions of the attribute:

* [ex_lpa_smooth.py](https://gist.github.com/waynegm/bff2e62490dda32a74b4) - which uses the 3D convolution filter included in scipy.ndimage

* [ex_lpa_smooth_numba.py](https://gist.github.com/waynegm/bff2e62490dda32a74b4) - which uses the [Numba JIT compiler](http://numba.pydata.org/) to dramatically speed up the convolution. My own tests show a 3-4 times increase in throughput.

## Examples
<div class="juxtapose" style="margin:0px;padding:0px" data-startingposition="50" data-showlabels="true" data-showcredits="false" data-animate="false" data-mode="horizontal">
<img src="./images/lpa_input.jpg" data-label="Input" data-credit="">
<img src="./images/lpa_5x5x5.jpg"  data-label="lpa 5x5x5 WF: 0.5" data-credit="">
</div>

## Input Parameters
![Input Parameters](images/lpa_smooth_inputpar.jpg "LPA smoothing filter input parameters")

| NAME             | DESCRIPTION |
|------------------|-------------|
| Z window (+/-samples) | Specifies the extent of the analysis cube in the Z direction. Number of Z samples in cube will be 2*Z_window+1.{: style="width:60%"} |
| Stepout               | Specifies the inline and crossline extent of the analysis cube. Number of samples in each direction will be 2*Stepout+1. |
| Weight Factor         | Determines the extent of the gaussian weight function used in the weighted least squares approximation.  A value of 0.15 gives near zero weight for points at the extent of the analysis cube. |

Increasing either the Weight Factor or analysis cube size increases the smoothing.

## References
[Anisotropic Multidimensional Savitzky Golay kernels for Smoothing, Differentiation and Reconstruction](http://www.doc.ic.ac.uk/research/technicalreports/2006/DTR06-8.pdf)

[Polynomial Expansion for Orientation and Motion Estimation](http://www.diva-portal.org/smash/get/diva2:302485/FULLTEXT01.pdf)

