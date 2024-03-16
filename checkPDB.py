#!/usr/bin/env python

import PDBTools.pdblib as module
import os

# Create a function that will print out the options from which the user can choose from.
def print_options():
    """ Functon prints out the options the user can choose from """
    print("Please read and decide what options you would like to choose")
    print("1  Getting the header")
    print("2  Getting the title")
    print("3  Getting the source")
    print("4  Getting the keywords")
    print("5  Getting the authors")
    print("6  Getting the resolution")
    print("7  Getting the Journal Title")

def print_chain_options():
    """ Function prints out the chain ID options the user can choose from """
    print("The following options are for chain ID selection.")
    print("A")
    print("B")
 
# First while loop is for the PDB_ID. It will be used for the subsequent functions in the script.
while True:
    PDB_ID = input ("Please input a PDB_ID:")
    # If user inputs the following, the loop will break.
    if PDB_ID == "q" or PDB_ID == "quit" or PDB_ID == "Q":
        break
    # User must only input a PDB_ID with upper case.
    if not PDB_ID.isupper():
        print("Error.Please use uppercase for all characters.")
        continue
    # Download the PDB file that is given to the input.
    try:
        if not PDB_ID:
            raise ValueError("No PDB_ID has been given. Try Again.")
        # Fetch the function using the pdblib.py module.
        module.pdb_download(PDB_ID)
    except ValueError:
        print("Error. No PDB_ID has been given.")
        # For loop will continue to run until PDB_ID is given.
        continue

    # Second while loop that is under first while loop. This while loop is for the options the user can choose from.
    while True:
        print_options()

        # User will input their option choice from the printed list.
        option = input("Please choose an option you would like to display:")
        # Loop will break.
        if option == "q" or option == "Q" or option == "quit":
            break
        if not option.isnumeric():
            print("Error. Option has to be numeric")
            continue
        # Adding a try-exception block in order to catch errors.
        try:
            # This is what will be printed out depending on the user's option.
            if option == "1":
                header =module.get_HEADER(PDB_ID)
                print(header)
            elif option == "2":
                title =module.get_TITLE(PDB_ID)
                print(title)
            elif option == "3":
                source = module.get_SOURCE(PDB_ID)
                print(source)
            elif option == "4":
                keywords = module.get_KEYWORDS(PDB_ID)
                print(keywords)
            elif option == "5":
                authors = module.get_AUTHOR(PDB_ID)
                print(authors)
            elif option == "6":
                resolution = module.get_RESOLUTION(PDB_ID)
                print(resolution)
            elif option == "7":
                journal_title = module.get_JRNL_TITL(PDB_ID)
                print(journal_title)
            else:
                print("Error: Option chosen is not available")
        except ValueError:
            print("Error. Please input a valid, numerical option")
            # For loop will continue to run until option is given
            continue

    while True:
        print_chain_options()
        
        #User will input the chain they would want to retrieve protein residues for.
        print("The following prompts will allow to read the protein residues of a chain ID, and save them to an output_filename")
        chain = input("To print the protein residues of a particular chain for the PDB_ID, please input a chain ID from the given options:")
        output_filename = input("Type 'output_filename' to name your file:")
        # Loop will break.
        if chain == "q" or chain == "quit" or chain == "Q":
            break
        elif not chain.isalpha() or not chain.isupper():
            print("Error. Input has to be single uppercase letter")
            continue
        if output_filename == "q" or output_filename == "Q" or output_filename == "quit":
            break
        # Adding a try-exception block here.
        try:
            # This is what will be printed out.
            if chain == "A" or chain == "B":
                residues = module.protein_residues(PDB_ID, chain)
                result = module.fasta_file(PDB_ID,chain,output_filename)
                if residues:
                    print(residues)
                    print("Residues have been written to your file")
                else:
                    print("Error.Protein residues for chain {} are not available".format(chain))
            else:
                print("Error. Given input is invalid. Please refer to the option list.")
        except ValueError:
            print("Error. Please input a valid chain ID/output_filename")


    while True:
        # User will input the chain ID they want.
        chain = input("To retreive the relevant lines of the PDB file, please firstly provide a chain ID of your choice:")
        if chain == "q" or chain == "Q" or chain == "quit":
            break
        elif not chain.isalpha() or not chain.isupper():
            print("Error.Chain_ID has to be in uppercase")
        record_type = input("Secondly, please provide the record type (ATOM or HETATM):")
        # Loop will break
        if record_type == "q" or record_type == "Q" or record_type == "quit":
            break
        if not record_type.isalpha() or not record_type.isupper():
            print("Error.Record_type has to be in uppercase.")
        # This is where the user will specify if they want to print the lines or write them to a file.
        output = input("What would you like to do with the lines? Write them to a file (W) or read them (R)?")
        if not output.isupper() or not output.isalpha():
            print("Error.Output has to a single uppercase letter")
            continue
        if output == "R":
            if chain in ["A","B"] and record_type in ["ATOM","HETATM"]:
                    lines = module.relevant_lines(PDB_ID, chain, record_type)
                    if lines:
                        print(lines)
                    else:
                        print("Error. Relevant lines not available for chain {}".format(chain))
            else:
                print("Error.Please provide a chain ID and/or record type")
        elif output == "W":
                    if chain in ["A","B"] and record_type in ["ATOM","HETATM"]:
                        lines = module.relevant_lines(PDB_ID, chain, record_type)
                        if lines:
                            with open(f"Relevant lines for {PDB_ID}_{chain}_{record_type}", "w") as fobject:
                                    fobject.write(lines)
                            print("Lines have been written to file")
                        else:
                            print("Error. Relevant lines for chain {} not available. No lines written to file.".format(chain))
        
                    else:
                        print("Error. Please input a chain ID (A or B) and a record_type (ATOM or HETATM)")
        else:
            print("Error.Please input correct output (W or R)")
            continue

    while True:
        # Ask user to input chain of their choice in order to get the non-standard protein residues.
        chain = input("To retreive the non-standard protein residues of a particular chain, please input a chain ID:")
        if chain == "q" or chain == "Q" or chain == "quit":
            break
        if not chain.isalpha():
            print("Error.Chain_ID has to be in uppercase")
            continue
        try:
            
            if chain in ["A","B"]:
                    non_standard_residues = module.non_standard_residues(PDB_ID, chain)
                    if non_standard_residues:
                        print(non_standard_residues)

                    else:
                        print("Error.Non_standard_residues for chain {} not available".format(chain))
        except ValueError:
            print("Error.Please input correct chain ID (A or B)")

    while True:
        try:
            print("The following prompts will allow you to change the chain ID of the structure you have downloaded")
            # Ask user for the following inputs: input_filename, output_filename, chain and new_chain.
            input_file = input("Please input the name of the pdb_file you have downloaded:")
            output_file = input("Please input the name you want to give to the output file:")
            chain = input("What chain are you wanting to alter:")
            if not chain.isalpha():
                print("Error. Chain_ID has to uppercase")
                continue
            new_chain = input("What do you want to rename the chain to?:")
            if not new_chain.isalpha():
                print("Error.new_chain needs to be uppercase")
            # Loop will break:
            if input_file == "Q" or input_file == "quit" or input_file == "q":
                break
            if output_file == "q" or output_file == "quit" or output_file == "Q":
                break
            if chain == "Q" or chain == "quit" or chain == "q":
                break
            if new_chain == "Q" or new_chain == "q" or new_chain == "quit":
                break
            # Utilizing the function:
            if chain in ["A", "B"]:
                alter_structure_chain = module.alter_chain_ID(input_file, output_file, chain, new_chain)
                # When file has been written to.
                print("output_file has been written into.")
            else:
                print("Error. Please make sure all inputs are valid and try again.")
        except ValueError:
            print("Error. Please make sure all inputs are valid")
        except FileNotFoundError:
            print("Error. File is not found")

    while True:
        try:
            print("The following prompts will allow you to get a plot of the temperature factors of a protein given a chain ID")
            # Ask the user for inputs.
            chain = input("Please input a chain ID:")
            if not chain.isalpha():
                print("Error.Chain_ID has to be uppercase")
                continue
            # Breaking the loop.
            if chain == "Q" or chain == "quit" or chain == "q":
                break
            # Ask the user for plot_dimensions
            plot_dimensions = input("Please put the dimensions you want the plot to have (Enclose them in round brackets):")
            # Breaking the loop
            if plot_dimensions == "Q" or plot_dimensions == "quit" or plot_dimensions == "q":
                break
            # Ask the user to name the output file.
            output_filename = input("Please enter 'output_filename'")
            if output_filename == "Q" or output_filename == "q" or output_filename == "quit":
                break
            # utilizing the function:
            temp_fact = module.temp_factor(PDB_ID, chain, plot_dimensions, output_filename)
            # User will have to save the plot on their own.
            print("Plot has been generated. Please save it")
        except ValueError:
            print("Error. Please ensure that your inputs are valid.")
