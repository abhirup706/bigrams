import sys

def bigramCount(file,add1Flag,sentence1,sentence2):
	tok_lst =[]
	tokCount = {}
	bigrams = {}
	bigramProb = {}
	bigramProb_sm = {}
	bigramCnt = {}
	sentprob = 0

	text = open(file,'r').read()


	tok_lst = text.strip().split()

	tok_lst_sent1 = sentence1.strip().split()

	tok_lst_sent2 = sentence2.strip().split()
	# for n in tok_lst:
	#	print (n)

   # find counts of each words to compute bigram probability

	for i in tok_lst:
   		if i in tokCount:
   			tokCount[i] += 1
   		else:
   			tokCount[i] = 1

	vocabCnt = 0
	for i in tokCount:
		vocabCnt = vocabCnt + tokCount[i]

	print ("\nTotal Vocabulary Count in Corpus: "+str(vocabCnt))

	for i in range(len(tok_lst)-1):
		temp = (tok_lst[i],tok_lst[i+1])

		if temp in bigrams:
			#print (temp)
			#print (bigrams[temp])
			bigrams[temp] += 1
		else:
			#print (temp)
			#print(bigrams[temp])
			bigrams[temp] = 1


	sent1Prob = 1
	print ("\n==================================== \n")
	print ("SENTENCE 1 PROBABILITIES AND BIGRAMS \n")
	print ("==================================== \n")

	print ("Sentence 1:" + sentence1 +"\n")
	if (add1Flag == 0):

		for i in range(len(tok_lst_sent1)-1):
			temp = (tok_lst_sent1[i],tok_lst_sent1[i+1])

			cnt_firstWord = tokCount[tok_lst_sent1[i]]

			bigramCnt[temp] = bigrams[temp]
			bigramProb[temp] = bigrams[temp]/cnt_firstWord

			sent1Prob = sent1Prob * bigramProb[temp]

		print ("\nSENTENCE 1 BIGRAM COUNTS IN CORPUS\n")
		for i in bigramCnt:
			print (str(i)+ ":"+str(bigramCnt[i]))

		print ("\nSENTENCE 1 BIGRAM PROBABILITIES IN CORPUS\n")
		for i in bigramProb:
			print (str(i)+ ":"+str(bigramProb[i]))

		print ("\nProbability of Sentence 1 without Add-1 Smoothing: "+str(sent1Prob))

	if (add1Flag == 1):

		for i in range(len(tok_lst_sent1)-1):
			temp = (tok_lst_sent1[i],tok_lst_sent1[i+1])

			cnt_firstWord = tokCount[tok_lst_sent1[i]]

			bigramCnt[temp] = bigrams[temp]
			bigramProb[temp] = (bigrams[temp]+1)/(cnt_firstWord+vocabCnt)

			sent1Prob = sent1Prob * bigramProb[temp]

		print ("\nSENTENCE 1 BIGRAM COUNTS IN CORPUS\n")
		for i in bigramCnt:
			print (str(i)+ ":"+str(bigramCnt[i]))
		
		print ("\nSENTENCE 1 BIGRAM PROBABILITIES IN CORPUS (WITH ADD-1 SMOOTHING)\n")

		for i in bigramProb:
			print (str(i)+ ":"+str(bigramProb[i]))


		print ("\nProbability of Sentence 1 with Add-1 Smoothing: "+str(sent1Prob))
	bigramCnt.clear()
	bigramProb.clear()
	print ("\n \n")
	#computing for sentence 2

	print ("==================================== \n")
	print ("SENTENCE 2 PROBABILITIES AND BIGRAMS \n")
	print ("==================================== \n")

	print ("Sentence 2:" + sentence2 +"\n")
	sent2Prob = 1
	if (add1Flag == 0):

		for i in range(len(tok_lst_sent2)-1):
			temp = (tok_lst_sent2[i],tok_lst_sent2[i+1])

			cnt_firstWord = tokCount[tok_lst_sent2[i]]

			bigramCnt[temp] = bigrams[temp]
			bigramProb[temp] = bigrams[temp]/cnt_firstWord

			sent2Prob = sent2Prob * bigramProb[temp]

		print ("\nSENTENCE 2 BIGRAM COUNTS IN CORPUS\n")
		for i in bigramCnt:
			print (str(i)+ ":"+str(bigramCnt[i]))

		print ("\nSENTENCE 2 BIGRAM PROBABILITIES IN CORPUS\n")
		for i in bigramProb:
			print (str(i)+ ":"+str(bigramProb[i]))

		print ("\nProbability of Sentence 2 without Add-1 Smoothing: "+str(sent2Prob))

	

	if (add1Flag == 1):

		for i in range(len(tok_lst_sent2)-1):
			temp = (tok_lst_sent2[i],tok_lst_sent2[i+1])

			cnt_firstWord = tokCount[tok_lst_sent2[i]]

			bigramCnt[temp] = bigrams[temp]
			bigramProb[temp] = (bigrams[temp]+1)/(cnt_firstWord+vocabCnt)

			sent2Prob = sent2Prob * bigramProb[temp]

		print ("\nSENTENCE 2 BIGRAM COUNT IN CORPUS\n")

		for i in bigramCnt:
			print (str(i)+ ":"+str(bigramCnt[i]))

		print ("\nSENTENCE 2 BIGRAM PROBABILITIES IN CORPUS (WITH ADD-1 SMOOTHING)\n")
		for i in bigramProb:
			print (str(i)+ ":"+str(bigramProb[i]))


		print ("\nProbability of Sentence 2 with Add-1 Smoothing: "+str(sent2Prob))




if len(sys.argv) != 3:
	print('Correct Usage is: py bigram.py <corpus file name> <add-one flag>')
	exit()

print ('File Name  : ' + sys.argv[1])
print ('Add-1 Flag : ' + sys.argv[2])



sent1= "mark antony , heere take you caesars body : you shall not come to them poet ."
sent2= "no , sir , there are no comets seen , the heauens speede thee in thine enterprize ."

bigramCount(sys.argv[1],int(sys.argv[2]),sent1,sent2)

#for i in sent1_bigram:
#	print (str(i) + " : " + str(sent1_bigram[i]))



