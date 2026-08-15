import json
import os

FILE_NAME = "students_data.json"

def load_data():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            return json.load(file)
    return {"students": [], "s_ditelis": [], "s_dic": {}}

def save_data(data):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def works(n):
    data = load_data()
    students = data["students"]
    s_ditelis = data["s_ditelis"]
    s_dic = data["s_dic"]

    if n == 1:
        s_name = input("Enter the name of student: ")

        if s_name in students:
            no = s_dic[s_name]
            print()

            for key, value in s_ditelis[no].items():
                print(key,value)

        else :
            print("\nHe is not our student.")

    elif n == 2:
            ns_name = input("\nWhat is the nickname of him: ")
            students.append(ns_name)
            s_dic[students[-1]] = list(s_dic.values())[-1]+1

            s_ditelis.append({})
            print("\nEnter the following information: \n")

            for key in s_ditelis[0].keys():
                print(key,end=" ")
                s_ditelis[s_dic[ns_name]][key] = input()

            save_data(data)

    elif n == 3:
        rs_name = input("Give the student name: ")

        if rs_name in students:
            students.remove(rs_name)
            s_ditelis.pop(s_dic[rs_name])

            for key in s_dic.keys():
                if s_dic[key] > s_dic[rs_name]:
                    s_dic[key]= s_dic[key]-1

            del s_dic[rs_name]

            save_data(data)
                        
        else:
            print("\nHe is not our student.")

    elif n == 4:
        s_name = input("\nGive the student name: ")

        if s_name in students:
            i = 1
            keys = ["Full Name","ID No","Class","Age"]
            for key in keys:
                print(i,".",key)
                i += 1

            choose = int(input("\nWhat do you want to update: "))

            s_ditelis[s_dic[s_name]][keys[choose-1]+":"] = input("Update Data: ")

            save_data(data)

        else:
            print("He is not our student.")

    elif n == 5:
        print("\nOur students are:")
        for name in students:
            print("    ",name)