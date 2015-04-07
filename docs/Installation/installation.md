# Installation

For both Linux and Windows there are 2 alternatives, site wide installation or per-user installation.

## Linux

### Sitewide Installation

1. Copy the lib\*.so and libui\*.so files for the plugins of interest to you into the appropriate platform sub folder in the OpendTect installation bin folder for the appropriate OpendTect version (eg copy to /opt/seismic/OpendTect/5.0/bin/lux64/Release).

2. Copy the \*.alo files for the plugins of interest to you into the appropriate platform sub folder in the OpendTect installation bin folder for the appropriate OpendTect version (eg copy to /opt/seismic/OpendTect/5.0/bin/lux64/Release).

3. Restart OpendTect.

### Per-user Installation

On Linux it is also possible to install the plugin files in a users *.od* folder. Note that the OpendTect-4-plugins won't work in OpendTect 5+ and the OpendTect-5-plugins won't work in OpendTect 4. See the [FAQ](faq.md) for a workaround if you want to use this method of installation and want to run both versions of OpendTect.

1. Copy the lib\*.so and libui\*.so files for the plugins of interest to you into the appropriate platform sub folder in the users ~/.od/bin folder (eg copy to /home/user/.od/bin/lux64/Release).

2. Copy the \*.alo files for the plugins of interest to you into the appropriate platform sub folder in the users ~/.od/plugins folder (eg copy to /home/user/.od/plugins/lux64).

3. Restart OpendTect.

## Windows

### Sitewide Installation

1. Copy all the files in bin/win64/Release to the appropriate platform sub folder in the OpendTect installation bin folder for the appropriate OpendTect version (eg copy to c:\Program Files\OpendTect\4.6.0\bin\win64\Release).

2. Restart OpendTect.

### Per-user Installation

On Windows it is also possible to install the plugin files in a users *.od* folder. Note that the OpendTect-4-plugins won't work in OpendTect 5+ and the OpendTect-5-plugins won't work in OpendTect 4. See the [FAQ](faq.md) for a workaround if you want to use this method of installation and want to run both versions of OpendTect.

1. Copy the files in the "bin\win64\Release" either from the build folder or the binary distribution zip file into the users "C:\Users\%username%\\.od\bin\win64\Release" folder.

2. Copy the \*.alo files for the plugins from the build folder or the "plugin\win64" folder of the binary distribution zip file into the users "C:\Users\%username%\\.od\plugin\win64" folder.

3. Restart OpendTect.