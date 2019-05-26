---
title: Grid 2D-3D Horizon
description: creates a 3D horizon/grid from 2D and 3D horizon interpretation
layout: page
pager: true
tags: plugin
---

{% from 'util.html' import figure %}
{% from 'util.html' import table_with_hdr %}

This plugin, for the open source seismic interpretation platform [opendtect] Version 6.4.0 or later, creates a 3D horizon/grid from the 2D and 3D horizon interpretation in an [opendtect] survey/project. 

## Description

The plugin adds a "Grid 2D-3D Horizon..." item to the "Processing|Create Horizon Output" menu which opens a dialog box for:

-  Selecting 2D and 3D seismic interpretation to grid
-  Specifying the output horizon name, extent and inline /crossline interval
-  Specifying a cropping polygon 
-  Specifying a set of fault polygon constraints
-  Selecting the interpolation algorithm to use

In the current release the plugin includes two gridding/interolation algorithms:

-  Continuous curvature splines with tension - [Wessel and Bercovici (1998)](https://doi.org/10.1023/A:1021713421882 "Interpolation with Splines in Tension: A Green's Function Approach. Paul Wessel and David Bercovici Mathematical Geology 1998 30:1, 77-93")
-  Inverse distance squared weighted averages

If fault constraints are provided only input data on the same side of the fault is used to interpolate a grid node.

{{ figure('grid2d-3d_lccts_nofaults.jpg', 'Example of continuous curvature spline gridding without fault constraints') }}

{{ figure('grid2d-3d_lccts_faults.jpg', 'Example of continuous curvature spline gridding with fault constraints') }}

{{ figure('grid2d-3d_idw_faults.jpg', 'Example of inverse distance squared gridding with fault constraints') }}

## Input Parameters

{{ figure('grid2d-3d_input_1.jpg', 'Grid 2D-3D horizon plugin input data selection dialog') }}

{{ figure('grid2d-3d_input_2.jpg', 'Grid 2D-3D horizon plugin input dialog, showing Bounding Box grid extent and continuous curvature interpolation settings') }}

-  Grid Extent: Two options available:
    -  Bounding Box - set the output horizon extent from the extent of the input data, adjusted to snap to the specified Inl/Crl steps
    -  Horizon - set the output horizon extent to match an existing horizon in the survey/project
-  Inl/Crl Step - Under the BoundingBox Grid Extent option the output grid spacing can be specified relative to the 3D survey step/sampling 
-  Cropping Polygon - select a polygon to crop the grid output
-  Fault Polygons - select  polygons to use as fault constraints during gridding. Suggest fault naming scheme that prefixes the polygons with "f_horizon name" to make them easy to select
-  Algorithm - Local Continuous Curvature Tension Spline parameters:
    -  Search radius - only data within a square +/- this radius  is used to estimate a grid node
    -  Tension - the spline tensioning parameter, varies from 0 (equivalent to Minimum Curvature) to 1 (equivalent to an elastic membrane) 

{{ figure('grid2d-3d_input_3.jpg', 'Grid 2D-3D horizon plugin input dialog, showing Horizon grid extent settings and inverse distance squared interpolation settings') }}

-  Algorithm - Inverse Distance Squared parameters:
    -  Search radius (if checked) - only data within a square +/- this radius  is used to estimate a grid node, otherwise use all input data (subject to the fault constaints) for each grid node.

