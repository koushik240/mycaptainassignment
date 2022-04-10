import csv

def write_into_csv(info_list):
    with open('student_info.csv',"w+" ,newline='')as csv_file:
        writer = csv.writer(csv_file)
        #to give only one header
        if csv_file.tell()==0:
            #to categorize it
               writer.writerow(["name","age","contact number","e-mail id"])
               writer.writerow(info_list)




#main function
if __name__ == '__main__':
    condition = True
    #additional information as in no.of students
    student_num = 1
    while condition :
        student_info = input("Enter student information for student#{} in the following format(name age contact_number e-mail id): "
                             .format(student_num))



    #split
        student_info_list = student_info.split(' ')


        print("\n The entered information is -\nName: {}\nAge: {}\nContact_number: {}\nE-mail id:{}"
            .format(student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3]))
        choice_check = input("Is the entered information correct (yes/no) ")

        if choice_check == "yes":
         write_into_csv(student_info_list)
         condition_check = input("Enter (yes/no) if you want to enter information for another student: ")

         if condition_check == "yes":
             condition = True
             student_num = student_num + 1

         elif condition_check == "no":
             condition = False
        #if the given information is wrong then the user should enter th evalue again
        elif choice_check == "no":
            print("\nPlease re enter the values! ")




