---
title: Frequently Asked Questions
layout: page 
pager: true
---
# FAQ
Can't find an answer here - then submit an issue on [Github](https://github.com/waynegm/OpendTect-Plugins/issues).

## Geopackage Export plugin isn't loading

The GeopackageExport plugin  requires access to external files (DLL's on Windows and lib*.so on Linux). These should have been included in the binary package for the plugins.

On Windows the folder containing the plugin and support DLL's must be added to the PATH environment variable. Do this by either:

- Editing/Adding the PATH environment variable for the System or User (Control Panel>System and Security>System - Advanced system settings - Environment Variables)
- Adding a line like "@set PATH=%HOMEPATH%.od\bin\win64\Release;%PATH%" (adjust "%HOMEPATH%.od\bin\win64\Release" to reflect your installation) to the bat script used to start OpendTect

## Plugins not loading

1. Try manually loading the plugin.

2. Check the OpendTect log file for error messages and see if there is already a solution outlined elsewhere in this page.


## Per-user Installation and Multiple OpendTect versions

The OpendTect-6.4-plugins won't work in OpendTect 6.2 and the OpendTect-6.2-plugins won't work in OpendTect 6.4. Here is a way to use the plugins with mutliple versions of OpendTect.

### Use the OD_USER_PLUGIN_DIR environment variable

#### For Windows
1.Create __ODPlugins\6.4.0__ and __ODPlugins\6.2.0__ folders in the __C:\Users\%username%__ folder

2.Install the OpendTect-6.2-plugins in the __6.2.0__ folder and the OpendTect-6.4-plugins in the __6.4.0__ folder as per the [installation] instructions.

3.Create a "bat" file to start each version of OpendTect that sets the __OD_USER_PLUGIN_DIR__ environment variable to the appropriate folder before starting OpendTect. Here is what odt_6_4.bat might look like:
```
@set OD_USER_PLUGIN_DIR=%HOMEPATH%\ODPlugins\6.4.0
start "" "C:\Program Files\OpendTect\6.4.0\bin\win64\Release\od_start_dtect.exe"
```

#### For Linux
1.Create __ODPlugins\6.4.0__ and __ODPlugins\6.2.0__ folders in the users home directory
```
	mkdir ~/ODPlugins
	mkdir ~/ODPlugins/6.4.0 
	mkdir ~/ODPlugins/6.2.0 
```

2.Install the OpendTect-6.4-plugins in the users __6.4.0__ folder and the OpendTect-6.2-plugins in the __6.2.0__ folder as per the [installation] instructions.

3.Create executable shell scripts to start each version of OpendTect that sets the __OD_USER_PLUGIN_DIR__ to the appropriate folder before starting OpendTect. Here is what odt_6_4.csh might look like:
```
	#!/bin/csh -f
	setenv OD_USER_PLUGIN_DIR "$HOME/ODPlugins/6.4.0"
	/path to OpendTect 6.4/start_dtect
```

## libstdc++.so.6: version 'GLIBCXX_3.4.??' not found

This happens when the plugin is built with a gcc version different to the version used to build OpendTect. Solutions are: 

1. (Easy and seems to work ok but could break something) Rename the libstdc++.so.6 file in the OpendTect installation bin/lux64 folder to say old_libstdc++.so.6 and restart OpendTect.

2. (Hard) Install the same version of gcc that OpendTect was built with and rebuild the plugin.

3. (Hardest) Build OpendTect from source using your installed gcc.

