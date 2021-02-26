import webbrowser

url = "https://en.wikipedia.org/wiki/"


enter = input("What'is you search: ")

url += enter
print(webbrowser.open(url))

