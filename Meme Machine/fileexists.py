import os.path,shutil,random
num = 1

while num < 100001:
    randomnum = random.randint(1,100000)
    current_file_exists = os.path.exists('/Storage/Meme_Folder/' + str(num))
    currentfile = '/Storage/Meme_Folder/' + str(num)
    random_file_exists = os.path.exists('/Storage/Meme_Folder/' + str(randomnum))    
    randomfile = '/Storage/Meme_Folder/' + str(randomnum)
    if random_file_exists == True:
      if current_file_exists == False:
        shutil.copy(randomfile,currentfile)
      print(current_file_exists,str(num))
      num = num + 1

