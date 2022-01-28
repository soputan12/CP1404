import wikipedia

# print(wikipedia.search("Virus"))
# print(wikipedia.summary("malware"))
# print(wikipedia.page("New York"))

user_input = input(">>>")
a = wikipedia.page(user_input, auto_suggest=False)
print(a.title)
print(a.summary)
print(a.url)