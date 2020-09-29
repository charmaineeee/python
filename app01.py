print("Title of program: MCQ revision program")
print()

counter = 0
score = 0
total_num_of_qn = 3


counter +=1
tracker = 0

while tracker !=1:
  
  print("Q"+str(counter)+") "+ "What is 100÷2(16+9)+613-614+1230?")
  print("   a) 1240")
  print("   b) 1232")
  print("   c) 1233")
  print("   d) 1128")
  answer = input("Your answer: ")
  answer = answer.lower()
  if answer == "a":
    output = "You're wrong"
    score -=1
  elif answer == "b":
    output = "Try again"
    score -=1
  elif answer == "c":
    output = "Congratulations"
    tracker =1
    score +=1
  elif answer == "d":
    output = "Use your calculator"
    score -=1
  else:
    output = "Please choose a, b, c or d only."
  
  print()
  print(output)
  print()
  print("Your current score: " + str(round((score/total_num_of_qn*100),1)) + "%"  )
  print()
  print()
  


counter +=1
tracker = 0

while tracker !=1:
  
  print("Q"+str(counter)+") "+ "How many atoms are there in the chemical formula C169,719H270,466N45,688O52,238S911")
  print("   a) 539022")
  print("   b) 236843")
  print("   c) 539023")
  print("   d) 432683")
  answer = input("Your answer: ")
  answer = answer.lower()
  if answer == "a":
    output = "yes congratulations you have passed your mathematics and eyesight test"
    tracker =1
    score +=1
  elif answer == "b":
    output = "nope"
    score -=1
  elif answer == "c":
    output = "sorry nope"
    score -=1
    
  elif answer == "d":
    output = "check again"
    score -=1
  else:
    output = "Please choose a, b, c or d only."

  print()
  print(output)
  print()
  print("Your current score: " + str(round((score/total_num_of_qn*100),1)) + "%"  )
  print()
  print()
  
  

counter +=1
tracker = 0

while tracker !=1:
  
  print("Q"+str(counter)+") "+ "How many elements are there in Zn(NO3)2?")
  print("   a) 4")
  print("   b) 7")
  print("   c) 2")
  print("   d) 3")
  answer = input("Your answer: ")
  answer = answer.lower()
  if answer == "a":
    output = "count again carefully"
    score -=1
  elif answer == "b":
    output = "element or atom"
    score -=1
  elif answer == "c":
    output = "check"
    score -=1
    
  elif answer == "d":
    output = "congratulations"
    tracker =1
    score +=1
  else:
    output = "Please choose a, b, c or d only."

  

  print()
  print(output.lower())
  print()
  print("Your current score: " + str(round((score/total_num_of_qn*100),1)) + "%"  )
  print()
  print()
  
print("End of quiz!")
