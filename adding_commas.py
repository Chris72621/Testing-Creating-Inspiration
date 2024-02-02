user_input = input("Enter Data Here: ")

result = ""

for i in range(len(user_input) - 1):
    if user_input[i] != " " and user_input[i+1] == " ":
        result += user_input[i]
        result += ","
    else:
        result += user_input[i]
    

        
print("Result: ")
print(result)