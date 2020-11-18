---
title: Mistie
description: edit/apply Z shifts, phase rotations and amplitude corrections to seismic data
layout: page
pager: true
tags: plugin
---
{% from 'util.html' import figure %}
{% from 'util.html' import table_with_hdr %}

{{ figure('mistie_plugin.jpg', '') }}

This plugin, for the open source seismic interpretation platform [opendtect] Version 6.4.0 or later, allows creation and editing of a file with Z shift, phase rotations and amplitude scaling corrections for 2D and 3D seismic in an [opendtect] survey/project. The plugin also includes an attribute (Mistie Application) that will apply the corrections.

In an ideal world we would be given 2D seismic data that has consistent Z, phase and amplitude scales. In the real world this doesn't always happen and 2D seismic interpretation projects accumulate inconsistencies as more data is added. The concept implemented by this plugin is the interpreter builds/maintains the correction table as they work through the data. The virtual corrected seismic from the Mistie Application attribute can be interpreted on the fly or the interpreter can generate a new adjusted dataset and interpret that.

## Description
The plugin provides components to:

 1. Estimate misties from seismic data or horizon interpretation 
 2. Analyse the misties and estimate corrections to minimize the misties in a least squares sense
 3. Edit/Maintain a set of mistie corrections
 4. Attribute to apply the corrections to seismic data and tools to apply Z corrections to horizon interpretation.

There are two alternative workflows to build a mistie correction file:

 1. Estimate the misties from the data and compute a mistie correction file in the [#Mistie Analysis] dialog
 2. Manually build the mistie correction file in the [#Mistie Correction Editor]

### **Mistie Analysis**
The plugin adds a "Mistie Analysis" item to the Analysis main menu. Selecting the item opens the Mistie Analysis dialog:

{{ figure('mistie_analysis.jpg', 'Mistie Analysis') }}

Actions associated with the toolbar buttons are:

{% set inputtable=[
['ICON','DESCRIPTION'],
['<img class="img-responsive" alt="New" src="images/new.png" title="New"/>','Open the Mistie Estimation dialog to estimate misties from the seismic data. Existing contents of the mistie table are erased.'],
['<img class="img-responsive" alt="Open" src="images/open.png" title="Open"/>','Load mistie estimates from a previously saved file. Existing contents of the mistie table are erased.'],
['<img class="img-responsive" alt="Save" src="images/save.png" title="Save"/>', 'Save the current mistie estimates. If the current misties were loaded from a file then that will be overwritten, otherwise user will be asked to provide a new file name.'],
['<img class="img-responsive" alt="SaveAs" src="images/saveas.png" title="SaveAs"/>', 'Prompts for a file and saves the current mistie estimates.'],
['<img class="img-responsive" alt="Merge" src="images/plus.png" title="Merge"/>', 'Prompts for another mistie file and merges the results with the mistie set currently active in the tool optionally keeping or replacing common items.'],
['<img class="img-responsive" alt="Filter" src="images/minus.png" title="Filter"/>', 'Opens a dialog to filter the misties listed in the table, used for correction calculation and displayed in the mistie report.'],
['<img class="img-responsive" alt="Calculate Corrections" src="images/attributes.png" title="Calculate Corrections"/>', 'Open the Correction Calculation dialog.'],
['<img class="img-responsive" alt="Mistie Report" src="images/xplot.png" title="Mistie Report"/>', 'Opens a web browser and displays an interactive dashboard report for the current misties and correction set active in the tool.']]
%}
{{ table_with_hdr(inputtable,hdrstyle=['col-xs-2','col-xs-10'],style='table-striped table-bordered table-responsive') }}

### **Mistie Estimation** 
The ![New](images/new.png) toolbar item in the [#Mistie Analysis] dialog opens a dialog box where the user can specify whether misties should be estimated from the seismic data or from horizon interpretation.

In the case of estimation from the seismic data the dialog looks like:

{{ figure('mistie_estimation_seismic.jpg', 'Mistie Estimation from Seismic') }}

The user can:

-  Select the data type (attribute) and which lines to include in the analysis
-  Include and select a 3D seismic volume to include in the analysis
-  Specify the trace interval along 2D lines to estimate the 2D to 3D misties, the average mistie is assigned to the 2D to 3D tie 
-  Limit the maximum time-shift or mistie to consider
-  Specify a Z window for the cross correlation of traces at line interections
-  Indicate if only time corrections should be estimated (default is to simultaneously estimate Z, phase rotation and amplitude corrections)

The default estimation of Z phase rotation and amplitude misties is based on the method described by [Bishop and Nunns (1994)](https://library.seg.org/doi/10.1190/1.1443654 "Correcting amplitude, time, and phase mis‐ties in seismic data. Thomas N. Bishop and Alan G. Nunns, GEOPHYSICS 1994 59:6, 946-953") using cross correlation of the amplitude envelope of the traces. This is the preferred method for seismic data with a reasonable bandwidth. For narrow bandwidth data (eg site survey data) the time corrections only estimation method which uses cross correlation of the raw seismic traces may generate better results.

In the case of estimation from horizon interpretation the dialog looks like:

{{ figure('mistie_estimation_horizon.jpg', 'Mistie Estimation from Horizon Interpretation') }}

The user can:

- Select a 2D horizon and set of lines to use
- Select a 3D horizon to use
- Specify the trace interval along 2D lines to estimate the 2D to 3D misties, the average mistie is assigned to the 2D to 3D tie

The Apply button will initiate the estimation of the misties, when complete results are displayed in the [#Mistie Analysis] dialog. Clicking the ![Mistie Report](images/xplot.png) icon will generate a [#Mistie Report] with histograms and scatterplot of the mistie estimates  for review.

### **Mistie Filter**
The ![Filter](images/minus.png) toolbar item in the [#Mistie Analysis] dialog opens the following dialog that allows filtering of the misties displayed in the list, used for correction calculation and included in the mistie report:

{{ figure('mistie_filter.jpg', 'Mistie filtering') }}

Activate the checkbox next to the filter to activate it. At this moment only filtering by the tie quality (correlation coefficient) is supported. The tie quality can vary from 0.0 (no tie) to 1.0 (perfect tie). A cut-off of 0.5-0.6 should filter unreliable mistie estimates.

### **Mistie Correction Calculation**
The ![Calculate Corrections](images/attributes.png) toolbar item in the [#Mistie Analysis] dialog opens the following dialog to compute mistie corrections that minimize the root mean square (RMS) mistie after correction:

{{ figure('mistie_correction.jpg', 'Mistie correction calculation') }}

The user can:

-  Optionally select one or more line(s) to use as a reference. Reference lines will have Z, phase and amplitude corrections constrained to be 0, 0, 1 respectively and corrections will be computed only for  the non-reference lines. Selecting no lines will distribute corrections across all lines.
-   Control the maximum number of iterations used to calculate the corrections - the default value should be adequate in most circumstances.
-   Control the convergence criteria that stops the iteration used to calulate the corrections - iterations stop if the change in the RMS mistie (after applying corrections) between successive iterations is less than the threshhold. Thresholds exist for the Z, phase and amplitude corrections. The default values should be adquate in most circumstances. 

The calculated corrections will be displayed in a new table dialog:

{{ figure('mistie_correction_viewer.jpg', 'Mistie correction viewer') }}

The toolbar buttons can be used to save the corrrections to a disk file.

### **Mistie Report**
The ![Mistie Report](images/xplot.png) toolbar item in the [#Mistie Analysis] dialog generates and displays in the system web browser a graphical, html format dashboard of the mistie anaysis and correction calculation results. This includes tabulated data, histograms and a 3D scatterplot. Here is an example of a [mistie report](images/mistie_report_example.html). The html file displayed in the browser can be saved for later display suing the browser's save page functionality. 

### **Mistie Correction Editor**
The plugin adds a "Mistie Corrections" item to the Survey-Manage main menu. Selecting the item opens the Mistie Correction Editor. This tool can be used to manually create mistie correction files or modify files generated by the [#Mistie Correction Calculation].

{{ figure('mistie_editor.jpg', 'Mistie correction editor') }}

The editor has toolbar buttons to:

{% set inputtable=[
['ICON','DESCRIPTION'],
['<img class="img-responsive" alt="New" src="images/new.png" title="New"/>','Create a mistie correction set with all the  2D lines in the project (with default corrections that make no change to the  data). Existing contents of the mistie table are erased.'],
['<img class="img-responsive" alt="Open" src="images/open.png" title="Open"/>','Load mistie corrections from a previously saved file. Existing contents of the mistie table are erased.'],
['<img class="img-responsive" alt="Save" src="images/save.png" title="Save"/>', 'Save the current mistie corrections. If the current corrections were loaded from a file then that will be overwritten, otherwise the user will be asked to provide a new file name.'],
['<img class="img-responsive" alt="SaveAs" src="images/saveas.png" title="SaveAs"/>', 'Prompts for a file and saves the current mistie corrections.'],
['<img class="img-responsive" alt="Merge" src="images/plus.png" title="Merge Corrections"/>', 'Merge another mistie correction set file with the current set, optionally keeping or replacing the existing corrections where there is duplicate line/dataset names.']]
%}
{{ table_with_hdr(inputtable,hdrstyle=['col-xs-2','col-xs-10'],style='table-striped table-bordered table-responsive') }}

Within the editor it is possible to:

- Add new lines/datasets and associated corrections
- Edit existing corrections
- RightMouseButton click on a row brings up a menu to insert or delete selected row(s)
- Limited clipboard copy and paste is available

You can include corrections for a particular 3D seismic volume by using a line/dataset name of the form "3D_XXXX" where the "XXXX" is the volume name, eg note the "3D_pstm" in the above figure. Multiple unique "3D_XXXX" entries are allowed to specify corrections for different 3D volumes in the project. 

If a line doesn't need a correction it can be omitted from the set and default (no change) corrections will be assumed when the Mistie Application attribute is applied. A message (which can be safely ignored) is added to the log file when this occurs. 

The name in the line/dataset column must exactly match the project line name.

### **Mistie Application Attribute**
The plugin adds a "Mistie Application" attribute to the list of [opendtect] attributes.

{{ figure('mistieapplication_input.jpg', 'Mistie Application attribute input parameters') }}

The attribute parameters include:

-  The input seismic volume to be corrected
-  A file with the mistie correction set to apply
-  Which corrections to apply 

When the attribute is displayed the shift, phase rotation and amplitude scalar for the line is read from the correction file and applied.

### **Mistie Correction of Horizon Interpretation**
The plugin adds an "Apply Mistie Corrections" item to the "Processing | Create Horizon Output" main menu that opens a dialog box to apply mistie corrections to 2D and 3D horizon interpretation.

{{ figure('mistie_horizon_2D_apply.jpg', 'Mistie Application to 2D Horizon') }}

{{ figure('mistie_horizon_3D_apply.jpg', 'Mistie Application to 3D Horizon') }}

### General Notes
-  The default file extension for saved mistie estimates is "mistie"
-  The default file extension for saved mistie corrections is "miscor"
-  The default file location for all files is the __Misc__ folder in the OpendTect survey/project folder
-  All files are in a simple text format which can also be modified using a text editor

