import sys, math, decimal, glob, os, re

def main():
    files=[]
    os.chdir("files")
    for file in glob.glob("*.csv"):
        #print(file)
        files.append(file)
    files.sort()
    f2 = open('../output.txt', 'w')
    print "Filename - String - back(lookup) - front(lookup) - Correlation - no of rows"
    f2.write("Filename - String - back(lookup) - front(lookup) - Correlation - no of rows")
    for index in xrange(len(files)):
        #print "Results for file - ",files[index]
        #print "String - back(lookup) - front(lookup) - Correlation - no of rows"
        f=open(files[index],'r')
        line = f.readline().strip().split(',')
        data = {}
        #print line
        #print line[0],line[1],line[2]
        while len(line)>1:
            if line[0] not in data:
                data[line[0]]=[]
            inval=[]
            #print line
            #print line[0], line[1], line[2]
            inval.append(line[1])
            inval.append(line[2])
            #data[wrd]=[]
            data[line[0]].append(inval)
            line = f.readline().strip().split(',')
        f.close()
        sorted(data.items(), key = lambda k: (k))
        for ky in data:
            data[ky].sort(key = lambda k: k[0])
        #print data
        decimal.getcontext().prec=10

        for key in data:
            tot=len(data[key])
            for i in xrange(1,tot):
                for j in xrange(1,tot):
                    front=[]
                    back=[]
                    xy=0;x2=0;y2=0;x=0;y=0;n=tot-(i+j);n=0;
                    for loop in xrange(i,tot-j):
                        n+=1
                        #print int(data[key][loop][1])
                        bck=((float(data[key][loop][1])-float(data[key][loop-i][1]))/float(data[key][loop-i][1]))
                        frnt=((float(data[key][loop+j][1])-float(data[key][loop][1]))/float(data[key][loop][1]))
                        #print i,j,bck,frnt
                        x+=bck
                        y+=frnt
                        y2+=frnt*frnt
                        x2+=bck*bck
                        xy+=bck*frnt
                        #xy2+=(bck*frnt*bck*frnt)
                        #back.append(bck)
                        #front.append(frnt)
                    #print x,y,x2,y2,xy
                    #print n*x2,(x*x),n*y2,y*y
                    value=(n*x2 - (x*x))*(n*y2 - y*y)
                    #print value
                    denom=math.sqrt(float(value))
                    #print denom
                    if denom==0:
                        r=0
                        #continue
                    else: r=(n*(xy) - x*y)/denom
                    if i+j < tot:
                        print files[index],"\t  ",key,"\t\t  ",i,"\t\t  ",j,"\t\t  ","{0:.6f}".format(round(r,6)), "\t  ",n
                        if r<0:
                            f2.write("\n"+str(files[index])+"\t  "+str(key)+"\t\t\t  "+str(i)+"\t\t\t  "+str(j)+"\t\t\t   "+"{0:.6f}".format(round(r,6))+ "        "+str(n))
                        else:
                            f2.write("\n" + str(files[index]) + "\t  " + str(key) + "\t\t\t  " + str(i) + "\t\t\t  " + str(j) + "\t\t\t   " + "{0:.6f}".format(round(r, 6)) + "         " + str(n))


            #print key,len(data[key])



if __name__=="__main__":
    main()