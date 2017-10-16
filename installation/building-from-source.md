---
title: Building from Source
layout: page 
pager: true
---
# Building from Source

## Linux
These instructions are for Linux. Some of the attributes won't build (eg [LTFAttrib](../Attributes/LTFAttrib.md))unless Madagascar is installed.

1. Download the source for the plugins for the appropriate version of OpendTect from Github
   * [OpendTect v5+](https://github.com/waynegm/OpendTect-5-plugins/archive/master.zip)
   * [OpendTect v4](https://github.com/waynegm/OpendTect-4-plugins/archive/master.zip)

2. Use the OpendTect installation manager to install the OpendTect developer packages and install any other packages required for compiling and building code for your operating environment as per the <a href="http://www.opendtect.org/rel/doc/Programmer/" target="_blank">OpendTect Programmer's Manual</a>

3. Start OpendTect

4. Select the *Utilities-Tools-Create Plugin Devel. Env.* menu item to create a development work folder (eg /home/user/ODWork).

5. Unzip the attribute source zip archive downloaded in step 1 in the development work folder. This will overwrite the *CMakeLists.txt* in the development work folder and add the plugin source folders to the plugin folder.

6. Optionally edit *CMakeCache.txt* in the development work folder and change Debug to Release.

7. Optionally set the environment variable pointing to your Madagascar install
```
	export RSFROOT=/opt/OpendTect_4/4.6.0/Madagascar
```

8. Open a terminal, cd to the development work folder and type:
```
	cmake .
	make
```

9. This should create the binary files for each plugin, lib\*.so and libui\*.so, in the bin folder (eg in ODWork/bin/lux64/Release/) and four \*.alo files for each plugin in the root of the development work folder.

If you don't have Madagascar installed or RSFROOT is not set the plugins that depend on the Madagascar libraries (eg LTFAttrib) won't build and there will be error messages. These error messages can be ignored if you don't want the Madagascar dependent attributes.

## Windows
These instructions are for Windows. Note that the attributes that require Madagascar (eg [LTFAttrib](../Attributes/LTFAttrib.md)) cannot be built on Windows.

1. Download the source for the plugins for the appropriate version of OpendTect from Github
   * [OpendTect v5+](https://github.com/waynegm/OpendTect-5-plugins/archive/master.zip)
   * [OpendTect v4](https://github.com/waynegm/OpendTect-4-plugins/archive/master.zip)

2. Use the OpendTect installation manager to install the OpendTect developer packages and install any other packages required for compiling and building code for your operating environment as per the <a href="http://www.opendtect.org/rel/doc/Programmer/" target="_blank">OpendTect Programmer's Manual</a>

3. Start OpendTect

4. Select the *Utilities-Tools-Create Plugin Devel. Env.* menu item to create a development work folder (eg c:\Users\user\ODWork).

5. Unzip the attribute source zip archive downloaded in step 1 in the development work folder. This will overwrite the *CMakeLists.txt* in the development work folder and add the plugin source folders to the plugin folder.

6. Follow the instructions in the [OpendTect Programmer's Manual](http://opendtect.org/rel/doc/Programmer/windows.html) to configure and build the plugins.

7. This should create the binary files for each plugin in the bin folder (eg in ODWork\bin\win64\Release).

On Windows you must use "Release" build plugins with the "Release" version of OpendTect.
