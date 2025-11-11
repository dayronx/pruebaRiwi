# calculo_grade = float(input("Enter your Calculus grade: "))
# algebra_grade = float(input("Enter your Algebra grade: "))
# physics_grade = float(input("Enter your Physics grade: "))


option = ""

while option !=4:
   print("\n--- MENU ---")
   print("1.Calculus")
   print("2. Algebra")
   print("3. Physics")
   print("4. Exit")
   print("*******************************************************")

   option = input("Choose an option (1-4): ")

   if option =='1':
      exam1_score = float(input("Enter your first exam score: "))
      exam2_score = float(input("Enter your second exam score: "))
      exam3_core  = float(input("Enter your third exam score: "))
      exam4_score = float(input("Enter your fourth exam score: "))

      average = (exam1_score+exam2_score+exam4_score+exam4_score)/4

      if average == 5:
         print("*******************************************************")
         print(f"With your grade of {average}, it is...Excellent, your grade is perfect.")
         print("*******************************************************")
      elif average < 5 and average > 3:
         print("*******************************************************")
         print(f"With your grade of {average}, it is...You passed the course.")
         print("*******************************************************")
      elif average == 3:
         print(f"With your grade of {average}, it is...You made it, but it was close.")
      elif average < 3 and average > 1:
         print("You failed the Calculus course.")
      elif average <= 1:
         print(f"With your grade of {average}, it is...You've neglected this subject; you're very lazy.")
      else:
         print(f"With your grade of {average}, it is...This grade does not correspond to this grading system.")



   elif option =='2':
      
      exam1_score = float(input("Enter your first exam score: "))
      exam2_score = float(input("Enter your second exam score: "))
      exam3_core  = float(input("Enter your third exam score: "))
      exam4_score = float(input("Enter your fourth exam score: "))
      average = (exam1_score+exam2_score+exam4_score+exam4_score)/4

      if average == 5:
         print("Excellent, your grade is perfect.")
      elif average < 5 and average > 3:
         print("You passed the course.")
      elif average == 3:
         print("You made it, but it was close.")
      elif average < 3 and average > 1:
         print("You failed the Algebra course.")
      elif average <= 1:
         print("You've neglected this subject; you're very lazy.")
      else:
         print("This grade does not correspond to this grading system.")

   elif option =='3':
   
      exam1_score = float(input("Enter your first exam score: "))
      exam2_score = float(input("Enter your second exam score: "))
      exam3_core  = float(input("Enter your third exam score: "))
      exam4_score = float(input("Enter your fourth exam score: "))
      average = (exam1_score+exam2_score+exam4_score+exam4_score)/4

      if average == 5:
         print("Excellent, your grade is perfect.")
      elif average < 5 and average > 3:
         print("You passed the course.")
      elif average == 3:
         print("You made it, but it was close.")
      elif average < 3 and average > 1:
         print("You failed the Algebra course.")
      elif average <= 1:
         print("You've neglected this subject; you're very lazy.")
      else:
         print("This grade does not correspond to this grading system.")

   elif option =='4':
      break