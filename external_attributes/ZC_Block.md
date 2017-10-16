---
title: ZC Block
description: Blocks a seismic trace between zero crossings
layout: page
pager: true
tags: external-attribute
---

{% from 'util.html' import figure %}# Zero Crossing Block

__Script: Miscellaneous/ex_zc_block.py__

## Description
This Python [../plugins/ExternalAttrib] script blocks a seismic trace between zero crossings. The block amplitude is determined by the min/max of the interval blocked.

The script requires the Numba Python package.

## Examples
This example shows the attribute output (black wiggle) over the input (variable density). To get a blocky wiggle display interpolation has to be turned off in the 2D viewer properties. 
{{ figure('ex_zc_block_example.jpg', 'Zero crossing block') }}

## Input Parameters
{{ figure('ex_zc_block_input.jpg', 'ex_zc_block.py input parameters') }}

There are no input parameters other than selection of the input volume.




