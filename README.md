# PDB Query

# Software Description
This software was created to download PDB files, read their data and also query the contents of the PDB files.
It downloads the PDB files from the RCSB site and stores them in the current directory that you are working in.
Note, should you move the downloaded PDB file to another directory, the software will assume the PDB file is unavailable,
and download it again. The software can also retrieve a plethora of information from the PDB file:
the header, title, source, author, resolution and journal title of the PDB file, as well as the keywords of the PDB file.
In addition to that, it can create a file with the protein residues of a particular chain and/or a file with the relevant
lines of a specific chain. You will also get the opportunity to see the non-standard protein residues of a particular chain
(should they be present). It can alter the chain ID of a structure and save the edited file as a new file. Finally, it can plot
the temperature factors of a protein and return an image of the plot.

# Setting up the conda environment
In order for this software to work, the user must be operating on a conda environment that supports this software.
This software is upported by the py311 conda environment. If the user does not have this environment set up, follow the 
prompts below to set up the environment.
To create the py311 conda environment, input the following in your bash terminal:
`conda create -n py311 conda-forge python=3.11`
To verify if the conda environment was created, do the following in your bash terminal:
`conda env list`
To activate the py311 environment, do the following in your bash terminal:
`conda activate py311`

# Installing the requests module
The software makes use of a third-party library called `requests` which collects data from a given url and stores it in your
current directory. To make use of this module, the user will have to install it in their terminal. To install the module, you
can make use of the pip package by doing the following:
`pip install requests`
This comand will download the requests module and it will be ready to be imported by the user.
Alternatively, you can use conda to install the `requests` module:
`conda install requests`

# Insalling other third-party modules/libraries
This software makes use of matplotlib to create a plot for the temperature factors.
To install matplotlib, use the following command:
`pip install matplotlib`

# Getting the software from GitHub
To retrieve this software from GitHub and clone it on your local machine, the following actions need to be conducted:
If you have not already, download Git and install it onto your system. Git can be downloaded from the official Git website.
To clone the software, you will need to find the repository url of the software and copy it. You can find the repository url
by clicking "code" on GitHub.
Open your terminal and make use of the `git clone` command followed by the repository url to clone the repository.
From there, the repository will be cloned in your current working directory.

# How to run the script
Before running the script, it is vital to understand what the `checkPDB.py` script does. This script will continuosly ask
the user for inputs. These inputs will extract information and data from the PDB file of your choosing. The script will, in
some instances write to files.
The script can be run by using the following command `python checkPDB.py`.
The following command will execute the scripts using the python interpretor.
The user may also use an alternative route, which is to change the permissions of the file and make the script executable.
Use the `chmod +x checkPDB.py` command to make the scripts excecutable. To run the script, simply make
use of this command, `./checkPDB.py`
