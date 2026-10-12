
import emoji

name = input("Enter your name: ")
print("Hello", name + "!", emoji.emojize(":smile:"))

activity = input("Enter your favorite activity: ")

print("Enjoy", activity + "!", emoji.emojize(":star:"))
print(emoji.emojize("Keep learning Python! :thumbs_up:"))
