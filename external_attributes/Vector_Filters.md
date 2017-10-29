---
title: Vector Filter
description: vector filter orientation (inline and crossline dip) data
layout: page
pager: true
tags: external-attribute filter
---

{% from 'util.html' import figure %}
{% from 'util.html' import table_with_hdr %}

__Script: ex_vector_filter_dip.py__

## Description
This [../plugins/ExternalAttrib] script can be used to apply a vector filter to orientation ( inline and crossline dip) data. The script offers a choice of mean vector, L1 vector median and L2 vector median filters.

Initially the inline and crossline dip data are converted to a normal vector to the local orientation: $ \[x_i, y_i, z_i\] $. 

The Mean Vector Filter averages of the vector components of the orientation normal vectors in the analysis cube:
$$
\Big\[x_f, y_f, z_f\Big\]  = \frac{1}{N} \Big\[\sum\limits_{i}^N x_i, \sum\limits_{i}^N y_i, \sum\limits_{i}^N z_i\Big\]
$$

The L1 vector filter finds the normal vector in the analysis cube whose sum of absolute distance from all the others is a minimum:
$$
\Big\[x_f, y_f, z_f\Big\] = argmin \sum\limits_{i}^N \Big\[|x_f-x_i| + |y_f-y_i| + |z_f-z_i|\Big\]
$$

The L2 vector filter finds the normal vector in the analysis cube whose sum of squared distance from all the others is a minimum:
$$
\Big\[x_f, y_f, z_f\Big\] = argmin \sum\limits_{i}^N \Big\[(x_f-x_i)^2 + (y_f-y_i)^2 + (z_f-z_i)^2\Big\]
$$


The filtered orientation can be output as any of the following:
{% set outtable=[
['OUTPUT','DESCRIPTION'],
['Inline Dip','Event dip observed on a crossline in microseconds per metre for time surveys and millimetres per metre for depth surveys. Output can be positive or negative with the convention that events dipping towards larger inline numbers producing positive dips.'],
['Crossline Dip','Event dip observed on an inline in microseconds per metre for time surveys and millimetres per metre for depth surveys. Output can be positive or negative with the convention that events dipping towards larger crossline numbers producing positive dips.'],
['True Dip','Event dip in microseconds per metre for time surveys and millimetres per metre for depth surveys. Output is always positive.'],
['Dip Azimuth','Azimuth of the True Dip direction relative to the survey orientation. Output ranges from -180 to 180 degrees. Positive azimuth is defined from the inline in the direction of increasing crossline numbers. Azimuth = 0 indicates that the dip is dipping in the direction of increasing crossline numbers. Azimuth = 90 indicates that the dip is dipping in the direction of increasing inline numbers.']]
%}
{{ table_with_hdr(outtable,hdrstyle=['col-xs-4','col-xs-8'],style='table-striped table-bordered table-responsive') }}


The script requires the Numba Python package.

## Examples
{{ figure('ex_phase_dip.jpg', 'Unfiltered phase dip - crossline dip on an inline') }}

{{ figure('ex_vfmean_phase_dip.jpg', 'Mean vector filtered phase dip - 3x3x3 (Stepout and ZWindow of 1)') }}

{{ figure('ex_vfl1_phase_dip.jpg', 'L1 vector median filtered phase dip - 3x3x3 (Stepout and ZWindow of 1)') }}

{{ figure('ex_vfl2_phase_dip.jpg', 'L2 vector median filtered phase dip - 3x3x3 (Stepout and ZWindow of 1)') }}

## Input Parameters
{{ figure('ex_vector_filter_dip_input.jpg', 'ex_vector_filter_dip.py input parameters') }}

{% set inputtable=[
['NAME','DESCRIPTION'],
['Output','What to calculate - choice of inline dip, crossline dip, true dip or dip azimuth.'],
['Z window (+/-samples)','Specifies the extent of the analysis cube in the Z direction. Number of Z samples in cube will be $ 2*Zwindow+1 $.'],
['Stepout','Specifies the inline and crossline extent of the analysis cube. Number of samples in each direction will be $ 2*Stepout+1 $.'],
['Filter','Choice of Mean Dip, L1 Vector Median or L2 Vector Median.']]
%}
{{ table_with_hdr(inputtable,hdrstyle=['col-xs-4','col-xs-8'],style='table-striped table-bordered table-responsive') }}




