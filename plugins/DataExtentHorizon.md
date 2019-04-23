---
title: DataExtentHorizon - Create a 3D horizon
description: creates a constant Z value 3D horizon which covers user selected 2D and 3D seismic data
layout: page
pager: true
tags: plugin
---

{% from 'util.html' import figure %}
{% from 'util.html' import table_with_hdr %}

This plugin, for the open source seismic interpretation platform [opendtect] Version 6.4.0 or later, creates a constant Z value 3D horizon which covers the extent of 2D and 3D seismic data in an [opendtect] survey/project. With the horizon displayed it is possible to draw fault polygons and grid clipping polygons that extend beyond the 3D survey definition. These can then be used in the Grid 2D-3D plugin to produce structure maps that extend across both 2D and 3D seismic interpretation in an [opendtect] survey/project.

## Description

The plugin adds a "Covering 2D-3D Data Extent..." item to the "New" menu option for 3D Horizon items in the data display tree. Selecting the item opens a dialog box for:

-  Specifying a constant Z value for the output horizon
-  Selecting 2D and 3D seismic data that the horizon should cover
-  Specifying the name of the generated horizon

{{ figure('dataextenthorizon.jpg', 'Example of an horizon created by the plugin and various polygons drawn across the extent of the 2D and 3D seismic data in the project') }}

## Input Parameters

{{ figure('dataextenthorizon_input.jpg', 'DataExtentHorizon plugin input dialog') }}

