import webbrowser

try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")

# to search
query = "java википедия"

for j in search(query, tld="co.in", num=1, stop=1, pause=2):

    webbrowser.open('https://ru.wikipedia.org/wiki/Java', new=2)

    print(j)

# to search2

query = "python википедия"

for k in search(query, tld="co.in", num=1, stop=1, pause=2):

    webbrowser.open('https://ru.wikipedia.org/wiki/Python', new=2)

    print(k)

# to search 3

    query = "хентай википедия"

    for l in search(query, tld="co.in", num=1, stop=1, pause=2):

        webbrowser.open('https://ru.wikipedia.org/wiki/%D0%A5%D0%B5%D0%BD%D1%82%D0%B0%D0%B9', new=2)

        print(l)