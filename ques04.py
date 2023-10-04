#!/usr/bin/env python3

# encoding: utf8
# author: Anam Ahsan

def convert_seq():
    while True:
        #Prompt input of new sequence from user while valid entries given
        oligo_seq = input("Enter an oligonucleotide sequence: ")
        #List of valid bases
        main_bases = ['A', 'C', 'G', 'T']
        #Dictionary of complement bases
        complements = {'A':'T', 'C': 'G', 'G': 'C', 'T': 'A'}
        #Empty list to store converted sequence
        new_seq = []
        #Iterate through eace base in input sequence
        for base in oligo_seq:
            #If base not in list, no more prompts, end program
            if base not in main_bases:
                print("Invalid character found in sequence.") 
                return False
            #If base in list add to new sequence list  
            else:
                new_seq.append(base)
        #Reverse list of bases  
        new_seq.reverse() 
        #Get complement of each base in list using complement dictionary
        new_seq = [complements[base] for base in new_seq]
        #Print reverse complement sequence as string 
        print("The reverse complement sequence is : " + ''.join(new_seq))

convert_seq() #Initiate function
