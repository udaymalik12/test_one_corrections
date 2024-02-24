#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 20:35:09 2024

@author: udaymalik
"""

def count_unique_proteins(protein_lis):
    return len({protein.split('.')[0] for protein in protein_lis})

def count_proteins(protein_lis):
    unique_fam_freq_dic = {}
    for protein in protein_lis:
        protein_pf = protein.split(".")[0]
        unique_fam_freq_dic[protein_pf] = unique_fam_freq_dic.get(protein_pf, 0) + 1
    return unique_fam_freq_dic

def merge_protein_counts(dic_1, dic_2):
    combined_dic = {}
    set1 = set(dic_1.keys())
    set2 = set(dic_2.keys())
    for key in set1 | set2:
        dic_1_value = dic_1.get(key)
        dic_2_value = dic_2.get(key)
        combined_dic[key] = (dic_1_value, dic_2_value)
    return combined_dic
