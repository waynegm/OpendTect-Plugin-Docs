---
title: GradientAttrib
description: calculate inline, crossline and time/depth gradients
layout: page
pager: true
tags: plugin
---

{% from 'util.html' import figure %}
{% from 'util.html' import table_with_hdr %}

This attibute plugin for the open source seismic interpretation platform [opendtect] Version 6.0.0 or later calculates inline, crossline and time/depth gradients.

## Description

This plugin calculates the inline, crossline or time/depth gradient using operators optimised for rotation invariance, ie equal response in all directions, proposed  by [Kroon (2009)](http://www.k-zone.nl/Kroon_DerivativePaper.pdf "NUMERICAL OPTIMIZATION OF KERNEL BASED IMAGE DERIVATIVES. Dirk-Jan Kroon, University of Twente, Enschede") and [Farid and Simoncelli(2004)](http://www.cns.nyu.edu/pub/lcv/farid03-reprint.pdf "Differentiation of Discrete Multidimensional Signals. Hany Farid and Eero P. Simoncelli, IEEE TRANSACTIONS ON IMAGE PROCESSING, VOL. 13, NO. 4, APRIL 2004"). These provide more accurate alternatives to the Prewitt filter option of the OpendTect Convolve attribute for computing gradients.

The attribute offers a choice of Kroon's 3x3x3, Farid and Simoncelli's 5x5x5 or Farid and Simoncelli's 7x7x7 operator. The following figures demonstrate the relative accuracy of these operators and the OpendTect Prewitt filter on a simple periodic signal (top left) with event dip angle shown top right. Gradients calculated using each operator are used to compute the event dip angle and the absolute dip angle error. The superior accuracy of the operators provided by this attribute is clear.

{{ figure('gradient_attrib.jpg', 'Accuracy of the gradient attribute operators') }}

## Input Parameters

This attribute has 3 parameters:

{% set inputtable=[
['NAME','DESCRIPTION'],
['Input Volume','The input attribute volume.'],
['Output Gradient','What to calculate - choice of Inline, Crossline or Z gradient.'],
['Operator', 'What operator to use - choice of Kroon\'s 3x3x3, Farid\'s 5x5x5 or Farid\'s 7x7x7.']]
%}
{{ table_with_hdr(inputtable,hdrstyle=['col-xs-4','col-xs-8'],style='table-striped table-bordered table-responsive') }}


{{ figure('GradientAttrib_input.jpg', 'Gradient attribute input parameter dialog') }}


