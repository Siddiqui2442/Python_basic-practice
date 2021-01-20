#No.1-start
#変数　= 箱のような物
#変数がある事で、文字や数字をなどのデータを変数に入れておくことができる
#変数(箱)にデータを入れる事を[代入]といい、取り出す事を[参照]という
#変数には名前を付ける事ができ、[変数名]という
#変数を作る事を[変数宣言]という
#初めて変数にデータを入れることを[変数の初期化]という
#No.1-End

#No.2-start
#変数の宣言構文
#num = 1
#print(num)
#文字列や変数の中を参照すには、print関数を使う
#No.2-End

#No.3-start
#変数名はアルファベット.数字.アンダースコアが使える。
#様々な変数名を試してみる
#num = 1 print(num) OK
#num01 = 2 print(num01) OK
#num_01 = 3 print(num_01) OK
#No.3-End

#No.4-start
#NGな変数名.数字から始まる物
#num$01 = 1 print(num$01) NG
#num-01 = 2 print(num-01) NG
#01nunm = 3 print(01num) NG
#No.4-End

#No.5-start
#大文字と小文字は区別される
#NUM = 1 print(NUM)
#Num = 2 print(Num)
#No.5-end

#No.6-start
#変数名で予約語は使えない
#return = 1 print(return) こういう使い方はできない
#No.6-End

#No.7-start
# データ型とは，変数に入れるデータの種類の事
#数値型は整数=int型.小数=folat型がある
#num01 = 123 print(num01) 整数型
#num02 = 1.23 print(num02) 小数型
#どのデータ型をtype(タイプ)を使用して確認する事ができる
#print(type(num01)) print(type(num02))
#No.7-End

#No.8-start
#文字列型(String)
#str_a = "Hello World"
#print(str_a)
#print(type(str_a))
#No.8-End

#No.9-start
#プール型はTrueまたはFalseの二つのうち、どちらか1つを持つ型です。
#10>1は10が大きい.これを変数に代入するとTrueが入る
#10<1は誤りで，変数にに代入するとFalseが入る

#True結果
#a = 10
#b = 1
#bool01 = (a > b)
#print(bool01)
#print(type(bool01))

#False１結果
#a = 10
#b = 1
#bool01 = (a < b)
#print(bool01)
#print(type(bool01))
#No.9-End

#No.10-Start
#List(リスト)は，複数のデータを格納する事ができるデータ型
#リストの1つ1つの箱の事をを要素という
#リストのそれぞれの要素には，場所の情報が割り当てられている
#住所=インデックス番号が割り当てられている。0から始まる

#a = ["Taha","Bob","Tom"]
#print(a)
#a[0] = "Siddiqui"

#print(a[0])
#print(a[1])
#print(a[2])

#リストの中にリストを入れる
#A =[["sato","suzuki"],["tanaka","yamada"]]
#print(A[0][0])
#print(A[0][1])
#print(A[1][1])
#print(A[1][1])
# No.10-End

#No.11-Start
#算術演算子は足し算.引き算.掛け算.割り算などをするための演算子
#「+」「-」「*」「/」「%」

#x = 10
#y = 2
#print(x + y)
#print(x - y)
#print(x * y)
#print(x / y)
#print(x % y)

#関係演算子は2つの値が正しいか、正しくないか判断させる演算子のこと

#x = 10
#y = 2
#print(x > y) true
#print(x < y) false
#(「>」大きい(超える) (「<」小さい(未満)

#x = 10
#y = 2
#z = 10
#print(x <= y) False
#print(x >= z) True
#(「>=」以上の場合)　(「<=」以下の場合)

#x = 10
#y = 2

#print(x == y) False
#print(x != y) True
#等価は，2つの値が等しいということ
#(等価は「==」が2つ)　(等価でない場合は「!=」を使用)

#論理演算子は複数の条件を判断させる演算子のこと
#(かつ「and」) (または「or」)ということ

#and条件
#x = 8
#y = 3 

#print(x >=5   <= 10) True
#print(y >=5   <= 10) False

#or条件
#print(x == 3  == 3) False
#print(x == 1   == 1) False

#代入演算子.代入するときに，足し算や引き算を同時にすることができる
#複数代入演算子.足し算，引き算などと組み合わせること

#x = 8
#y = 12
#z = 20

#x += 10
#z += y
#print(x)
#print(z)
#No.11-End

#No.12-start
#プログラムの基本的な動きは「順次進行」「条件分岐」「繰り返し」の3つ
#if文(条件分岐)　if 条件:
                   #条件を満たしたときの処理
#age = 22
#age = 18
#if age >= 20:
    #print("adult")

#if~else文.条件を満たさないときの処理を記述・実行することができる
#if 条件A:
  #条件Aを満たしたときの処理
#else:
  #条件を満たさないときの処理
#age = 18
#age = 22
#if age  >=20:
    #print("adult")
#else:
    #print("child")

#if~elif文.もう一つ条件を加えたい場合に使う
#if 条件A:
  #条件Aを満たしたときの処理
#elif 条件B:
  #条件Bを満たしたときの処理
#else:
  #条件を満たさないときの処理

#age = 0
#age = 18
#age = 22
#if age >= 20:
    #print("adult")
#elif age == 0:
    #print("baby")
#else:
    #print("child")
#No.12-End

#No.13-start
#繰り返し処理.反復処理.ループ処理同じ
#for文
#for 変数(カウント変数)in range(繰り返す回数)繰り返し中に実行する処理

#for i in range(5):
#for i in range(5+1):
    #print(i)
#No.13-End

#No.14-start
#break文.繰り返しを終了する
#for i in range(5):
    #if i == 3:
         #break
    #print(i)
#continue文.ある条件に当てはまったときにその処理をスキップしたい場合に使います。
#for i in range(5):
    #if i == 3:
        #continue
    #print(i)
#for文の中にfor文入れる構造の事を「for文のネスト」という
#for i in range(3):
    #for j in range(3):
        #print(i,j,sep="-")

#for文でリスト内を参照
#arr = [2,4,6,8,10]
#for i in arr: #変数iに格納
    #print(i)
#arr = [2,4,6,8,10]
#sum = 0
#for i in arr:
    #sum += i
#print(sum)
#No.14-End

#次回は関数とクラスについて学習


