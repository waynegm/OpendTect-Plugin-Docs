# OpendTect-Plugin-Docs
 
Documentation for the plugins I have developed for the open source seismic interpretation system <a href="http://www.opendtect.org/" target="_blank">OpendTect</a>. The plugins are made available under the terms of the [GNU General Public License Version 3](docs/license.txt).

To read the documentation click [here](http://waynegm.github.io/OpendTect-Plugin-Docs/).

To build the documentation:

  * [Urubu](http://urubu.jandecaluwe.com/) is required - install it in a python virtual environment
    * *virtualenv urubu*
    * *source urubu/bin/activate*
    * *pip install mardown==2.6.9*
    * *pip install urubu* 
  * cd to the documentation repo folder
  * Run *make* to build the documentation
  * Run *make serve*  to start a local web server to display the build results - point a browser at [localhost:8000](http://localhost:8000/) to see the result

