---
title: Add Noise
description: add gaussian distributed noise to an input
layout: page
pager: true
tags: external-attribute
---

{% from 'util.html' import figure %}
{% from 'util.html' import table_with_hdr %}

__Script: Miscellaneous/ex_add_noise.py__

## Description
This Python [../plugins/ExternalAttrib] script adds gaussian distributed noise to an input signal.

## Examples
This example shows an input signal with different levels of added noise.

{{ figure('ex_add_noise_example.jpg', 'Input with varying levels of added noise') }}

## Input Parameters

{{ figure('ex_add_noise_input.jpg', 'ex_add_noise.py input parameters') }}

{% set inputtable=[
['NAME','DESCRIPTION'],
['S/N Ratio','Desired signal to noise ratio.']]
%}
{{ table_with_hdr(inputtable,hdrstyle=['col-xs-4','col-xs-8'],style='table-striped table-bordered table-responsive') }}




