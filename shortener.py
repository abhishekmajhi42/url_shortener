import url_shortener


'''url1="https://rims-edu.in"
url_short=url_shortener.make_shorten(url1)
print(url_short)'''


file=open('url_file.txt','r')

lines=file.readlines()

file2=open(r"url_file_shortened.txt","w+")

for url in lines:
    url_short=url_shortener.make_shorten(url.strip('\n'))
    print(url_short)
    file2.write(url_short)
    file2.write("\n")

file.close()
file2.close()

