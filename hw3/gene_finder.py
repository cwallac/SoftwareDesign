# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 11:24:42 2014

@author: YOUR NAME HERE
"""

# you may find it useful to import these variables (although you are not required to use them)
from amino_acids import aa, codons
from random import shuffle
def collapse(L):
    """ Converts a list of strings to a string by concatenating all elements of the list """
    output = ""
    for s in L:
        output = output + s
    return output


def coding_strand_to_AA(dna):
    """ Computes the Protein encoded by a sequence of DNA.  This function
        does not check for start and stop codons (it assumes that the input
        DNA sequence represents an protein coding region).
        
        dna: a DNA sequence represented as a string
        returns: a string containing the sequence of amino acids encoded by the
                 the input DNA fragment
    """
    
    result = ''
    for j in range(0,len(dna),3):
        test = dna[j:j+3]
        
        for i in range(len(codons)):
            if test in codons[i]:
                result += aa[i]
                
    return result 
    # YOUR IMPLEMENTATION HERE

def coding_strand_to_AA_unit_tests():
    """ Unit tests for the coding_strand_to_AA function """
    res1 = coding_strand_to_AA('TTTTTT')
    res2 = coding_strand_to_AA('wqrewefds')
    
    return 'input: TTTTTT expected output: FF, actual output: ' + res1 + 'input: fsdfsdfsdg expected output: '', actual output: '+ res2
    # YOUR IMPLEMENTATION HERE

def get_reverse_complement(dna):
    """ Computes the reverse complementary sequence of DNA for the specfied DNA
        sequence
    
        dna: a DNA sequence represented as a string
        returns: the reverse complementary DNA sequence represented as a string
    """
    
    # YOUR IMPLEMENTATION HERE
    
    result = ''
    for i in dna[::-1]:
        if i == 'A':
            result += 'T'
        elif i == 'T':
            result += 'A'
        elif i == 'C':
            result += 'G'
        elif i == 'G':
            result += 'C'
    return result
    
def get_reverse_complement_unit_tests():
    """ Unit tests for the get_complement function """
    res = get_reverse_complement('ATCGATCG')
    print 'Input ATCGATCG Expected Output: CGATCGAT Output: ' + res
    # YOUR IMPLEMENTATION HERE    

def rest_of_ORF(dna):
    """ Takes a DNA sequence that is assumed to begin with a start codon and returns
        the sequence up to but not including the first in frame stop codon.  If there
        is no in frame stop codon, returns the whole string.
        
        dna: a DNA sequence
        returns: the open reading frame represented as a string
    """
    
    for i in range(0,len(dna),3):
        
        # a shorthand: if dna[i:i+3] in ['TAG', 'TAA', 'TGA']:
        if dna[i:i+3] == 'TAG' or dna[i:i+3] == 'TAA' or dna[i:i+3] == 'TGA':
            return dna[0:i]
        
    return dna
    # YOUR IMPLEMENTATION HERE

def rest_of_ORF_unit_tests():
    """ Unit tests for the rest_of_ORF function """
    res1 = rest_of_ORF("ATGTGAA")
    res2 = rest_of_ORF("ATGAGATAGG")
    print 'Input: ATGTGAA EXPECTED OUTPUT: ATG ACTUAL OUTPUT: ' + res1
    print 'Input: ATGAGATAGG EXPECTED OUTPUT: ATGAGA ACTUAL OUTPUT: ' + res2    
    # YOUR IMPLEMENTATION HERE
        
def find_all_ORFs_oneframe(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence and returns
        them as a list.  This function should only find ORFs that are in the default
        frame of the sequence (i.e. they start on indices that are multiples of 3).
        By non-nested we mean that if an ORF occurs entirely within
        another ORF, it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """
    
    results = []
    i = 0
    while i < len(dna):
        
        if dna[i:i+3] == 'ATG':
            frame = rest_of_ORF(dna[i::]) # no need to have the second colon if no `step` is required
            i += len(frame)-3
            results.append(frame)
        i += 3
    return results
        
        
                
    # YOUR IMPLEMENTATION HERE        
     
def find_all_ORFs_oneframe_unit_tests():
    """ Unit tests for the find_all_ORFs_oneframe function """
    res = find_all_ORFs_oneframe("ATGCATGAATGTAGATAGATGTGCCC")
    # YOUR IMPLEMENTATION HERE
    print "INPUT: ATGCATGAATGTAGATAGATGTGCCC EXPECTED OUTPUT:['ATGCATGAATGTAGA', 'ATGTGCCC'] ACTUAL OUTPUT: " + str(res)
def find_all_ORFs(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence in all 3
        possible frames and returns them as a list.  By non-nested we mean that if an
        ORF occurs entirely within another ORF and they are both in the same frame,
        it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """
    results = []
    for j in range(3):
         
         i = j
         while i < len(dna):
        
            if dna[i:i+3] == 'ATG':
                frame = rest_of_ORF(dna[i::])
                i += len(frame)-3
                results.append(frame)
            i += 3
    return results
    # YOUR IMPLEMENTATION HERE

'''
You could also do:

results = []

results.append(find_all_ORFs_oneframe(dna))
results.append(find_all_ORFs_oneframe(dna[1:]))
results.append(find_all_ORFs_oneframe(dna[2:]))

return results
'''

def find_all_ORFs_unit_tests():
    """ Unit tests for the find_all_ORFs function """
    res = find_all_ORFs("ATGCATGAATGTAG")
    print "INPUT: ATGCATGAATGTAG EXPECTED OUTPUT:['ATGCATGAATGTAG', 'ATGAATGTAG', 'ATG'] ACTUAL OUTPUT: " + str(res)
        
    # YOUR IMPLEMENTATION HERE

def find_all_ORFs_both_strands(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence on both
        strands.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """
    revres = find_all_ORFs(get_reverse_complement(dna))
    res = find_all_ORFs(dna)

    # shorthand: return res + revres
    for i in range(len(revres)):
        res.append(revres[i])
    return res
         
    # YOUR IMPLEMENTATION HERE

def find_all_ORFs_both_strands_unit_tests():
    """ Unit tests for the find_all_ORFs_both_strands function """

    # YOUR IMPLEMENTATION HERE
    res = find_all_ORFs_both_strands("ATGCGATAGCAT")
    
    print "INPUT: ATGCGATAGCAT EXPECTED OUTPUT:['ATGCGA', 'ATGCTATCGCAT'] ACTUAL OUTPUT: " + str(res)
    
def longest_ORF(dna):
    """ Finds the longest ORF on both strands of the specified DNA and returns it
        as a string"""

    # YOUR IMPLEMENTATION HERE
    longest = ''
    res = find_all_ORFs_both_strands(dna)
    for i in range(len(res)):
        if len(longest) < len(res[i]):
            longest = res[i]
    return longest
    
def longest_ORF_unit_tests():
    """ Unit tests for the longest_ORF function """

    # YOUR IMPLEMENTATION HERE
    res = longest_ORF("ATGTAGATGCAAAACTGA")
    
    print "INPUT: ATGTAGATGCAAAACTGA EXPECTED OUTPUT:ATGCAAAAC ACTUAL OUTPUT: " + str(res)
    
def longest_ORF_noncoding(dna, num_trials):
    """ Computes the maximum length of the longest ORF over num_trials shuffles
        of the specfied DNA sequence
        
        dna: a DNA sequence
        num_trials: the number of random shuffles
        returns: the maximum length longest ORF """

    # YOUR IMPLEMENTATION HERE
    longest = 0
    for i in range(num_trials):
        dna = list(dna)
        
        
        shuffle(dna)
        
        randstring = collapse(dna)
        res = len(longest_ORF(randstring))
        if res > longest:
            longest = res
    return longest

    
def gene_finder(dna, threshold):
    """ Returns the amino acid sequences coded by all genes that have an ORF
        larger than the specified threshold.
        
        dna: a DNA sequence
        threshold: the minimum length of the ORF for it to be considered a valid
                   gene.
        returns: a list of all amino acid sequences whose ORFs meet the minimum
                 length specified.
    """

    # YOUR IMPLEMENTATION HERE
    aminos = []
    frames = find_all_ORFs_both_strands(dna)
    for i in range(len(frames)):
        if len(frames[i]) > threshold:
            
            aminos.append(coding_strand_to_AA(frames[i]))
    return aminos
