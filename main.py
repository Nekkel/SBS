
try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")

# to search
query = "java википедия"

for j in search(query, tld="co.in", num=1, stop=1, pause=2):

    print(j)

# to search2

query = "python википедия"

for k in search(query, tld="co.in", num=1, stop=1, pause=2):

    print(k)
# to search 3
    query = "хентай википедия"

    for l in search(query, tld="co.in", num=1, stop=1, pause=2):
        print(l)