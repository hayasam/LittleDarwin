from scipy.stats.stats import pearsonr   
# from math import sqrt


corr = list()

for i in range(1,41):
    inputFileF = "fo-"+ str(3*i) + ".csv"
    inputFileS = "to-"+ str(i) + ".csv"
    


    with open(inputFileF, 'r') as iF:
        inF = iF.readlines()
    
    with open(inputFileS, 'r') as iS:
        inS = iS.readlines()
        
    fo = list()
    so = list()

    maxLength = len(inF)

    if len(inF) != len(inS):
        print "[WARN}", inputFileF, inputFileS, "not equal size.", len(inF), len(inS)
        if len(inS) > maxLength:
            assert False
            # maxLength = len(inS)

        # continue

    skipped = 0
    for i in range(0,maxLength):
        inFs = inF[i].split(',')
        inSs = inS[i-skipped].split(',')

        if inFs[0] != inSs[0]:
            skipped += 1
            print inFs[0], "not found."
            continue


        fop = (float(inFs[2])/float(inFs[3]))

        fo.append( fop*3 - 3*(fop**2) + fop**3)
        so.append(float(inSs[2])/float(inSs[3]))
    
    # print (fo,so)
    
    r,p = pearsonr(fo, so)
    corr.append(str(r**2)+"\n")

with open("corr3.csv", 'w') as corrF:
    corrF.writelines(corr)
