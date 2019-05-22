---
title: Mistie - edit/apply mistie corrections
description: edit/apply Z shifts, phase rotations and amplitude corrections to seismic data
layout: page
pager: true
tags: plugin
---

{% from 'util.html' import figure %}
{% from 'util.html' import table_with_hdr %}

This plugin, for the open source seismic interpretation platform [opendtect] Version 6.4.0 or later, allows creation and editing of a file with Z shift, phase rotations and amplitude scaling corrections for 2D and 3D seismic in an [opendtect] survey/project. The plugin also includes an attribute (Mistie Application) that will apply the corrections.

In an ideal world we would be given 2D seismic data that has consistent Z, phase and amplitude scales. In the real world this doesn't always happen and 2D seismic interpretation projects accumulate inconsistencies as more data is added. The concept implemented by this plugin is the interpreter builds/maintains the correction table as they work through the data. The virtual corrected seismic from the Mistie Application attribute can be interpreted on the fly or the interpreter can generate a new adjusted dataset and interpret that.

Future planned enhancements include:

-  Add an option to generate a correction file from the data itself that minimizes the misties in a least squares sense for all line interections 
-  Add an option to apply the Z shifts to an existing seismic interpretation

## Description

### Mistie Correction Editor
The plugin adds a "Mistie Corrections" item to the Survey-Manage main menu. Selecting the item opens the Mistie Correction Editor.

{{ figure('mistie_editor.jpg', 'Mistie correction editor') }}

The editor has toolbar buttons to:

-  Create a mistie correction set with all the  2D lines in the project (with default corrections that make no change to the  data)
-  Read (open) a mistie correction set previously saved to a file 
-  Save any updates to the currently open mistie correction set 
-  Save the current mistie correction set to a user selected file
-  Merge another mistie correction set file with the current set, optionally keeping or replacing the existing corrections where there is duplicate line/dataset names

Within the editor it is possible to:

- Add new lines/datasets and associated corrections
- Edit existing corrections
- RightMouseButton click on a row brings up a menu to insert or delete selected row(s)
- Limited clipboard copy and paste is available

You can include corrections for a particular 3D seismic volume by using a line/dataset name of the form "3D_XXXX" where the "XXXX" is the volume name, eg note the "3D_pstm" in the above figure. Multiple unique "3D_XXXX" entries are allowed to specify corrections for different 3D volumes in the project. 

If a line doesn't need a correction it can be omitted from the set and default (no change) corrections will be assumed when the Mistie Application attribute. A message (which can be safely ignored) is added to the log file when this occurs. 

The name in the line/dataset column must exactly match the project line name.

### Mistie Application Attribute
The plugin adds a "Mistie Application" attribute to the list of [opendtect] attributes.

{{ figure('mistieapplication_input.jpg', 'Mistie Application attribute input parameters') }}

The attribute parameters include:

-  The input seismic volume to be corrected
-  A file with the mistie correction set to apply
-  Which corrections to apply 

When the attribute is displayed the shift, phase rotation and amplitude scalar for the line is read from the correction file and applied.

### Notes
-  The default file extension for the mistie corrections is "mst"
-  The default file location is the __Misc__ folder in the OpendTect survey/project folder
-  The file is in the OpendTect IOPar file format. This is a simple text format which can also be modified using a text editor

