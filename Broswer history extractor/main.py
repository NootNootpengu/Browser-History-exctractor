from browser_history.browsers import Firefox, Chrome

f = Chrome()
outputs = f.fetch_history()

# his is a list of (datetime.datetime, url) tuples
his = outputs.histories
print(his)
input()
