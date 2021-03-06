---
title: Spatial Filter - Circular
description: lowpass, highpass, bandpass or band reject circularly symmetric spatial filters
layout: page
pager: true
tags: external-attribute filter
---

{% from 'util.html' import figure %}
{% from 'util.html' import table_with_hdr %}

__Script: Filtering/ex_spatial_filter_circular.py__

## Description
This Python [../plugins/ExternalAttrib] script applies lowpass, highpass, bandpass or band reject circularly symmetric spatial filters. The filters are applied by direct spatial convolution using the MAXFLAT operators presented by [Khan and Ohba (2001)](https://www.researchgate.net/publication/3384111_Explicit_formulae_for_coefficients_of_2D_circular_symmetric_MAXFLATFIR_lowhigh_pass_digital_filters "Explicit formulae for coefficients of 2D circular symmetric MAXFLAT FIR low/high pass digital filters.  Electronics Letters Volume: 37, Issue: 24, 22 Nov 2001").

{{ figure('ex_spatial_filter_resp.jpg', 'Filter responses') }}

Note that the filter cutoff or band pass/reject frequency is specified in Normalised Spatial Frequency. Normalised Frequency ranges from 0 to 1 at the spatial nyquist. Converting a spatial frequency in cycles/metre to the equivalent Normalised Spatial Frequency is as simple as dividing it by the spatial nyquist frequency.

As written the filter does not take into account differences in spatial sampling in the inline and crossline directions.

## Examples
This example uses a Low Pass filter to remove acquisition footprint from the F3 Demo dataset.

{{ figure('ex_spatial_filter_fkinput.jpg', 'FK spectrum of inline 425') }}

Note the noise at 0.0133 cycles/metre or 0.67 normalised frequency (i.e. 0.0133/0.02).

A spatial low pass filter with a normalised frequency cutoff of 0.5 is very effective at attenuating this acquisition footprint.

<div class="juxtapose">
    <img src="images/ex_spatial_filter_inline_input.jpg" data-label="Input Iln425"/>
    <img src="images/ex_spatial_filter_inline_filtered.jpg"  data-label="Lowpass Filtered Iln425"/>
</div>

{{ figure('ex_spatial_filter_fkoutput.jpg', 'FK spectrum of inline 425 after filter') }}

<div class="juxtapose">
    <img src="images/ex_spatial_filter_slice_input.jpg" data-label="Input Slice300ms "/>
    <img src="images/ex_spatial_filter_slice_filtered.jpg"  data-label="Lowpass Filtered Slice300ms"/>
</div>

## Input Parameters
{{ figure('ex_spatial_filter_input.jpg', 'ex_spatial_filter.py input parameters') }}

{% set inputtable=[
['NAME','DESCRIPTION'],
['Stepout','Determines the size of the convolution operator. Minimum of 9 (filter kernel size of 19) recommended.'],
['Type','Filter type - Low Pass, High Pass, Band Pass or Band Reject.'],
['Normalised Spatial Frequency','For Low Pass and High Pass filters this specifies the filter cutoff. For Band Pass/Reject filters this is the centre of the pass/reject band. The width of the band is hardwired to +/- 0.1 in the script. The filter cutoff corresponds to the half amplitude point.']]
%}
{{ table_with_hdr(inputtable,hdrstyle=['col-xs-4','col-xs-8'],style='table-striped table-bordered table-responsive') }}




