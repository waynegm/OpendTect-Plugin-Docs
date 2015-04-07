# FAQ

## Building plugins that require Madagascar

To build plugins that use the Madagascar libraries (eg LTFAttrib) you need to set the RSFROOT environment variable before building the plugins.
```
	export RSFROOT=/opt/OpendTect_4/4.6.0/Madagascar
	cmake.
	make
```

## Plugins not loading

1. Try manually loading the plugin.

2. Check the OpendTect log file for error messages and see if there is already a solution outlined elsewhere in this page.

3. Open an <a href="https://github.com/waynegm/OpendTect-5-plugins/issues" target="_blank">issue</a> on GitHub.

## Per-user Installation and Multiple OpendTect versions

The OpendTect-4-plugins won't work in OpendTect 5+ and the OpendTect-5-plugins won't work in OpendTect 4. There are a couple of ways you can have access to plugins for both versions of OpendTect.

### Use the OD_USER_PLUGIN_DIR environment variable

This is the preferred option because it allows the same application settings files to be shared by both versions of OpendTect.
#### For Windows
1. Create *od5* and *od4* folders in the C:\Users\ *username* folder

2. Install the OpendTect-4-plugins in the *od4* folder and the OpendTect-5-plugins in the *od5* folder as per the [installation instructions](installation.md).

3. Create a "bat" file to start each version of OpendTect that sets the *OD_USER_PLUGIN_DIR* environment variable to the appropriate folder before starting OpendTect. Here is what odt_5.bat might look like:
```
@set OD_USER_PLUGIN_DIR=%HOMEPATH%\od5
start "" "C:\Program Files\OpendTect_5\5.0.0\bin\win64\Release\od_start_dtect.exe"
```

#### For Linux
1. Create *.od5* and *.od4* folders in the users home directory
```
	mkdir ~/.od5 
    mkdir ~/.od4
```

2. Install the OpendTect-4-plugins in the users *.od4* folder and the OpendTect-5-plugins in the *.od5* folder as per the [installation instructions](installation.md).

3. Create executable shell scripts to start each version of OpendTect that sets the *OD_USER_PLUGIN_DIR* to the appropriate folder before starting OpendTect. Here is what odt_5.csh might look like:
```
	#!/bin/csh -f
	setenv OD_USER_PLUGIN_DIR "$HOME/.od5"
	/path to OpendTect 5/start_dtect
```

### Have 2 user settings folders
#### For Windows
1. Copy the users existing *.od* folder to *.od5*

2. Install the OpendTect-4-plugins in the *.od* folder and the OpendTect-5-plugins in the *.od5* folder as per the [installation instructions](installation.md).

3. Create a "bat" file to start OpendTect 5  that sets the *DTECT_SETTINGS* environment variable to the appropriate folder before starting OpendTect. Here is what odt_5.bat might look like:
```
@set DTECT_SETTINGS=%HOMEPATH%\.od5
start "" "C:\Program Files\OpendTect_5\5.0.0\bin\win64\Release\od_start_dtect.exe"
```
#### For Linux
1. Copy the users existing *.od* folder to *.od5*

2. Install the OpendTect-4-plugins in the *.od* folder and the OpendTect-5-plugins in the *.od5* folder as per the [installation instructions](installation.md).

3. Create an executable shell script to start OpendTect 5 that sets the *DTECT_SETTINGS* environment variable to the appropriate folder before starting OpendTect. Here is what odt_5.csh might look like:
```
	#!/bin/csh -f
	
	setenv DTECT_SETTINGS "$HOME/.od5"
	/path to OpendTect 5/start_dtect
```

## libstdc++.so.6: version 'GLIBCXX_3.4.??' not found

This happens when the plugin is built with a gcc version different to the version used to build OpendTect. Solutions are: 

1. (Easy and seems to work ok but could break something) Rename the libstdc++.so.6 file in the OpendTect installation bin/lux64 folder to say old_libstdc++.so.6 and restart OpendTect.

2. (Hard) Install the same version of gcc that OpendTect was built with and rebuild the plugin.

3. (Hardest) Build OpendTect from source using your installed gcc.

