def enumerate_all_possibles_alignements (seq1, seq2, reward_match, cost_mismatch, cost_gap):
	
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
	
			
	return (liste_att)
		

def ali_optimaux(liste_att):
	#permet de trouver les alignements optimaux		
	liste_att=sorted(liste_att, key=lambda liste_att: liste_att[5])
	i=1
	p=-2
	liste_opti=[liste_att[-1]]
	while i>0:
		if liste_att[-1][5] == liste_att[p][5]:
			liste_opti.append(liste_att[p])
			p=p-1
		else:
			i=-1
	return liste_opti
		
print(enumerate_all_possibles_alignements("AAC","AG",1,-1,-1))
print("Il y a", len(enumerate_all_possibles_alignements("AAC","AG",1,-1,-1)), "resultats possibles")
print("Les alignements optimaux sont les suivants:", ali_optimaux(enumerate_all_possibles_alignements("AAC","AG",1,-1,-1)))


#print(enumerate_all_possibles_alignements("AGAC","ATTG",1,-1,-1))
#print("Il y a", len(enumerate_all_possibles_alignements("AGAC","ATTG",1,-1,-1)), "resultats possibles")


