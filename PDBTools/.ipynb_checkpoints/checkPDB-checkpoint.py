#!/usr/bin/env python
from PDBTools import PDBTools
from PDBTools import pdblib
from pdblib.py import pdb_download

PDB_ID = input("Please input a PDB_ID of your choosing:")
PDB_ID = str(PDB_ID)

while True:
    # Exception handling for cases where the PDB_ID is not a string.
    try:
        if PDB_ID != str:
            raise TypeError("Error. PDB_ID has to be a string. Try again")
    except TypeError:
           print("Error. PDB_ID is not a string")
    
    # Exception handling for cases where PDB_ID is not given.
    try:
        if input is None:
            raise IndexError("Please input a PDB_ID")
    except IndexError:
           print("Error.No PDB_ID has been given. Try Again.")
    
    if PDB_ID == "q" or PDB_ID == "quit" or PDB_ID == "Q":
        break
    elif PDB_ID == "":
       download_pdb(PDB_ID)
       continue
    else:
        print("PDB_ID is invalid.Please try again with correct PDB_ID.")
