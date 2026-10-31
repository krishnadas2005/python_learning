#Create a global variable called school and set it to "CS50".
school = "CS50"
#Define a function called show_scope().
def show_scope():
    topic = "Scope"
    print(F'outside variable: {school}.')
    print(f'inside variable: {topic}.')

show_scope()

print(school)