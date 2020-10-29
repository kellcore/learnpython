from sys import argv

script, user_name, message = argv
prompt = '" " '

print(f"Hi, {user_name}! I'm the {script} script.")
print("I'd like to ask you a few questions.")
print("Then I have a special message for you.")
print(f"Do you like me, {user_name}?")
likes = input(prompt)

print(f"Where do you live, {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f"What's your favorite piece of advice?")
advice = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. NOICE.
You said {advice}!
Here's a special message for you: {message}!
""")
