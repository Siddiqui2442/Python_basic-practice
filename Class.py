#クラスとは「データ」と「処理」をまとめたものになる
#データのことを「アトリビュート」という
#処理のことを「メゾット」という
#アトリビュートは、クラス内で定義された変数のことである
#数値や文字列を代入したり，参照したりすることができる
#クラスにアトリビュートを作ることを「アトリビュートを定義する」という
#アトリビュートと変数の違いは，クラスの外にあるかクラスの中にあるか:変数は外:アトリビュートは中

#メゾットも関数と同じで，色々な「処理」をまとめて1つにしたもの
#簡単に例えると、メゾットはラス内に定義された関数である
#メゾットも関数と同じようにdefで定義する
#まとめると、「アトリビュート」はクラス内の変数、「メゾット」はクラス内の関数ということになる
#クラスを作ることをクラスを定義すること言う


#メゾットを定義する場合，必ず1つ引数を記述しなければならない
#関数の場合は，渡したい引数がない場合，空欄でもよい
#メゾットの場合は，渡したい引数がない場合でも必ず引数が1つ必要になる
#この引数は，どんな引数名でもよいが、「self」と書くのが習慣
#メゾットに渡したい引数が1つの場合，メゾットの引数にselfと渡したい引数名の合計2つ書く

#class Student:
    #def avg(self):
        #print((80 + 70)/2)
#クラスはこのままでは使えない
#クラスから作られたインスタンスを変数に代入してから使う

#変数名
#a001 = Student()
#これでクラスを使えるようになる
#クラスを使えるような状態にすること「インスタンス化」=実態という意味「オブジェクト化」「オブジェクト生成」といったりする
#インスタンス化とは，クラスという型から，インスタンスという実査に使える「モノ」を作ることをいう
#a001をインスタンス化と呼ぶ
#a001.avg()

#クラスを使い回す場合
#class Student:
    #def avg(self,math,english):
        #print((math + english)/2)
#a001 = Student()
#a001.avg(80,70)

#アトリビュートは，クラス内に定義された変数のこと
#class Student:
    #def avg(self,math,english):
        #print((math + english)/2)
#a001 = Student()
#a001.avg(80,70)

#a001.name = "taha"
#これでアトリビュートの定義はおわり
#print(a001.name)
#print(a001.gender) 未定義のアトリビュートはエラーになる
#a002 = Student()
#print(a002.name)未定義のためエラー

#インスタンスごとにアトリビュートを定義しなければならない
#インスタンスごとにアトリビュートが存在するのでインスタンスを作るごとに，アトリビュートを定義する必要がある
#「a001.name」のような記述をインスタンスごとに10個，記述しなければならない
#その不便さを解消するのが「コンストラクタ」である
#コンストラクタは，インスタンス化するときに，自動的に実行されるメゾットのこと
#コンストラクタは「初期化メゾット」ともいう
#初期化メゾットは、インスタンス化をすれば、必ず実行されるメゾットである
#あとから使うアトリビュートをは、初期化メゾットで自動的に作っておけばおけ

#初期化メゾットの記述方法
#class Student:
    #def __init__(self,name):
        #self.name = name

    #def avg(self,math,english):
        #print((math + english)/2)

#a001 = Student("taha")

#print(a001.name)

#a002 = Student("siddiqui")
#print(a002.name)

#クラスの便利なところ:一度定義しておけば，あとからいくらでもインスタンスを作ることができる
#コピペでどんどんインスタンスをつくることができる

#まとめ

#def __int__(self): コンストラクタ
#self.name = "" アトリビュート

#def avg(self,math,englis): メゾット
#print((math + english)/2)

#インスタンス a001 = Student() クラス
#a00.name = "taha"
#print(a001.name)