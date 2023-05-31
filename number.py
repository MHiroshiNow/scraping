import sys
def number_shop():
    n=input("店舗番号を入力してください。")
    url='ポータルのURLを入れる'+n
    print(url)

# number_shop()
args = sys.argv
url='店舗のURLを入れる'+args[1]
print(url)
print(args[1])
