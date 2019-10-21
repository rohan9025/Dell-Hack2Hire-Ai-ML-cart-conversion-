"""
    This is Recommendor#1. It gets the specifications of the
    laptops from the cart and checks the closest laptop in the
    dataset to recommend.

    Author: makflakes
"""

from pandas import read_csv

class similarity:
    def __init__(self, path_to_dataset):
        self.dataset = read_csv(path_to_dataset)
        self.dataset = self.dataset.values.tolist()

    def check_similarity(self, test_art : dict, num_close : int = None):
        count2 = 0
        recommendedlist = []
        test_artifact = [
            test_art['cpu'],
            test_art['gpu'],
            test_art['screen'],
            1,
            test_art['memory'],
            test_art['price']
        ]

        for i in self.dataset :
            for j in range (0,len(i)):
                
                if j==0:                                                 #processor
        
                    if (i[j]==test_artifact[0]):
                        
                        count2 = count2+10
                        
                    elif ( i[j]-(test_artifact[0])==2 or i[j]-(test_artifact[0])==-2):
                        count2 = count2+5
                    
                    else :
                        count2 = count2+1

               
                if j==1:                                                 #graphics
                    
                    if (i[j]==test_artifact[1]):
                        count2 = count2+10

                    elif ( -25<=i[j]-(test_artifact[1])<=25 ):
                        count2=count2+5
                    
                    else :
                        count2=count2+1
                    
                if j==2:                                                   #ScreenSize
                    
                    if (i[j]==test_artifact[2]):
                        count2 = count2+10

                    elif ( -2<=i[j]-(test_artifact[2])<=2 ):
                        count2=count2+5
                    
                    else :
                        count2=count2+1

                if j==3:                                                    #Color
                    
                    if (i[j]==test_artifact[3]):
                        count2 = count2+10

                    elif ( i[j]-(test_artifact[3])!=0 ):
                        count2=count2+0

                   
                if j==4:                                                    #RAM
                    if (i[j]==test_artifact[3]):
                        count2 = count2+10

                    if(i[j]>test_artifact[3]):
                        count2 = count2 + 5    

                    else :
                        count2 = count2 + 1                                           
                                    
                if j==5:                                                       #Price
                    #print (i[j])
                    #print (test_artifact[4])

                    
                    if (i[j]==test_artifact[4]):
                        count2 = count2+200
                    
                    elif ( (-4000<=(i[j]-test_artifact[4])<=4000)):
                        count2 = count2 + 160

                    elif ( (-8000<=(i[j]-test_artifact[4])<=-4000) or (4000<=(i[j]-test_artifact[4])<=8000)):
                        count2 = count2 + 130

                    elif (  (-12000<=(i[j]-test_artifact[4])<=-8000) or (8000<=(i[j]-test_artifact[4])>=12000)):
                        count2 = count2 + 100

                    else :
                        count2 = count2 + 0

                #print(i[j])

                if j==6:                                                        #Name
                    count2=count2+0

            recommendedlist.append(count2)
            count2=0

        if (num_close == None):
            num_close = 3

        N = num_close
        res = sorted(range(len(recommendedlist)), key = lambda sub: recommendedlist[sub])[-N:] 
        
        final_list = []

        for ind in res:
            final_list.append(self.dataset[ind])

        return final_list

if __name__ == '__main__':
    
    test_artifact = {
        'cpu' : 5,
        'gpu' : 0,
        'screen' : 15,
        'memory' : 8,
        'price' : 50000
    }

    similarity_obj = similarity()

    print (similarity_obj.check_similarity(test_artifact))