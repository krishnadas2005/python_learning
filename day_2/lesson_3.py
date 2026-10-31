#asks user their name
name = input("Enter the name: ")

#asks user what you want to learn               
study = input("Enter what you want to learn: ")

#asks users favourite tool
tool = input("Enter your favourite tool: ")

#display heading
print("_____MY_LEARNING_CARD_____")

print("my name is ",name, "i want to study",study, "my favourite tool is",tool, sep='|')
print(name, study, tool, sep='|')

print("next step...", end=" ")
print("learn independently")            

print("Python", "Git", sep=' / ', end=": ")
print("ready")