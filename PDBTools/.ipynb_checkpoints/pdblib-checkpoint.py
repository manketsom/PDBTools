#!/usr/bin/env python

import requests
import os
from matplotlib import pyplot as plt

def pdb_download(PDB_ID):
    """ Function downloads a PDB file only if it unavailable locally """
    # Create a variable that stores the filename of a given PDB ID.
    PDB_file_name = PDB_ID + ".pdb"
    # This will prevent unnecessary downloading.
    if os.path.exists(PDB_file_name):
        print("The file {} is available locally, and will not be downloaded.".format(PDB_file_name))
    # Create an url that will allow any PDB file to be downloaded
    url = "https://files.rcsb.org/download/"+ PDB_ID + ".pdb"
    # Request for the file and get a response.
    response = requests.get(url)
    # Open a file for writing the text.
    with open(f"{PDB_ID}", "w") as fobject:
        fobject.write(response.text)
        print("The file {} will be downloaded".format(PDB_file_name))

def get_HEADER(PDB_ID):
    """ Function retrieves the header from a specified PDB file """
    # Url to download your desired pdb file
    pdb_url = "https://files.rcsb.org/download/" + PDB_ID + ".pdb"
    # Request to get the file and get the response.
    response = requests.get(pdb_url)
    # Use the split method to convert the retrieved string into a list of lines.
    lines = response.text.split("\n")
    # Get the details.
    for line in lines:
        if line.startswith("HEADER"):
            header = line[10:68]
            print(header)
        return header

def get_TITLE(PDB_ID):
    """ Function prints the title from a specified PDB file """
    # Url to download your desired pdb file
    pdb_url = "https://files.rcsb.org/download/" + PDB_ID + ".pdb"
    # Request to get the file and get the response.
    response = requests.get(pdb_url)
    # Use the split method to convert the retrieved string into a list of lines.
    lines = response.text.split("\n")
    # Make an empty string where title characters will be stored.
    title = ""
    for line in lines:
        if line.startswith("TITLE"):
            # title string will be concatenated to the characters in line[10:].
            title += line[10:].strip()
            # Create an empty list where the wrapped lines will be stored.
            wrap_lines = []
            # Ensuring that the line is not longer than 80 characters.
            for i in range(0,len(title),80):
                # Make use of splicing to get to ensure that there is only 80 characters in a line.
                wrap_lines.append(title[i:i+80])
    # All entries separated by a semi-colon must be on a single line.
    Title = ";".join(wrap_lines)
    print(Title)
    return Title

def get_SOURCE(PDB_ID):
    """ Function prints the source from a specified PDB file """
    # Url to download your desired pdb file
    pdb_url = "https://files.rcsb.org/download/" + PDB_ID + ".pdb"
    # Request to get the file and get the response.
    response = requests.get(pdb_url)
    # Use the split method to convert the retrieved string into a list of lines.
    lines = response.text.split("\n")
    # Getting the source.
    source = ""
    for line in lines:
        if line.startswith("SOURCE"):
            # Isolate the lines you want.
            source += line[10:].strip()
            # Make an empty list that will store all the wrapped information for 'SOURCE'.
    wrap_source = []
            # Ensuring that the line is not longer than 80 characters. Make use of splicing too.
    for i in range(0,len(source),80):
        wrap_source.append(source[i:i+80])

    Source = ";".join(wrap_source)
    print(Source)
    return Source

def get_JRNL_TITL(PDB_ID):
    """ Function prints the Journal title from a specified PDB file """
    # Url to download your desired pdb file
    pdb_url = "https://files.rcsb.org/download/" + PDB_ID + ".pdb"
    # Request to get the file and get the response.
    response = requests.get(pdb_url)
    # Use the split method to convert the retrieved string into a list of lines.
    lines = response.text.split("\n")
    # Getting the source.
    journal_title = ""
    for line in lines:
        if line.startswith("JRNL        TITL"):
            journal_title += line[19:].strip()
            # Make an empty list that will store all the wrapped information for 'SOURCE'.
    journal_title_wrap = []
            # Ensuring that the line is not longer than 80 characters. Make use of splicing too.
    for i in range(0,len(journal_title),80):
        journal_title_wrap.append(journal_title[i:i+80])

    JRNL_T = ";".join(journal_title_wrap)
    print(JRNL_T)
    return JRNL_T

def get_KEYWORDS(PDB_ID):
    """ Function prints the keywords from a specified PDB file """
    # Url to download your desired pdb file
    pdb_url = "https://files.rcsb.org/download/" + PDB_ID + ".pdb"
    # Request to get the file and get the response.
    response = requests.get(pdb_url)
    # Use the split method to convert the retrieved string into a list of lines.
    lines = response.text.split("\n")
    # Getting the keywords.
    for line in lines:
        if line.startswith("KEYWDS"):
            keywords = line[10:66]
            print(keywords)
            return keywords

def get_AUTHOR(PDB_ID):
    """ Function prints the author of a journal that has been referenced in the pdb file """
    # Url to download your desired pdb file
    pdb_url = "https://files.rcsb.org/download/" + PDB_ID + ".pdb"
    # Request to get the file and get the response.
    response = requests.get(pdb_url)
    # Use the split method to convert the retrieved string into a list of lines.
    lines = response.text.split("\n")
    # Getting the author.
    for line in lines:
        if line.startswith("AUTHOR"):
            author = line[10:31]
            print(author)
            return author

def get_RESOLUTION(PDB_ID):
    """ Function retrieves the resolution from a specified PDB file """
    # Url to download your desired pdb file
    pdb_url = "https://files.rcsb.org/download/" + PDB_ID + ".pdb"
    # Request to get the file and get the response.
    response = requests.get(pdb_url)
    # Use the split method to convert the retrieved string into a list of lines.
    lines = response.text.split("\n")
    # Getting the resolution.
    for line in lines:
        if line.startswith("REMARK   2 RESOLUTION."):
            resolution = line[26:41]
            print(resolution)
            return resolution

def protein_residues(PDB_ID, chain):
    """ Function prints out the single-letter protein residues of either Chain A or
        Chain B"""
    # Url to download your desired pdb file
    pdb_url = "https://files.rcsb.org/download/" + PDB_ID + ".pdb"
    # Request to get the file and get the response.
    response = requests.get(pdb_url)
    # Use the split method to convert the retrieved string into a list of lines.
    lines = response.text.split("\n")
    # Create a dictionary with key(three-letter residue) and value(one-letter residue):
    aa_residues = {"ALA": "A", "ARG":"R", "ASP":"D", "ASN":"N", "CYS":"C", "GLU": "E", "GLN":"Q", "GLY":"G", "HIS":"H", "ILE":"I",
             "LEU": "L", "LYS": "K", "MET": "M", "PHE":"F", "PRO":"P", "SER":"S", "THR":"T", "TRP":"W", "TYR":"Y", "VAL":"V"}
    # Create an empty string for the residues that will be printed on a single line.
    residues = ""
    # Isolating the lines starting with "ATOM" and "CA" and "chain"
    for line in lines:
        if line.startswith("ATOM") and line[13:15] == "CA" and line[21:22] == chain:
            three_letter_code = line[17:20]
            # Use the dictionary method 'get' to get the one-letter codes.
            single_letter_code = aa_residues.get(three_letter_code)
            # Append the 'residues' string to the one-letter code
            residues += single_letter_code
    print(residues)
    return residues

def fasta_file(chain, output_filename):
    """ Function takes chain and output_filename as inputs and generates a FASTA-formatted file.
        If no chain is given, it saves each chain as an entry in a single fasta file. Function requires
        you to specify a PDB_ID before calling the function."""
    # Need to retreive the residues that will make the sequence that is to be written in the fasta file.
    sequence = protein_residues(PDB_ID, chain)
    # Need to generate the header for the definition line using the get_HEADER function.
    header = get_HEADER(PDB_ID)
    with open(f"{PDB_ID}.Fasta {chain}", "w") as fobject:
        fobject.write("{} {}\n{}".format(header, chain, sequence))
    if chain is None:
        # Create an empty string where both sequences for the chains will be stored.
        both_chains = ""
        # Create a list with both chains
        chains = ["A","B"]
        for chain in chains:
            sequence = protein_residues(PDB_ID, chain)
            both_chains = both_chains + ("{} {}\n{}\n".format(header,chain,sequence))
            with open(f"{PDB_ID}.Fasta", "w") as fobject:
                fobject.write(both_chains)

def relevant_lines(chain, type):
    """ Function writes the relevant lines to a file with given inputs of chain ID
         and a HETATM/ATOM record type. Function requires you to input a PDB_ID before
         calling the function """
    # Url to retrieve your desired pdb file
    pdb_url = "https://files.rcsb.org/download/" + PDB_ID + ".pdb"
    # Request to get the file and get the response.
    response = requests.get(pdb_url)
    # Use the split method to convert the retrieved string into a list of lines.
    lines = response.text.split("\n")
    # Create a condition that will allow the type argument to be given a value and return a set of lines.
    if type == "ATOM":
        pattern = "ATOM"
    elif type == "HETATM":
        pattern = "HETATM"
    # Create a condition that will rename the filename according to the record type.
    if type == "ATOM":
        pdb_file = "ATOM.pdb"
    elif type == "HETATM":
        pdb_file = "HETATM.pdb"
        # Create an empty list where all the relevant lines will be stored.
        relevant_lines = []
        for line in lines:
            if line.startswith(pattern) and line[21:22] == chain:
                relevant_lines.append(line)
        return relevant_lines

def non_standard_residues(PDB_ID, chain):
    """ Function takes as input a PDB_ID and a chain and returns a printed
        list of non-standard protein residues"""
    # Url to retrieve your desired pdb file
    url = "https://files.rcsb.org/download/" + PDB_ID + ".pdb"
    # Request to get the file and get the response.
    response = requests.get(url)
    # Use the split method to convert the retrieved string into a list of lines.
    lines = response.text.split("\n")
    # Make an empty list where all the residues will be stored.
    prot_residues = ""
    # Get the non-standard protein residues
    for line in lines:
        if line.startswith("HETATM") and line[13:15] == "CA" and line[21:22] == chain:
            residues = line[17:20]
            prot_residues+= residues
    print(prot_residues)

def alter_chain_ID(input_file, output_file, chain, new_chain):
    """ Function takes as inputs an input and output_file, a chain
        and a new chain. It alters a chain ID of the ATOM and HETATM structures and saves the file."""
    # Open the pdbfile you have downloaded for reading.
    with open(input_file, "r") as fobject:
        # These lines will be used to alter the chain ID
        input_lines = fobject.readlines()

    # Open a file to which the altered chain IDs will be written.
    with open(output_file, "w") as fobject:
        for line in input_lines:
        # Structures we are altering are ATOM and HETATM.
            if line.startswith("ATOM") or line.startswith("HETATM"):
                # Where the old chain is found.
                if line[21:22] == chain:
                    # Creating a line that has the altered chain.
                    line = line[:21] + new_chain +line[22:]
            fobject.write(line)


def temp_factor(chain_ID, plot_dimensions, output_filename):
    """ Function takes as input a chain ID, plot dimensions and an output_filename,
        and plots the temperature factor of that specific chain"""
    # Input pdb id here.
    PDB_ID = ""
    # Url to retrieve your desired pdb file
    url = "https://files.rcsb.org/download/" + PDB_ID + ".pdb"
    # Request to get the file and get the response.
    response = requests.get(url)
    # Use the split method to convert the retrieved string into a list of lines.
    lines = response.text.split("\n")
    # Create an empty list where the temperature factors will be stored.
    temp_factors = []
    for line in lines:
        # "ATOM" is the protein.
        if line.startswith("ATOM") and line[13:15] == "CA" and line[21:22] == chain_ID:
            # Concvert the strings into a float type.
            factors = float(line[61:66])
            temp_factors.append(factors)

    # Make the temperature plot
    plt.figure(plot_dimensions)
    plt.plot(temp_factors, color="green")
    plt.xlabel("ATOM indexing")
    plt.ylabel("Temperature Factor")
    plt.title("Plot Of The Temperature Factors for Chain {}". format(chain_ID))
    # Save the plot to an output_filename:
    plt.savefig(output_filename)
