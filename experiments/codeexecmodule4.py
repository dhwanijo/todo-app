import webbrowser

user_term = input("Enter the term you want to search: ")
webbrowser.open("https://www.google.com/search?q=" + user_term)