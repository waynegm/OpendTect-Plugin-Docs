---
title: GeopackageDisplay
description: display lines and polylines in a Geopackage database on an OpendTect 3D horizon
layout: page
pager: true
tags: plugin
---

{% from 'util.html' import figure %}
{% from 'util.html' import table_with_hdr %}

This is an extension of the [geopackageexport] plugin that displays lines and polylines from a Geopackage database file over an [opendtect] 3D horizon.

## Description

The plugin adds a "Geopackage Display" item to the "Add" context menu of 3D Horizons in the scene tree. Selecting the item opens a dialog box for selecting the Geopackage file, the layer to display and the line color and width. Multiple layers can be displayed.

{{ figure('geopackage_display_menu.jpg', 'Geopackage Display menu item') }}

### Notes
-  The plugin requires the survey to have a projection based CRS defined.
-  This plugin is actually part of the [geopackageexport] plugin - see notes there as well 

{{ figure('geopackage_display_example.jpg', 'GIS data draped on an OpendTect 3D horizon') }}


