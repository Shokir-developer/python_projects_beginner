import webbrowser

url = input("Enter url link completely: ")

download = url[:12] + "ss" + url[12:]

webbrowser.open(download)