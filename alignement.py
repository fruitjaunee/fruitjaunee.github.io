# -*- coding: utf-8 -*-
""" Algorithm of brutal force alignment.

In order to find an optimal alignment between two sequences we define a score system: we determine a score when two caracters are identical, another when they are not and another when a caracter is aligned with a gap.
The final score of the aligment is the sum of all the scores.
The optimal alignment is the one that has the higher score of all the possible alignments. 

"""


import doctest

def enumerate_all_possibles_alignements (seq1, seq2, reward_match, cost_mismatch, cost_gap):
	"""Function to find all the possible alignements between two sequences.
	

	Args:
		seq1 (str): The first sequence to compare.
		seq2 (str): The second sequence to compare.
		reward_match (int) : Value given when there is a match between the two sequences.
		cost_mismatch (int) : Value given when there is a mismatch between the two sequences.
		cost_gap (int) : Value given when there is a gap in one of the sequences.

	Returns:
		final_list : A list containing all the possible alignments of the two sequences and their score.
	
	Example:
	>>> enumerate_all_possibles_alignements("AAC","AG",1,-1,-1)
	[['--AAC', 'AG---', -5], ['-A-AC', 'A-G--', -5], ['-AA-C', 'A--G-', -5], ['-AAC-', 'A---G', -5], ['-AAC', 'A--G', -4], ['-AAC', 'A-G-', -4], ['-AAC', 'AG--', -4], ['A--AC', '-AG--', -5], ['A-A-C', '-A-G-', -5], ['A-AC-', '-A--G', -5], ['A-AC', '-A-G', -4], ['A-AC', '-AG-', -4], ['AA--C', '--AG-', -5], ['AA-C-', '--A-G', -5], ['AA-C', '--AG', -4], ['AAC--', '---AG', -5], ['AAC-', '--AG', -4], ['AA-C', '-AG-', -2], ['AAC-', '-A-G', -2], ['AAC', '-AG', -1], ['A-AC', 'AG--', -2], ['AA-C', 'A-G-', -2], ['AAC-', 'A--G', -2], ['AAC', 'A-G', -1], ['AAC', 'AG-', -1]]

	"""
	
	if seq1[0] == seq2[0]:
		n=reward_match
	else:
		n=cost_mismatch
	
	liste_ali=[(1,seq1[0],seq2[0],1,1,n),(2,seq1[0],"-",1,0,cost_gap),(3,"-",seq2[0],0,1,cost_gap)]
	noeud_courant=[]
	liste_att=[]

	
		
	while len(liste_ali) != 0:
	
		noeud_courant=liste_ali.pop()
		
		
		op=noeud_courant[0]
		ch1=noeud_courant[1]
		ch2=noeud_courant[2]
		pos1=noeud_courant[3]
		pos2=noeud_courant[4]
		score=noeud_courant[5]
		
		
		if pos1==len(seq1) and pos2==len(seq2):
		#on ne peut plus creer de fils, donc c'est fini 
			liste_att.append(noeud_courant)
		
		
		elif pos1< len(seq1) and pos2< len(seq2):
		#on peut creer les trois fils car les trois options sont possibles
			if seq1[pos1] == seq2[pos2]:
				n= score +reward_match
			else:
				n= score +cost_mismatch
		
		
			fils1=(1,ch1+seq1[pos1],ch2+seq2[pos2],pos1+1,pos2+1,n)
			fils2=(2,ch1+seq1[pos1],ch2+"-",pos1+1,pos2,score+cost_gap)
			fils3=(3,ch1+"-",ch2+seq2[pos2],pos1,pos2+1,score+cost_gap)
		
		
			liste_ali.append(fils1)
			liste_ali.append(fils2)
			liste_ali.append(fils3)
		
		
		elif pos1==len(seq1) and pos2<len(seq2):
		#on ne peut creer que le fils 3
		
			fils3=(3,ch1+"-",ch2+seq2[pos2],pos1,pos2+1,score+cost_gap)
			liste_ali.append(fils3)
			
		elif pos1<len(seq1) and pos2==len(seq2):
		#on ne peut creer que le fils 2
		
			fils2=(2,ch1+seq1[pos1],ch2+"-",pos1+1,pos2,score+cost_gap)
			liste_ali.append(fils2)
	
	
	index=[1,2,5]
	final_list =[]
	for i in liste_att:
		ali=[]
		for j in index:
			ali.append(i[j])
		final_list.append(ali)
			
	return (final_list)
		

def ali_optimaux(liste_att):
	"""Function to find the optimal alignment between two sequences.


	Args:
		liste_att (list): List containing all the possible alignments of two sequences with their score.
		

	Returns:
		liste_opti : A list containing only the alignments with the higher score.
	
	Example:
	>>> ali_optimaux(enumerate_all_possibles_alignements("AAC","AG",1,-1,-1))
	[['AAC', 'AG-', -1], ['AAC', 'A-G', -1], ['AAC', '-AG', -1]]

	"""
	#permet de trouver les alignements optimaux		
	liste_att=sorted(liste_att, key=lambda liste_att: liste_att[2])
	i=1
	p=-2
	liste_opti=[liste_att[-1]]
	while i>0:
		if liste_att[-1][2] == liste_att[p][2]:
			liste_opti.append(liste_att[p])
			p=p-1
		else:
			i=-1
	return liste_opti
		

doctest.testmod(verbose =True)


