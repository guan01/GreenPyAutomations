import pandas as pd
simpsons = pd.read_html("https://en.wikipedia.org/wiki/List_of_The_Simpsons_episodes_(seasons_1%E2%80%9320)#Season_1_(1989%E2%80%9390)")

# print table count in html
print(len(simpsons))
# print the second table from the html...
print(simpsons[2])