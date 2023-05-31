import subprocess


n = input("店舗番号を入力してください。")
with open("database.txt", "r", encoding="utf-8") as file:
    for line in file:
        if n in line:
            mylist = line.split(",") # lineをカンマで分割
            data1 = mylist[0]
            data2 = mylist[1]
            data3 = mylist[2]
            


# 実行するファイル名と引数を指定する
filename = "sanitary_check_test.py"
args = [data1,data2,data3]

# コマンドを生成する
cmd = ["python", filename] + args

# コマンドを実行する
result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# 標準出力と標準エラー出力を出力する
print(result.stdout.decode())
print(result.stderr.decode())

