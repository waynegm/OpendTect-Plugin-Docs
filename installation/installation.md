---
title: Installation 
layout: page
---
{% from 'util.html' import figure %}
# Installation

**As of OpendTect 6.4.5 this suite of plugins can be installed using the OpendTect Installation Manager. Just activate the WMPlugins option in the installer.**

{{ figure('od_install_mgr.jpg', 'OpendTect Installation Manager') }}

This will install the wmPlugins into the OpendTect installation folder.

The following instructions are only needed for a manual intallation.

## Linux

### Sitewide Installation
To install the plugins into the OpendTect program folder (eg __/opt/seismic/OpendTect/6.4.0/ __):

1. Copy the contents of the __bin/lux64/Release/__ folder in the tgz file to __/opt/seismic/OpendTect/6.4.0/bin/lux64/Release/__;

2. Copy the contents of the __plugins/lux64/__ folder in the tgz file to __/opt/Seismic/OpendTect/6.4.0/plugins/lux64/__; and

3. Restart OpendTect.

### Per-user Installation

On Linux it is also possible to install the plugin files in a users __.od__ folder. Note that the OpendTect-6.4.0-plugins won't work in OpendTect 6.2.0 and the OpendTect-6.2.0-plugins won't work in OpendTect 6.4.0. See the [faq] for a workaround if you want a per-user installation and want to run multiple versions of OpendTect.

1. Copy the contents of the __bin/lux64/Release/__ folder in the tgz file to the users __.od/bin/lux64/Release/__ folder;

2. Copy the contents of the __plugins/lux64/__ folder in the tgz file to the users __.od/plugins/lux64/__ folder; and

3. Restart OpendTect.

## Windows

### Sitewide Installation
To install the plugins into the OpendTect program folder (eg __c:\Program Files\Opendtect\6.4.0 __):

1. Copy the contents of the __bin\win64\Release\ __ folder in the zip file to __c:\Program Files\Opendtect\6.4.0\bin\win64\Release\ __;

2. Copy the contents of the __plugins\win64\ __ folder in the zip file to __c:\Program Files\Opendtect\6.4.0\plugins\win64\ __; and

3. Restart OpendTect.

### Per-user Installation

On Windows it is also possible to install the plugin files in a users __.od__ folder. Note that the OpendTect-6.4.0-plugins won't work in OpendTect 6.2 and the OpendTect-6.2-plugins won't work in OpendTect 6.4. See the [faq] for a workaround if you want a per-user installation and want to run multiple versions of OpendTect.

1. Copy the contents of the __bin\win64\Release\ __ folder in the zip file to the users __C:\Users\%username%\\.od\bin\win64\Release\ __ folder;

2. Copy the contents of the __plugins\win64\ __ folder in the zip file to the users __C:\Users\%username%\\.od\plugins\win64\ __ folder; and

3. Restart OpendTect.
