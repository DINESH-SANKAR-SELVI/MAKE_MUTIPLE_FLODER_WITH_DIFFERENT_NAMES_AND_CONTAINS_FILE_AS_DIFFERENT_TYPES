import csv
import shutil
import os
import csv

class fileName:
      global count 
      def __init__(self):  
            count = 0
            setData = []
            finalName = ""
            finalreg = []
            topicName = ["SIMPLE PROGRAMS","ARRAY","FUNCTIONS","POINTERS","STRUCTURES","FILE","SORTING & SEARCHING","STRING","SPARSE MATRIX","GRAPHICS","QUEUE","STACK","LINKED LIST","DOUBLELY LINKED LIST","TREE"]
            filename=['.py','.java','.cpp','.php','.xml']
            with open("E:\\PART_LOGIC_PROJECT\\QUIZES.csv",'r') as F :
                  read = csv.reader(F)
                  for getData in read:
                        setData.append(str(getData))
                        #print(getData)
            F.close()
            for firstMine in setData:
                  firstMine = firstMine[2:-1:1]
                  count=count+1
                  if count >0 and count<10 :
                        firstMine = firstMine[2:-1:1]
                  elif count>9 and count<100 :
                        firstMine = firstMine[3:-1:1]
                  elif count>99 and count<1000 :
                        firstMine = firstMine[4:-1:1]
                  else:
                        return NULL
                  for thirdMine in firstMine :
                        if (not(thirdMine=="\'") and not(thirdMine==",") and not(thirdMine=="-") and not(thirdMine=="&") and not(thirdMine==" ")):
                              finalName = finalName+thirdMine
                        else:
                              pass
                  #print(finalName)
                  new_abs_path = os.path.join("E:\\", "PART_LOGIC_PROJECT")
                  if (new_abs_path):
                        if count >0 and count<44 :
                              new_abs_path1 = os.path.join(new_abs_path, topicName[0])
                              if os.path.exists(new_abs_path1):
                                    os.mkdir(new_abs_path1+"\\"+finalName)
                                    print("FLODER CREATED...!",count,new_abs_path1,finalName)
                                    for fileType in filename:
                                          file1=new_abs_path1+"\\"+finalName+"\\"+finalName+fileType
                                          with open(file1,'w') as filety:
                                                filety.write("")
                                                filety.close()
                                                print(file1)
                        elif count >43 and count<64 :
                              new_abs_path1 = os.path.join(new_abs_path, topicName[1])
                              if os.path.exists(new_abs_path1):
                                    os.mkdir(new_abs_path1+"\\"+finalName)
                                    print("FLODER CREATED...!",count,new_abs_path1,finalName)
                                    for fileType in filename:
                                          file1=new_abs_path1+"\\"+finalName+"\\"+finalName+fileType
                                          with open(file1,'w') as filety:
                                                filety.write("")
                                                filety.close()
                                                print(file1)
                        elif count >63 and count<76 :
                              new_abs_path1 = os.path.join(new_abs_path, topicName[2])
                              if os.path.exists(new_abs_path1):
                                    os.mkdir(new_abs_path1+"\\"+finalName)
                                    print("FLODER CREATED...!",count,new_abs_path1,finalName)
                                    for fileType in filename:
                                          file1=new_abs_path1+"\\"+finalName+"\\"+finalName+fileType
                                          with open(file1,'w') as filety:
                                                filety.write("")
                                                filety.close()
                                                print(file1)
                        elif count >75 and count<84 :
                              new_abs_path1 = os.path.join(new_abs_path, topicName[3])
                              if os.path.exists(new_abs_path1):
                                    os.mkdir(new_abs_path1+"\\"+finalName)
                                    print("FLODER CREATED...!",count,new_abs_path1,finalName)
                                    for fileType in filename:
                                          file1=new_abs_path1+"\\"+finalName+"\\"+finalName+fileType
                                          with open(file1,'w') as filety:
                                                filety.write("")
                                                filety.close()
                                                print(file1)
                        elif count >83 and count<90 :
                              new_abs_path1 = os.path.join(new_abs_path, topicName[4])
                              if os.path.exists(new_abs_path1):
                                    os.mkdir(new_abs_path1+"\\"+finalName)
                                    print("FLODER CREATED...!",count,new_abs_path1,finalName)
                                    for fileType in filename:
                                          file1=new_abs_path1+"\\"+finalName+"\\"+finalName+fileType
                                          with open(file1,'w') as filety:
                                                filety.write("")
                                                filety.close()
                                                print(file1)
                        elif count >89 and count<98 :
                              new_abs_path1 = os.path.join(new_abs_path, topicName[5])
                              if os.path.exists(new_abs_path1):
                                    os.mkdir(new_abs_path1+"\\"+finalName)
                                    print("FLODER CREATED...!",count,new_abs_path1,finalName)
                                    for fileType in filename:
                                          file1=new_abs_path1+"\\"+finalName+"\\"+finalName+fileType
                                          with open(file1,'w') as filety:
                                                filety.write("")
                                                filety.close()
                                                print(file1)
                        elif count >97 and count<105 :
                              new_abs_path1 = os.path.join(new_abs_path, topicName[6])
                              if os.path.exists(new_abs_path1):
                                    os.mkdir(new_abs_path1+"\\"+finalName)
                                    print("FLODER CREATED...!",count,new_abs_path1,finalName)
                                    for fileType in filename:
                                          file1=new_abs_path1+"\\"+finalName+"\\"+finalName+fileType
                                          with open(file1,'w') as filety:
                                                filety.write("")
                                                filety.close()
                                                print(file1)
                        elif count >104 and count<123 :
                              new_abs_path1 = os.path.join(new_abs_path, topicName[7])
                              if os.path.exists(new_abs_path1):
                                    os.mkdir(new_abs_path1+"\\"+finalName)
                                    print("FLODER CREATED...!",count,new_abs_path1,finalName)
                                    for fileType in filename:
                                          file1=new_abs_path1+"\\"+finalName+"\\"+finalName+fileType
                                          with open(file1,'w') as filety:
                                                filety.write("")
                                                filety.close()
                                                print(file1)
                        elif count >122 and count<126 :
                              new_abs_path1 = os.path.join(new_abs_path, topicName[8])
                              if os.path.exists(new_abs_path1):
                                    os.mkdir(new_abs_path1+"\\"+finalName)
                                    print("FLODER CREATED...!",count,new_abs_path1,finalName)
                                    for fileType in filename:
                                          file1=new_abs_path1+"\\"+finalName+"\\"+finalName+fileType
                                          with open(file1,'w') as filety:
                                                filety.write("")
                                                filety.close()
                                                print(file1)
                        elif count >125 and count<139 :
                              new_abs_path1 = os.path.join(new_abs_path, topicName[9])
                              if os.path.exists(new_abs_path1):
                                    os.mkdir(new_abs_path1+"\\"+finalName)
                                    print("FLODER CREATED...!",count,new_abs_path1,finalName)
                                    for fileType in filename:
                                          file1=new_abs_path1+"\\"+finalName+"\\"+finalName+fileType
                                          with open(file1,'w') as filety:
                                                filety.write("")
                                                filety.close()
                                                print(file1)
                        elif count >138 and count<148 :
                              new_abs_path1 = os.path.join(new_abs_path, topicName[10])
                              if os.path.exists(new_abs_path1):
                                    os.mkdir(new_abs_path1+"\\"+finalName)
                                    print("FLODER CREATED...!",count,new_abs_path1,finalName)
                                    for fileType in filename:
                                          file1=new_abs_path1+"\\"+finalName+"\\"+finalName+fileType
                                          with open(file1,'w') as filety:
                                                filety.write("")
                                                filety.close()
                                                print(file1)
                        elif count >147 and count<156 :
                              new_abs_path1 = os.path.join(new_abs_path, topicName[11])
                              if os.path.exists(new_abs_path1):
                                    os.mkdir(new_abs_path1+"\\"+finalName)
                                    print("FLODER CREATED...!",count,new_abs_path1,finalName)
                                    for fileType in filename:
                                          file1=new_abs_path1+"\\"+finalName+"\\"+finalName+fileType
                                          with open(file1,'w') as filety:
                                                filety.write("")
                                                filety.close()
                                                print(file1)
                        elif count >155 and count<184 :
                              new_abs_path1 = os.path.join(new_abs_path, topicName[12])
                              if os.path.exists(new_abs_path1):
                                    os.mkdir(new_abs_path1+"\\"+finalName)
                                    print("FLODER CREATED...!",count,new_abs_path1,finalName)
                                    for fileType in filename:
                                          file1=new_abs_path1+"\\"+finalName+"\\"+finalName+fileType
                                          with open(file1,'w') as filety:
                                                filety.write("")
                                                filety.close()
                                                print(file1)
                        elif count >183 and count<188 :
                              new_abs_path1 = os.path.join(new_abs_path, topicName[13])
                              if os.path.exists(new_abs_path1):
                                    os.mkdir(new_abs_path1+"\\"+finalName)
                                    print("FLODER CREATED...!",count,new_abs_path1,finalName)
                                    for fileType in filename:
                                          file1=new_abs_path1+"\\"+finalName+"\\"+finalName+fileType
                                          with open(file1,'w') as filety:
                                                filety.write("")
                                                filety.close()
                                                print(file1)                                   
                        else:#elif count >187 and count<=195 :
                              new_abs_path1 = os.path.join(new_abs_path, topicName[14])
                              if os.path.exists(new_abs_path1):
                                    os.mkdir(new_abs_path1+"\\"+finalName)
                                    print("FLODER CREATED...!",count,new_abs_path1,finalName)
                                    for fileType in filename:
                                          file1=new_abs_path1+"\\"+finalName+"\\"+finalName+fileType
                                          with open(file1,'w') as filety:
                                                filety.write("")
                                                filety.close()
                                                print(file1)                                   
                        finalName=""
                  else:
                        print("FLODER NOT CREATED..!")
                        exit(1)     
fileName()