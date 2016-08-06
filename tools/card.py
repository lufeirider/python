def fuzz(card,suffix):
    aW = [1,2,4,8,5,10,9,7,3,6,1,2,4,8,5,10,9,7]
    aA = ["1","0","X","9","8","7","6","5","4","3","2"]
    
    for a in range(1,10):
        for b in range(1,10):
            for c in range (1,10):
                aP = []
                aB = []
                iSum = 0
                cardTemp = card + str(a) + str(b) + str(c)

                for i in range(1,18):
                    aP.append(cardTemp[(17-i):(18-i)])
                
            
                for i in range(1,18):
                    aB.append(int(aP[i-1]) * int(aW[i]))
                    iSum += int(aB[i-1])
                
                if aA[iSum%11] in suffix:
                    print cardTemp+aA[iSum%11]
        
print fuzz("前14位","最后一位")
