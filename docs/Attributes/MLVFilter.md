# MLV Filter

Structure preserving Mean of Least Variance Filter plugin for open source seismic interpretation platform <a href="http://www.opendtect.org/" target="_blank">OpendTect</a>.

## Description

This attribute is an implementation of a mean of least variance filter [Schulze & Pearce (1993)](http://proceedings.spiedigitallibrary.org/proceeding.aspx?articleid=1008684 "Value-and-criterion filters: a new filter structure based on morphological opening and closing. Mark A. Schulze and John A. Pearce. Proc. SPIE 1902, Nonlinear Image Processing IV, 106 (May 21, 1993)") where the analysis elements are all the possible planes through the sample points in the analysis block. This algorithm may be similar to that proposed by [Al-Dossary & Wang (2011)](http://library.seg.org/doi/abs/10.1190/1.3627375 "Structure‐preserving smoothing for 3D seismic attributes. Saleh Al‐Dossary and Yuchun Eugene Wang. SEG Technical Program Expanded Abstracts 2011. January 2011, 1004-1008"). 

The sample variance for all samples on each analysis element is calculated and the output statistic (average, mean or element index) is output for the element with the least variance. 

The following figure shows the relationship between the geometry of the analysis elements and the element index.

![Element Index](../../images/MLVFilterAttrib_elements.jpg "MLV Filter analysis elements")

## Examples
<div class="juxtapose" style="margin:0px;padding:0px" data-startingposition="50" data-showlabels="true" data-showcredits="false" data-animate="false" data-mode="horizontal">
<img src="../../images/MLVFilterAttrib_input.jpg" data-label="Input" data-credit="">
<img src="../../images/MLVFilterAttrib_MLV3_Mean.jpg"  data-label="MLV Size 3 Average - 1 pass" data-credit="">
</div>

<div class="juxtapose" style="margin:0px;padding:0px" data-startingposition="50" data-showlabels="true" data-showcredits="false" data-animate="false" data-mode="horizontal">
<img src="../../images/MLVFilterAttrib_MLV5_Mean.jpg" data-label="MLV Size 5 Average - 1 pass" data-credit="">
<img src="../../images/MLVFilterAttrib_MLV3_Mean2.jpg"  data-label="MLV Size 3 Average - 2 passes" data-credit="">
</div>

**MLV Size 3 Elements over Input**

![MLV 3 Elements](../../images/MLVFilterAttrib_MLV3_Elements.jpg "MLV 3 elements")

## Input Parameters

This attribute has 2 parameters:

| NAME             | DESCRIPTION |
|------------------|-------------|
| Filter size | Specifies a cube of samples centred  at the analysis location. Increasing the size will increase the degree of smoothing at the risk of smearing structural features. As the examples show it may be better to apply multiple passes of a small size filter than a single pass of a larger filter to reduce the risk of artifacts in the output. OpendTect makes it really easy to cascade multiple filter passes.{: style="width:60%"} |
| Output statistic | What the filter will output. The options are average, median or the element index. The element index is included for curiosity and quality control. Generally the default *Average* provides the most pleasing output. |

![Input Parameters](../../images/MLVFilterAttrib_par1.jpg "MLF Filter input parameters")


