tc = int(input())

num_lst = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

for i in range(tc):

    num_dic = {}

    numbering = input()
    num = list(map(str, input().split()))
    for k in range(len(num_lst)):
        cnt = 0
        for j in range(len(num)):
            if num_lst[k] == num[j]:
                cnt+= 1
            num_dic[num_lst[k]] = cnt

    # print(num_dic)

    print(f"#{i+1}")
    print("ZRO " * num_dic["ZRO"], "ONE "* num_dic["ONE"], "TWO "* num_dic["TWO"], "THR "* num_dic["THR"], "FOR " * num_dic["FOR"], "FIV "* num_dic["FIV"], "SIX "* num_dic["SIX"], "SVN "* num_dic['SVN'], "EGT "* num_dic['EGT'], "NIN "* num_dic['NIN'])

'''
1
#1 7041
SVN FOR ZRO NIN FOR EGT EGT TWO FOR FIV FIV ONE SVN ONE ONE FIV TWO SVN SIX ONE FOR TWO THR TWO TWO ONE SIX EGT FIV SVN SIX ONE EGT NIN TWO SVN NIN FIV FOR THR ONE TWO THR THR FOR ONE ONE THR EGT SVN FOR TWO SVN SVN NIN THR ONE NIN EGT SIX FIV ZRO TWO EGT SIX ZRO TWO FOR EGT SIX FIV ZRO NIN ZRO ZRO SIX ONE THR EGT NIN THR FOR FOR SIX ZRO SIX SIX ONE EGT FOR NIN SIX THR SVN EGT EGT TWO NIN ONE THR FIV NIN EGT FOR ZRO SVN SIX THR SIX ONE FIV FOR TWO ZRO NIN SVN THR SVN TWO SIX ZRO ONE SIX FIV SVN FIV FOR ONE TWO ZRO ZRO ONE FOR SIX ZRO SVN ONE SVN SVN SVN SVN THR THR FIV NIN NIN EGT ONE EGT TWO SIX SIX ZRO THR EGT ZRO ONE TWO FIV ZRO NIN FOR SVN EGT THR FIV ONE TWO ZRO ONE SIX FOR ZRO SIX ONE EGT NIN EGT FOR ONE FOR THR NIN EGT EGT ZRO EGT SVN SVN EGT THR EGT THR SVN ONE ZRO SVN THR FOR NIN SIX FIV ONE ZRO NIN NIN SIX EGT THR FOR EGT FOR NIN NIN TWO FIV FIV THR THR THR SVN FOR THR EGT ZRO EGT EGT ZRO SIX EGT ONE NIN EGT NIN SVN TWO TWO EGT TWO EGT NIN ZRO SVN EGT ONE FIV EGT SIX ONE TWO FOR TWO FIV EGT SIX TWO SIX FIV THR NIN TWO FOR SIX ONE EGT TWO ONE ONE NIN SVN SIX TWO NIN FIV TWO ZRO ZRO THR NIN ONE EGT ONE NIN FIV THR TWO FIV TWO FIV EGT SIX SVN SVN TWO TWO NIN FOR ONE NIN SIX NIN EGT TWO FIV FIV FOR NIN ONE TWO FIV ZRO EGT THR NIN THR NIN SIX SVN NIN NIN SVN SIX NIN THR FIV SVN SIX SIX FIV EGT TWO FIV FOR FOR ONE SIX ONE SIX THR THR FIV FIV THR TWO EGT TWO FIV THR SIX ONE EGT SIX TWO ONE FOR SIX TWO NIN ONE FIV ZRO THR SIX FOR NIN TWO NIN THR FOR FOR ZRO FIV NIN SIX THR FOR TWO EGT EGT SVN FIV EGT ONE TWO FIV SVN FOR FOR FOR FOR FOR TWO NIN THR ZRO SVN SVN EGT SVN THR ZRO THR EGT TWO FIV TWO ZRO THR SVN TWO NIN SVN FIV THR FOR THR TWO ONE ONE THR TWO FIV THR FIV ONE TWO TWO TWO SIX FOR ZRO SVN ZRO THR FOR ZRO ZRO FIV THR ONE ZRO SIX SVN FIV ZRO ZRO FOR FIV FOR NIN FIV SIX FOR EGT TWO ONE SIX EGT THR ONE FOR EGT FOR NIN TWO ZRO SVN ZRO SIX ZRO SVN ZRO FIV SIX SVN THR EGT FOR NIN TWO SIX FIV SVN SVN FOR FIV SVN NIN EGT THR ZRO TWO TWO THR SIX SVN ONE FIV FIV FOR ZRO TWO SIX ZRO SIX ONE ONE ONE SVN THR ZRO ZRO FOR EGT THR ZRO ONE TWO NIN ZRO THR EGT EGT FIV SVN SVN ZRO EGT NIN THR ZRO SVN FOR SVN EGT THR SVN ONE ZRO ZRO EGT THR FOR FIV ZRO ONE FOR FIV SIX TWO ZRO THR FIV SIX SIX SIX SVN SIX SVN SVN ONE NIN ONE SIX TWO SVN TWO SVN SIX FIV ONE THR NIN NIN FIV NIN TWO SIX FIV THR TWO FOR FOR FOR TWO SVN NIN TWO THR SVN THR ONE FIV SVN EGT FIV EGT THR TWO FOR ONE ONE FIV NIN FIV ONE ZRO SIX FOR FIV THR ZRO EGT NIN ONE THR FOR SVN FOR SIX THR SIX FIV TWO EGT ONE ZRO THR ONE FIV FIV TWO TWO ONE SVN FOR EGT TWO THR SIX THR ZRO THR FIV TWO EGT ZRO SVN TWO TWO FIV NIN ONE ZRO EGT FIV ZRO SVN NIN ZRO FIV THR FOR ONE ZRO FOR EGT FIV NIN TWO FIV FOR ONE THR NIN FIV EGT TWO SVN NIN SIX ONE SVN SVN ONE NIN ZRO THR FOR ONE SVN FIV THR THR TWO FOR ONE TWO NIN ZRO EGT SVN FOR FIV SIX EGT ZRO SVN SVN FOR THR ONE THR SIX THR ZRO ONE NIN ZRO FOR TWO NIN THR ONE FOR EGT TWO ZRO FIV FIV NIN THR TWO EGT SVN FOR EGT ONE FOR THR FIV FIV TWO SIX EGT NIN TWO NIN FIV NIN FOR FIV ZRO FIV EGT EGT ZRO ONE THR TWO TWO TWO SVN ZRO THR ONE THR THR SVN ZRO NIN FIV FIV EGT THR SVN EGT THR SVN NIN THR NIN ONE EGT TWO EGT ZRO ONE EGT FOR EGT SIX ZRO NIN THR ZRO ZRO EGT SVN SIX THR FIV SIX FIV EGT THR NIN FOR EGT THR NIN SVN SIX FOR FIV EGT SIX ONE FIV FIV ONE NIN SIX FOR FIV FOR TWO FIV THR TWO SIX EGT TWO SIX SIX THR NIN FOR FIV SIX TWO FIV THR FIV SIX SIX ONE FOR FOR SIX TWO SIX EGT TWO FIV FIV ONE ZRO ONE FIV ONE SVN SIX ZRO ZRO TWO FOR THR THR SIX TWO EGT TWO THR FOR THR FOR THR SIX EGT FOR SVN THR NIN EGT ZRO ZRO EGT EGT ZRO FIV ONE FOR THR SIX THR NIN TWO ONE NIN EGT TWO THR FOR ZRO TWO THR ONE NIN EGT NIN EGT NIN ONE THR FIV ONE FOR TWO FIV THR EGT NIN TWO EGT SVN ZRO ONE FOR EGT ONE NIN THR FIV NIN SVN NIN EGT ZRO ONE FOR SVN FIV FIV FIV ZRO NIN TWO EGT TWO FOR FIV ZRO FOR FOR ZRO FIV ONE ONE FIV NIN ZRO EGT THR EGT SVN TWO SIX NIN THR EGT ONE ZRO THR THR EGT FOR EGT ZRO ONE FIV FOR ONE THR SVN THR FIV EGT FIV SIX NIN ZRO EGT NIN THR SIX ZRO SIX NIN SVN EGT NIN FOR ONE FIV SIX SIX SIX SIX SIX SVN ONE FOR ZRO SIX ONE TWO ONE FOR NIN FIV TWO THR FOR ONE FIV TWO THR ONE SIX EGT EGT TWO SVN SVN ONE TWO SIX ZRO FOR NIN FOR SIX ZRO THR SIX TWO FOR FIV EGT EGT ONE TWO ONE FOR NIN EGT TWO FOR FIV TWO NIN NIN EGT THR EGT SIX NIN EGT SIX SIX TWO THR EGT TWO SIX TWO SVN FIV SVN EGT TWO SVN EGT ZRO TWO ZRO EGT NIN TWO EGT TWO ZRO FIV FIV TWO SVN SIX SVN EGT SVN EGT ONE SIX ZRO NIN FIV EGT NIN ZRO ZRO ZRO SVN TWO FIV FIV TWO ONE FOR EGT SIX FOR SIX EGT NIN EGT THR FIV FIV ONE FIV FIV EGT FOR ZRO FIV FOR SVN TWO ONE FOR NIN NIN ZRO THR ZRO THR FIV ZRO SVN SIX SVN EGT THR SIX FOR FOR ONE NIN FIV FIV SVN FOR SVN THR FOR ZRO EGT EGT ONE FIV TWO THR TWO FOR SIX SIX SIX TWO NIN ZRO FOR NIN THR ONE ONE NIN NIN FIV FIV FIV SIX ZRO FIV NIN FOR SIX THR FOR NIN ZRO FIV THR NIN ONE TWO EGT EGT ONE EGT SIX ZRO TWO FOR NIN ZRO TWO TWO ONE FIV FOR FOR FOR TWO FIV ZRO FOR TWO ONE TWO SVN SVN NIN FIV FIV FOR ZRO THR FOR ONE TWO TWO NIN EGT TWO TWO SVN EGT FIV EGT THR NIN FOR FOR SIX NIN EGT FIV SIX SIX ZRO SVN TWO SVN TWO SIX FOR SVN ONE THR TWO ONE SIX THR EGT THR TWO EGT SIX ZRO ONE TWO SIX ZRO FIV FOR SIX SVN NIN THR FOR SVN EGT EGT ONE SIX THR EGT SVN SIX ONE SVN TWO THR SVN EGT FIV EGT FIV EGT SVN THR THR ONE ZRO EGT ONE ZRO NIN TWO FOR NIN ONE FIV SVN THR THR FOR TWO TWO ZRO ONE TWO SVN SVN ZRO TWO FOR ONE ZRO THR SVN THR NIN FIV NIN SVN TWO ZRO TWO EGT SIX SVN ZRO EGT ONE EGT THR ZRO THR SIX TWO ZRO TWO EGT FOR ONE EGT THR SVN FIV EGT ONE SVN ZRO FOR EGT EGT ONE THR SIX SVN EGT NIN FIV FIV FIV SIX SIX THR ZRO ZRO EGT EGT TWO THR ZRO SIX FIV ZRO NIN SVN TWO TWO EGT TWO NIN FOR FOR EGT TWO SVN TWO FIV EGT FOR SVN THR NIN FIV ONE NIN ZRO TWO EGT THR ONE FOR THR ONE ZRO FOR ZRO SVN NIN ZRO EGT ONE FOR ZRO SVN NIN FIV THR EGT TWO THR TWO ONE ZRO FOR ZRO SVN FIV NIN ZRO FIV ONE TWO ZRO NIN EGT NIN ONE SVN THR THR ZRO SVN SIX SIX ZRO TWO EGT NIN EGT NIN NIN NIN FOR TWO ZRO EGT SVN EGT SVN THR ZRO SVN SIX FOR TWO ONE NIN ONE SIX ZRO THR THR SIX TWO TWO ONE FOR THR TWO SIX ZRO FIV FOR NIN SIX ZRO EGT TWO SVN FOR ZRO SVN SIX ZRO ONE TWO NIN THR EGT FIV ONE FIV SIX SIX EGT EGT NIN EGT SVN ZRO SVN NIN ONE FIV EGT SIX THR NIN FOR FIV THR EGT TWO THR NIN FOR EGT FIV ONE THR TWO EGT ONE SIX FOR SIX SVN SVN NIN SIX FOR ONE NIN TWO SIX THR ONE FIV NIN SVN ZRO TWO SIX ONE SVN SIX TWO FIV THR FOR ZRO SVN FIV FIV THR ONE EGT EGT EGT ZRO ONE SVN FIV ZRO FIV NIN ZRO NIN THR FIV FOR TWO SVN TWO SIX SVN TWO TWO ZRO ONE ONE SVN FIV NIN ONE EGT ONE SVN EGT SIX SIX NIN NIN TWO SIX SIX FIV EGT FOR ZRO THR SVN EGT THR ONE ONE TWO FIV SVN SIX TWO ONE SIX ONE ONE FIV SVN FOR EGT FIV SIX FOR NIN EGT FOR THR TWO FIV THR EGT THR TWO SVN ZRO SIX EGT ZRO ONE ONE NIN FIV THR SIX THR ONE FIV THR FOR ZRO THR ONE SVN NIN ZRO THR FIV TWO NIN ONE TWO SIX ONE SVN ZRO ONE FIV TWO TWO NIN ZRO FIV ONE EGT THR SIX EGT EGT SIX ONE SIX SIX SVN ZRO FOR NIN EGT NIN FOR NIN EGT SVN FIV SIX FOR EGT SIX EGT SVN EGT ZRO NIN FIV SIX NIN ZRO ZRO ONE THR FIV FIV EGT ZRO ONE SVN SVN FOR SIX SVN ZRO SVN FOR ONE TWO ONE EGT THR FIV SVN ONE FOR SVN SIX EGT TWO THR ZRO TWO SVN EGT EGT FIV NIN SVN ONE THR FOR SVN ONE THR SVN ONE TWO SVN FIV THR FOR FOR FIV FIV ONE FOR ONE TWO SIX SIX THR THR ZRO ZRO EGT ONE THR EGT ONE SIX NIN EGT ZRO ONE THR NIN THR NIN THR SIX FIV FIV FOR ZRO FIV ZRO SIX FIV FIV ONE EGT NIN SIX TWO TWO FIV ZRO FIV TWO FIV TWO ZRO SIX SVN TWO EGT ZRO ZRO SIX EGT THR ZRO SIX FOR THR SVN ZRO FIV TWO ZRO SVN FIV SIX ONE EGT ONE EGT FIV SIX FIV NIN TWO SIX FIV TWO THR TWO ONE TWO TWO EGT EGT EGT SVN FOR ZRO ZRO FIV NIN NIN FIV THR ZRO NIN NIN FIV ONE ONE ONE TWO THR THR NIN SVN TWO THR THR ZRO FOR EGT FOR THR NIN TWO FOR NIN ZRO FIV SVN FOR SVN SIX SIX THR ZRO NIN ZRO EGT ZRO ONE FIV ONE ZRO THR NIN FIV EGT NIN SIX TWO FIV SVN SIX THR EGT FIV NIN THR ZRO TWO FIV ONE FIV SVN SVN NIN FOR ONE SVN EGT FIV SVN EGT EGT FOR TWO THR EGT FOR ONE THR ZRO FOR ONE SVN SVN TWO ONE THR ONE THR ONE FIV ONE FIV ZRO FIV ONE TWO TWO ONE FIV FIV THR EGT NIN TWO EGT FOR TWO SVN FIV EGT FOR ZRO NIN FOR FOR THR FIV EGT FOR ONE ZRO THR THR FOR ZRO SIX SVN FIV FIV SIX ZRO NIN EGT THR FIV SVN NIN ZRO FOR EGT SVN FOR ZRO TWO THR FIV FOR ONE SIX SIX FOR FIV TWO NIN ONE TWO FOR NIN NIN THR SVN SIX FIV EGT SVN EGT NIN SVN SVN ONE SIX FIV ZRO ONE THR TWO SIX ZRO FIV SVN FOR FOR NIN ZRO SIX ONE ONE NIN ZRO FOR TWO ONE NIN SVN ZRO NIN THR THR THR ONE THR FIV SIX NIN FIV NIN EGT EGT THR NIN FIV ONE THR SIX TWO EGT EGT ONE NIN EGT ONE THR THR FOR THR NIN TWO SVN TWO ONE SVN SIX ONE SVN THR ZRO SIX ZRO TWO FIV SIX ZRO SVN TWO ZRO NIN FIV FOR THR TWO FIV SIX ZRO EGT EGT ONE FIV SVN FIV SVN NIN TWO THR SVN TWO SVN NIN THR SIX THR EGT ONE ZRO SIX EGT SVN SIX FIV ONE TWO NIN FIV SIX ONE FIV FOR ONE THR EGT FIV ZRO NIN TWO ONE THR THR FIV TWO NIN ZRO FOR EGT FIV SVN THR THR ZRO THR ZRO THR TWO ONE ONE ZRO EGT ONE EGT SVN TWO EGT NIN TWO THR ZRO TWO EGT TWO FIV FIV EGT ONE TWO FOR NIN EGT EGT TWO SVN ONE SVN NIN FIV ZRO THR FOR ZRO ONE FIV THR FOR TWO THR TWO NIN FOR NIN TWO FOR NIN ZRO FOR FOR NIN EGT FIV THR TWO THR ZRO ONE SVN ONE NIN EGT EGT THR TWO NIN THR THR TWO EGT THR FOR ZRO TWO ZRO ONE TWO ONE ZRO SVN SIX SIX EGT ZRO FIV EGT EGT NIN FIV SVN THR TWO TWO TWO ZRO ZRO TWO THR ONE SIX EGT SVN SVN TWO EGT SVN NIN FIV NIN TWO NIN ONE THR ZRO EGT ONE NIN TWO ZRO TWO FOR SVN FIV EGT ONE ZRO ZRO SVN ONE SIX NIN THR ZRO THR SVN THR ZRO FOR THR TWO THR ONE ZRO TWO SVN SVN ONE THR ZRO SVN ZRO THR SIX THR ONE NIN FIV SIX ONE FIV ONE ZRO NIN SVN THR ZRO EGT ONE FIV ONE SVN ONE SVN NIN FOR NIN EGT ZRO ZRO ONE EGT FIV ZRO EGT NIN TWO EGT ZRO EGT FIV ONE FOR SVN THR SIX ONE SIX EGT ZRO EGT SIX FIV SVN ONE ZRO TWO EGT THR FIV FIV SIX ONE FOR NIN THR EGT THR TWO THR THR SVN THR ZRO ONE FOR EGT SVN EGT NIN EGT NIN SVN NIN ONE NIN FIV EGT NIN SIX NIN THR THR ONE FOR ONE FOR FIV SVN SIX THR FOR SIX THR EGT THR FOR TWO SVN EGT NIN ZRO ONE FOR ZRO SVN THR FOR NIN FOR FIV SIX EGT NIN EGT NIN NIN SVN ZRO EGT FOR FIV SIX NIN THR SIX TWO ZRO ZRO SIX FIV ONE SIX ONE NIN SVN THR FIV ZRO ZRO SIX FIV ONE EGT TWO SVN TWO FOR FIV TWO TWO FIV EGT SIX NIN EGT THR FIV FIV ZRO FIV EGT ONE FIV ZRO SVN THR FOR ONE FIV SIX FOR ONE SVN ZRO FOR ZRO SIX ONE ZRO FIV FIV TWO FIV EGT THR TWO SVN EGT FIV TWO SVN TWO NIN SVN SIX THR ONE FIV NIN EGT NIN FIV FOR NIN FIV TWO FIV TWO TWO THR ZRO EGT SVN TWO EGT THR SVN FIV FOR ONE EGT TWO NIN SIX EGT NIN EGT ONE SIX THR SVN FIV FOR ONE ZRO ONE TWO TWO EGT FIV FOR SIX SVN SVN THR FOR FOR NIN ONE EGT THR EGT SVN NIN SVN ONE ONE FOR THR FIV TWO NIN ONE FIV FIV SIX SVN NIN ZRO TWO THR ONE NIN EGT SVN EGT FOR FOR FOR THR FIV EGT ZRO TWO NIN FOR NIN EGT THR FIV ZRO FOR THR FIV TWO FIV SVN SVN SVN FOR FOR ZRO FOR ONE ONE FIV FOR ZRO TWO EGT SIX EGT ONE FOR SVN SIX FOR NIN EGT SVN THR EGT SIX TWO EGT ZRO NIN EGT ZRO FOR NIN SIX EGT TWO EGT FOR SVN NIN FOR ZRO SVN FOR EGT ONE EGT TWO TWO ONE FOR SIX SIX NIN THR EGT ONE THR SIX FOR FIV TWO TWO ZRO ONE ZRO THR EGT SVN THR THR ONE FOR FIV SIX ONE TWO ONE NIN ONE EGT ZRO FOR SVN SVN FOR ONE ONE NIN EGT ONE ZRO THR TWO FIV ZRO THR TWO TWO SIX THR THR SIX ONE FIV EGT TWO ONE NIN THR NIN SVN TWO ONE THR TWO ZRO NIN TWO SVN FOR FIV ZRO THR TWO NIN SVN EGT ZRO ONE ONE FOR SVN FOR THR NIN NIN SIX SVN SIX TWO ZRO NIN SIX TWO THR ZRO THR FIV ONE NIN SIX SVN NIN TWO SVN FIV SIX EGT TWO FOR SIX THR ZRO NIN ONE EGT SVN SIX EGT FOR ZRO THR SVN NIN SIX TWO TWO SVN THR ZRO SVN THR ZRO SVN THR SIX FOR SIX SVN FOR ZRO ONE TWO FOR FOR SIX THR FOR FIV ZRO TWO ZRO ONE SIX NIN THR SVN NIN ONE FIV TWO FOR FOR ONE THR FOR SIX EGT EGT SVN ZRO THR FOR FOR SIX SVN ONE EGT ONE TWO ONE TWO THR ONE ONE ONE ZRO EGT NIN ONE ZRO NIN SVN SVN FOR FIV ONE SIX SVN EGT THR NIN THR ONE THR NIN SIX THR SVN FIV TWO ZRO SVN ONE SVN ZRO SIX SVN ONE SVN FIV FOR EGT ONE SVN FIV TWO ONE SVN FIV THR ONE ZRO ZRO ZRO FIV ZRO ZRO SVN EGT SIX FOR NIN ONE FOR EGT ZRO EGT NIN NIN SVN NIN NIN NIN SIX ZRO SIX THR EGT ZRO THR SIX NIN FOR TWO ZRO FOR FOR THR SIX NIN ONE EGT NIN ONE ONE EGT SIX THR FIV ZRO NIN ONE ZRO EGT TWO TWO SIX EGT NIN SVN SVN EGT NIN THR ZRO FIV SIX THR NIN SVN SVN FOR THR FIV EGT THR THR THR SIX ONE ZRO FOR SVN FOR TWO SVN ONE FIV SVN TWO TWO SVN ZRO THR SIX ZRO NIN EGT NIN SIX FOR ZRO TWO NIN ZRO THR TWO TWO FOR SVN SVN FOR FIV THR ONE THR THR FOR THR FIV TWO ONE SIX NIN EGT EGT FOR ONE FOR FIV SVN THR ZRO TWO SVN SVN SVN ZRO TWO ZRO ZRO EGT SIX FOR FIV ZRO ONE FIV SVN THR TWO SVN NIN ONE ONE FOR ZRO THR THR ONE FIV EGT THR ZRO FIV ONE ZRO TWO FIV ONE ZRO FOR ZRO SIX FOR EGT NIN FIV SIX TWO TWO TWO ONE SVN FOR SVN EGT SIX ZRO ZRO TWO ONE THR NIN TWO FOR ONE FIV FOR ZRO SIX SIX EGT ONE THR THR ONE ZRO FIV EGT NIN THR EGT NIN EGT FOR THR NIN NIN SIX NIN SVN SVN TWO FIV TWO THR TWO EGT THR THR EGT FIV SVN EGT EGT ONE THR FIV ONE TWO ZRO EGT SIX FIV FIV THR NIN FIV THR FIV FOR EGT FIV ZRO THR FIV ZRO EGT FOR THR FIV EGT ONE TWO SIX ZRO TWO TWO ONE SIX FIV ZRO ONE SVN SVN THR EGT THR FIV ONE THR TWO ONE NIN FOR TWO THR ZRO ONE FOR EGT SIX SIX ONE THR EGT SVN NIN FOR FOR THR FIV FOR FOR TWO SVN SVN FIV SIX SIX NIN ZRO SVN ZRO NIN EGT SIX SVN THR TWO ZRO ONE FIV THR FIV SIX FIV FOR SIX EGT ONE FIV EGT FIV THR THR TWO EGT SVN SIX NIN SIX FOR SIX THR TWO ONE ZRO FIV EGT SVN ZRO ZRO THR SVN THR FOR SIX TWO ZRO ONE ONE SIX FIV THR FOR NIN FIV THR FOR THR SVN SVN ZRO NIN ONE FIV FOR ZRO ZRO SVN ONE TWO THR SVN SVN THR THR THR NIN ONE FIV EGT EGT EGT ZRO TWO FOR FOR THR THR SIX SVN SIX SIX ONE FOR EGT ONE SIX FIV NIN SIX EGT SVN ONE NIN ONE SIX SVN SIX THR SVN ONE TWO SVN NIN FOR SVN ONE EGT TWO FOR EGT EGT ONE SIX TWO ZRO FOR EGT FIV NIN FOR FOR FOR NIN NIN FOR FIV THR TWO ONE SVN FOR THR ONE NIN ZRO SVN THR EGT FOR TWO SIX NIN EGT SVN SVN FOR EGT SVN EGT THR TWO ONE NIN THR SVN FOR FOR FOR THR FIV ONE THR TWO EGT ZRO NIN ZRO THR FOR NIN FOR FOR THR NIN EGT FIV THR EGT ONE TWO THR EGT NIN EGT FIV ONE ZRO SIX ONE EGT ONE EGT SVN SVN TWO EGT TWO THR SIX SIX NIN SIX FIV ONE THR EGT ZRO SVN SIX ONE SIX ZRO THR ONE ZRO FOR THR ONE FIV EGT NIN FIV FOR FIV SVN FOR FOR SIX SVN SVN FIV TWO SIX EGT EGT NIN ONE NIN EGT ZRO FIV ZRO TWO NIN SIX ZRO TWO TWO NIN TWO SIX SVN THR SIX ZRO FIV TWO ONE SVN ONE ONE FIV THR TWO SIX SIX EGT ONE FIV EGT SIX NIN FOR SIX SIX TWO EGT EGT ONE SIX EGT SVN EGT NIN SVN NIN ZRO FIV EGT TWO SIX NIN SVN ONE SVN FIV ONE SIX FOR FOR NIN NIN SIX ONE FIV FIV SIX ZRO SVN FIV ZRO SVN NIN FIV SIX EGT FIV THR SVN ZRO SVN FIV TWO THR ZRO FOR NIN EGT FIV EGT ZRO ZRO NIN SVN SVN FOR FOR SVN FIV NIN TWO THR TWO TWO THR ONE NIN SVN THR ZRO FOR THR SVN EGT ZRO EGT EGT ONE TWO SVN FOR NIN ONE NIN THR SIX TWO ZRO SVN TWO ZRO ZRO FIV THR FIV SVN SVN FOR FOR THR THR EGT SIX FOR FOR FIV NIN TWO FOR FOR TWO FOR TWO FIV THR TWO THR FOR ZRO TWO THR SVN TWO ZRO SVN SVN SIX ONE SVN FIV SIX SVN NIN ZRO EGT FIV SVN FOR TWO FIV SIX FIV EGT EGT TWO EGT FIV TWO SVN SIX SVN THR THR FIV SIX NIN FOR FOR FIV NIN SIX NIN TWO NIN FIV SIX ONE SVN EGT THR SVN TWO SIX NIN ONE ZRO ZRO FOR FIV SIX THR SIX FOR SIX SVN SIX THR NIN ONE FOR SVN FIV ZRO ZRO FIV FIV EGT EGT SIX NIN EGT ONE FIV SIX ZRO SIX ZRO FOR SVN EGT SIX FOR ZRO THR FOR ONE ZRO ZRO FOR THR SIX ONE ZRO FIV SIX EGT SIX SVN SIX SVN EGT NIN FOR FIV ONE ZRO TWO EGT SIX SVN ZRO SVN SVN FOR SIX TWO TWO NIN SIX FIV SIX FOR ZRO SIX NIN SIX TWO NIN ONE TWO SIX FOR SVN ZRO EGT TWO FOR ONE ZRO ZRO THR SIX ONE SVN NIN EGT ZRO TWO NIN EGT NIN SVN FOR SVN SVN FIV THR NIN ONE TWO NIN SIX ONE ONE FOR NIN EGT SIX NIN SVN FOR EGT TWO FIV EGT TWO FIV SIX ONE NIN THR SVN ONE THR TWO ZRO SIX EGT NIN NIN THR NIN ONE ONE THR FOR EGT TWO FOR NIN ONE FOR THR NIN FOR NIN FIV TWO ONE SIX SVN TWO FIV ONE EGT ZRO SVN FIV SVN FOR TWO NIN ONE EGT FOR FOR EGT ONE TWO EGT FOR SIX SVN THR ONE FIV EGT FIV FOR TWO SIX SIX FOR SIX ONE FOR ZRO FOR SIX SIX SVN FIV EGT ONE ONE FIV ONE ONE NIN ZRO SVN SIX THR FOR FOR FIV SVN TWO SIX FIV SIX TWO NIN SIX FIV THR TWO ONE SIX THR FOR NIN ZRO FIV SIX FIV ZRO SIX FIV THR THR TWO SIX SIX ZRO SIX TWO ZRO ZRO FIV TWO ZRO FIV SIX ONE ZRO FOR NIN FOR ZRO TWO SIX SIX FOR ZRO SVN TWO SIX SIX EGT FIV ONE ZRO ZRO TWO ONE THR EGT FOR THR FIV ZRO EGT SVN ZRO FIV THR FIV SIX THR ZRO TWO NIN NIN THR SVN NIN THR NIN THR ZRO TWO FIV ONE ONE EGT THR THR SVN FOR SIX SVN ONE NIN FOR SIX ONE TWO EGT TWO FIV SVN SVN EGT FOR TWO ZRO SIX FIV ZRO FIV SIX ZRO SVN TWO FOR FOR FOR ZRO FIV ZRO SIX SIX TWO SIX THR ONE SVN FIV FIV FIV FOR EGT NIN NIN EGT ONE TWO SVN SVN NIN TWO ONE EGT TWO NIN SVN NIN NIN ZRO ZRO SIX FOR TWO FIV THR FIV ONE NIN SVN EGT FOR NIN ONE NIN EGT SVN NIN SIX NIN FIV SIX FOR SVN FOR FOR EGT SIX FIV ONE FOR NIN EGT EGT SVN THR FOR FIV SVN SVN FIV ONE THR THR SVN NIN SIX FIV THR FOR ZRO TWO FOR NIN EGT ZRO FOR TWO SIX ONE FIV SIX ONE ZRO FIV ZRO FOR EGT SVN ZRO EGT ONE SVN TWO EGT ZRO ONE ONE NIN ONE ZRO THR TWO THR TWO TWO EGT ONE EGT SVN FIV SIX TWO SIX FOR SVN FOR THR SVN ZRO FIV FOR THR SVN THR EGT ZRO FIV SIX EGT TWO SIX EGT ONE TWO SIX SIX TWO FOR THR ZRO TWO ZRO FIV ONE ZRO FIV EGT ZRO ONE THR EGT TWO EGT FOR FIV SVN TWO THR EGT NIN ONE SIX TWO TWO ONE THR EGT FIV SIX SIX EGT NIN THR FIV SVN SIX NIN FIV SVN SVN ZRO ZRO TWO FIV NIN THR ZRO THR SVN SIX ONE FIV TWO FIV NIN FIV THR FIV FIV THR SIX SIX EGT FIV TWO ONE ZRO TWO SIX EGT NIN SIX TWO FIV EGT EGT SIX SIX ONE SIX SVN ONE TWO FIV TWO FOR NIN TWO SVN ZRO ZRO FOR NIN ZRO EGT ONE ZRO ZRO ONE SVN THR FIV SIX NIN FIV ZRO SIX SIX TWO THR SIX SVN FIV TWO FIV SIX SIX SIX SVN EGT SIX FOR FIV FIV EGT ZRO ZRO FOR FOR TWO TWO EGT SIX FIV ZRO NIN NIN NIN THR EGT SVN ONE FIV ONE NIN NIN EGT FIV TWO THR ONE ZRO SVN THR EGT EGT FIV NIN SIX NIN THR ONE ONE NIN ONE TWO FOR SIX EGT ZRO EGT NIN FIV ZRO FOR SIX EGT SIX SVN THR THR ONE SVN THR ONE THR FOR TWO SVN SVN THR THR SIX FIV FIV THR SIX ZRO NIN FIV SIX THR THR TWO NIN NIN SIX THR FIV FIV ONE FOR SVN ONE SVN NIN NIN SIX FIV TWO TWO THR SVN ZRO NIN SVN SIX NIN FIV SIX NIN NIN THR FIV EGT ONE EGT NIN SIX ONE EGT FOR FIV THR FOR SIX FOR ONE FIV TWO ONE SVN FIV FOR EGT THR EGT FIV TWO THR ONE THR TWO ZRO ZRO ZRO EGT FIV TWO EGT EGT SVN ONE ZRO EGT SIX THR TWO TWO TWO SVN ZRO EGT FOR SVN FOR THR FOR FOR FOR SIX ZRO FIV FIV THR SVN TWO ONE NIN ZRO EGT EGT EGT ZRO NIN ONE SIX SVN EGT SIX FIV NIN EGT ZRO FIV FOR SIX SVN SIX FOR ZRO ONE EGT EGT FOR NIN FOR SIX FOR ZRO NIN TWO NIN ONE TWO FOR THR NIN NIN SVN SVN SIX SIX SVN NIN THR NIN FOR FIV FOR SIX NIN EGT SIX EGT TWO SIX SVN FIV EGT SIX EGT TWO FOR THR FIV SIX SIX TWO SIX FOR NIN TWO FOR TWO NIN SIX SIX TWO TWO FIV SIX FIV TWO NIN FIV SVN FOR FOR THR FOR NIN TWO ONE THR THR SVN THR THR ZRO FIV FOR FIV ONE TWO EGT FIV SIX ZRO ONE EGT NIN TWO SVN THR EGT FOR TWO SIX SVN SIX THR ZRO TWO NIN THR NIN NIN TWO TWO TWO NIN FOR NIN FOR EGT FOR SIX THR FOR TWO EGT THR THR SVN EGT THR SVN FIV NIN ONE FOR NIN ONE SVN SIX TWO FIV TWO TWO EGT SIX ONE FIV FIV NIN SIX TWO SIX EGT NIN ZRO SIX FOR ZRO SIX SIX THR FIV FOR ONE EGT EGT FOR FOR SVN THR TWO FOR THR TWO FIV ONE TWO FOR NIN FIV ZRO SIX EGT FIV FOR ONE NIN ONE NIN TWO THR TWO TWO TWO NIN ONE SVN FIV ZRO NIN NIN EGT NIN EGT ZRO ONE EGT ZRO SIX EGT FOR FIV FIV ZRO EGT SIX ZRO FIV FOR SIX TWO NIN THR TWO FIV SIX THR FIV SVN TWO EGT FIV FOR EGT NIN TWO EGT SIX EGT EGT EGT FIV NIN NIN FOR TWO NIN NIN EGT SVN EGT THR ONE THR ZRO SIX SIX THR FOR ZRO EGT THR SVN SIX SIX ZRO FIV TWO ZRO SVN THR SIX EGT SVN NIN FOR EGT ZRO EGT FIV SVN TWO FOR TWO NIN TWO ZRO ONE FIV ZRO ONE FOR ZRO ZRO FIV SVN FOR SVN SVN FIV TWO EGT THR FIV NIN SVN EGT NIN SIX ZRO NIN ZRO ONE NIN ONE SIX ZRO ONE FOR THR FOR SVN NIN SIX NIN ZRO SVN FIV FIV FOR NIN FOR TWO ZRO NIN SVN THR THR SVN SVN ZRO FIV THR ONE TWO SIX FOR TWO FOR SIX ZRO THR FIV TWO SVN ONE ONE FOR NIN SIX FIV NIN EGT SVN EGT FOR ZRO TWO NIN ZRO FIV EGT TWO SIX TWO NIN SIX NIN EGT THR NIN FIV SVN ZRO ONE TWO ZRO SVN SIX FIV SIX THR TWO EGT FIV FIV EGT EGT ZRO ONE NIN FOR FIV SIX SVN SVN ONE EGT THR SIX THR THR EGT THR FIV NIN SIX ONE ONE NIN FOR THR NIN ONE NIN TWO SIX ZRO SVN ZRO NIN THR EGT SVN THR ZRO EGT SIX EGT THR ZRO SIX EGT FIV THR NIN EGT SIX ZRO FIV SIX THR EGT NIN SIX ZRO FIV NIN NIN ONE SVN FIV FOR EGT EGT FOR ONE ONE SVN ZRO TWO FIV SIX EGT EGT ZRO FIV THR FOR THR SVN FIV SIX ZRO SIX ONE ZRO NIN EGT SVN NIN FIV THR SVN ONE ONE SVN THR ONE SIX NIN ONE FOR TWO SVN ZRO EGT SIX FOR NIN SVN ZRO ONE THR ONE ONE NIN NIN NIN FIV NIN THR FIV SIX ONE FOR THR NIN FIV FOR FIV FIV ZRO THR SVN TWO TWO FOR THR ZRO FIV EGT ZRO THR ZRO SIX FIV FOR ZRO EGT EGT FOR EGT ONE SVN SVN EGT ZRO NIN ZRO ZRO ZRO TWO ZRO FOR FIV FOR TWO ONE SIX EGT FOR SIX SIX SIX TWO EGT EGT FIV TWO SVN SIX NIN TWO ONE SIX ZRO SVN SIX ZRO ZRO FIV FIV EGT FOR FOR THR NIN SIX THR SIX EGT FOR ONE ONE FIV FIV FOR TWO NIN TWO FOR ZRO FIV SVN SIX ZRO FOR FOR SVN FIV FIV NIN ONE EGT FOR FOR SIX FIV ONE ZRO FOR NIN NIN FIV EGT SVN FIV FOR EGT SIX ZRO TWO SIX TWO SVN THR ONE FIV NIN FIV NIN EGT NIN SVN FOR ZRO EGT FOR SVN TWO ZRO EGT EGT SIX ZRO TWO THR NIN ONE THR SVN NIN THR THR ONE TWO FIV SIX TWO ZRO SIX ONE SVN SVN ZRO FIV SIX ONE TWO TWO SIX ONE ZRO FIV FIV THR THR ONE TWO FIV SVN TWO ONE SVN ONE TWO TWO EGT ZRO NIN FOR NIN THR ONE FOR ONE FOR THR ZRO FOR EGT SVN THR TWO EGT TWO THR NIN EGT FIV ZRO EGT THR FIV ONE FIV EGT THR SVN ONE SIX ZRO NIN ZRO FIV THR ONE FOR TWO ZRO ONE FIV NIN ZRO FOR TWO SIX ZRO FIV TWO FOR TWO THR EGT FIV ZRO FIV THR TWO NIN SVN THR SVN FOR NIN EGT EGT EGT ZRO NIN SVN THR ZRO SVN SIX ONE TWO FOR TWO EGT SIX THR NIN EGT THR FIV ONE ZRO NIN SIX TWO FIV FOR EGT FIV THR ONE SVN ZRO EGT ZRO FOR SIX NIN SIX EGT FIV TWO TWO TWO ONE SVN EGT FIV NIN NIN TWO NIN SIX NIN FIV ZRO SIX TWO FIV TWO THR ONE SIX ONE ZRO TWO TWO ONE ZRO THR FIV FIV ZRO ZRO EGT ZRO ONE SIX FOR FOR NIN ZRO NIN TWO FIV ONE FOR ZRO TWO ONE FIV ONE SIX THR ZRO EGT TWO FIV SIX FOR TWO FOR FIV TWO ONE ONE FIV ZRO FIV ONE SVN TWO THR SVN THR ZRO NIN EGT FOR FOR NIN FIV ZRO FIV ONE TWO FOR ZRO SIX ZRO ONE NIN NIN THR SVN ZRO FIV SIX ZRO EGT FIV SVN NIN ONE ZRO TWO SIX NIN ZRO NIN FIV NIN NIN ONE ONE FOR SVN FIV ONE THR NIN EGT FOR THR FOR FOR ZRO ONE SVN FOR ONE SVN FIV ZRO NIN FIV EGT ONE TWO SVN ZRO NIN SIX SVN EGT EGT FOR EGT FIV ONE THR FIV ONE FOR SVN TWO FOR SIX FOR EGT ONE FOR EGT SIX SIX SIX ZRO NIN SVN NIN NIN THR FOR ONE FOR ZRO SVN SIX TWO TWO EGT SIX TWO THR EGT NIN THR SVN THR SVN SIX FOR ONE THR ZRO THR TWO ZRO TWO THR FOR THR SVN FIV TWO ZRO SVN SIX ZRO EGT SIX EGT NIN FOR THR NIN THR THR ZRO ZRO SVN ZRO SVN TWO THR SVN THR ONE FIV NIN ONE EGT ONE EGT THR EGT EGT EGT FOR SVN TWO ONE TWO SIX SVN ZRO EGT THR FOR ONE NIN TWO TWO ONE ONE THR FIV ONE ONE ZRO EGT ONE TWO FOR FOR FIV ZRO FIV FIV THR ZRO EGT NIN ZRO SVN TWO EGT ZRO FIV NIN EGT NIN ONE ONE FIV THR SVN NIN ZRO SVN FOR FOR SVN TWO ONE FOR SIX TWO SVN ONE ONE TWO FIV EGT FIV EGT FOR SIX EGT FIV EGT FIV NIN SVN TWO ONE NIN SVN TWO THR FIV TWO SVN NIN SIX FIV TWO EGT THR FIV SVN THR FIV NIN SVN NIN ONE ZRO THR EGT TWO EGT SIX ONE FIV SIX NIN ONE EGT NIN TWO NIN EGT EGT FOR TWO EGT SIX ONE SVN THR ONE FOR NIN SVN FIV NIN EGT ONE FIV FIV TWO TWO SIX SVN THR SVN NIN FOR SVN TWO FOR NIN THR SVN FOR TWO ONE NIN SIX SVN NIN NIN FOR SIX TWO SVN SVN THR ONE TWO NIN SVN ONE TWO SIX SIX THR SVN FOR TWO TWO FIV SIX FOR ONE FIV THR TWO THR TWO NIN TWO NIN SVN NIN FIV NIN FOR TWO NIN ZRO TWO FIV THR ONE NIN ZRO FOR SVN FIV NIN ZRO EGT EGT TWO EGT FIV FOR FOR ONE FOR SVN FIV NIN ONE FOR NIN ZRO SIX ZRO SVN THR ONE ONE EGT SIX ZRO THR ONE SIX EGT FOR ONE FIV TWO SIX ZRO FOR THR ZRO SIX NIN FIV SIX THR FIV TWO EGT FIV ZRO SIX FIV SIX FOR TWO TWO FIV FIV SIX ONE THR SIX ZRO THR ZRO ONE FOR THR SVN ZRO NIN TWO FIV TWO TWO EGT FOR TWO EGT FIV EGT TWO SVN TWO TWO ZRO THR NIN ONE ZRO ONE FIV FOR FOR FIV NIN NIN TWO SIX NIN ZRO THR FIV SIX EGT EGT NIN FIV SIX NIN ONE FOR TWO ZRO SVN EGT SVN EGT ONE EGT THR THR FIV ONE SVN TWO FIV ONE FIV EGT TWO FOR ZRO EGT ONE FIV THR THR FIV EGT FIV SVN NIN NIN TWO FOR FOR ONE SIX NIN TWO SIX EGT FIV TWO ZRO ONE TWO EGT TWO NIN SVN SIX EGT EGT SVN EGT FIV FOR FIV NIN ONE ZRO ZRO SIX ONE EGT SVN ONE SVN ONE ZRO SVN SVN NIN THR SIX ZRO THR FOR FOR NIN SIX FIV NIN EGT ZRO THR EGT SIX FOR THR ONE FOR THR ONE TWO ZRO SVN FOR EGT FOR NIN THR NIN SVN ONE FIV SVN THR TWO EGT FIV NIN SVN NIN THR SVN FIV ZRO ONE NIN EGT FOR SIX TWO ONE THR NIN ZRO SVN TWO EGT ZRO NIN TWO ZRO NIN FOR TWO ZRO SIX SIX FOR SIX ONE THR SIX FOR FIV EGT NIN SVN FOR FOR ONE SIX SVN FIV FOR ZRO TWO THR THR TWO TWO THR NIN EGT NIN THR NIN SVN FIV FIV TWO NIN FIV EGT NIN SVN ZRO FOR ONE ZRO THR EGT TWO SVN THR TWO THR FIV SIX ZRO SVN TWO NIN SIX SIX FOR TWO SVN FIV NIN SIX ZRO SVN SIX ONE FIV ZRO TWO FIV SVN EGT FOR ONE NIN TWO FIV TWO NIN THR ZRO TWO TWO SIX ZRO NIN TWO FIV ONE SIX FIV FOR SVN FOR NIN TWO ONE NIN SVN ONE SIX FOR THR ONE SVN FIV FIV FIV TWO NIN ZRO EGT THR NIN NIN TWO FOR FOR TWO FIV FIV THR SIX TWO EGT FOR ONE TWO SIX SIX NIN ONE FOR THR FOR SIX EGT FOR THR EGT FOR SVN FOR SIX FOR SIX SIX THR EGT ZRO SIX ONE ONE SIX NIN ZRO FIV EGT ONE ONE ONE FIV EGT THR FOR NIN ZRO EGT ONE NIN THR EGT SVN FOR SVN ZRO SVN SIX THR NIN TWO SIX NIN EGT NIN FIV ONE SVN ZRO ZRO SVN ONE TWO SIX NIN FOR THR ZRO TWO TWO TWO THR THR THR ONE ZRO TWO THR ZRO NIN NIN TWO SIX FIV SIX SIX THR FOR EGT EGT EGT EGT THR FIV ONE THR SVN THR SVN FOR ZRO SIX ONE NIN FOR SIX TWO FOR THR ZRO ONE THR FIV EGT THR SVN FOR SVN ONE TWO THR NIN ZRO EGT TWO EGT SIX ZRO SVN EGT ONE SIX FIV ONE FOR ZRO FIV SVN NIN ZRO FIV THR NIN FOR EGT FOR THR EGT EGT ZRO SVN FOR THR THR TWO ZRO EGT SIX FOR SIX NIN SVN SVN SVN NIN TWO FIV FIV SIX SVN SIX FOR FIV ZRO SIX TWO FIV THR SIX SIX EGT SIX THR FOR NIN ONE FIV FOR FOR FOR THR NIN SIX SVN FOR SVN SIX THR FOR TWO ONE NIN FIV NIN SIX ONE ONE EGT THR SIX ZRO SIX NIN ZRO NIN FOR SIX NIN THR SIX ONE THR SIX THR ZRO SVN FIV TWO SVN NIN FIV THR THR ONE SIX NIN FIV EGT THR EGT SVN ONE ONE FOR THR FIV SVN ZRO ONE SVN EGT SIX FIV ONE SIX NIN NIN ONE ONE TWO NIN FIV THR ZRO FOR SIX THR TWO EGT NIN FIV ZRO ZRO EGT ONE EGT FIV SVN ZRO FOR SVN FOR THR FOR TWO FIV FOR ZRO TWO FOR NIN FOR SIX THR EGT EGT NIN ONE NIN THR TWO ZRO SIX ZRO EGT EGT ZRO THR ONE TWO FOR NIN FIV FIV TWO NIN EGT TWO NIN ZRO ZRO SIX SVN FOR TWO SIX THR FOR THR SIX ONE ONE FOR ONE TWO NIN TWO SIX ZRO NIN EGT NIN FIV TWO ZRO SVN FOR ZRO NIN TWO FIV THR FIV EGT TWO FOR SIX EGT THR ONE SVN EGT SVN TWO FIV ZRO EGT FIV THR ZRO SIX ONE NIN FIV ONE SVN FOR ZRO THR NIN ZRO EGT THR ZRO EGT ONE FOR THR FOR TWO SIX FOR SIX FIV FOR EGT TWO ZRO NIN EGT TWO ONE FOR ZRO SIX TWO FOR TWO ZRO SIX SIX SIX TWO SVN ONE ONE NIN SVN TWO FIV ONE THR ZRO EGT NIN EGT FOR ONE SIX SIX SVN ONE ZRO TWO EGT THR THR ONE TWO SIX THR ONE FIV FOR FIV THR FOR FOR SVN THR FOR THR TWO ONE FOR ZRO SVN EGT NIN SVN ZRO THR ONE THR SIX ONE ZRO EGT THR THR ONE THR TWO ONE FOR NIN SIX TWO FOR NIN TWO TWO ONE NIN ZRO ZRO NIN FIV TWO FIV ONE SVN ONE THR ONE SIX FIV THR ZRO THR FOR TWO FOR THR SIX TWO FIV NIN THR SVN SIX THR NIN ONE ZRO FIV EGT ONE NIN ZRO FIV FOR EGT EGT FOR EGT THR EGT SVN FIV ZRO TWO FIV ZRO ONE FIV TWO FOR SIX TWO FOR FIV FIV FOR NIN FOR NIN TWO NIN SIX NIN ONE THR ZRO SIX TWO THR THR NIN ZRO FIV SVN ZRO NIN NIN ZRO ONE SVN NIN THR FOR ONE FIV FIV THR FOR NIN SVN FIV FOR EGT ONE THR SIX THR SVN ONE FIV ONE ONE ZRO TWO FIV ZRO ONE ZRO SVN THR FOR THR ONE ONE EGT SVN NIN ZRO FIV NIN TWO ONE TWO ZRO THR FOR SVN ZRO ZRO ONE EGT THR ONE ONE EGT EGT THR THR FIV NIN TWO EGT THR FOR FIV NIN ZRO SIX TWO FOR FIV NIN EGT FIV ONE EGT SVN SIX SVN FIV NIN FOR THR ONE ZRO FIV FOR SIX ZRO EGT ONE ONE SVN FOR FOR FIV FOR TWO NIN ZRO SVN NIN FOR SVN ZRO FIV SIX FOR NIN TWO FIV FIV ONE TWO ONE FOR THR THR TWO ONE NIN FOR NIN THR FIV FIV ZRO SIX ONE SVN THR ONE SIX TWO ZRO FOR SIX EGT TWO NIN SIX EGT ONE NIN SIX THR NIN EGT SVN FIV THR ZRO ZRO FIV FOR ONE THR FIV SVN THR SVN EGT FOR TWO EGT ZRO FOR ONE SIX FIV EGT THR SVN TWO ONE NIN SVN ONE TWO ONE ONE TWO ONE THR FIV SIX ZRO ONE FIV THR ZRO EGT FIV THR TWO TWO SIX SVN NIN TWO NIN SIX ONE TWO ONE ZRO ZRO EGT ZRO ZRO FIV NIN EGT ONE TWO FOR THR ZRO TWO ZRO ZRO FOR ONE NIN SIX FIV THR NIN SVN FOR EGT NIN FOR ZRO EGT SVN SVN FIV SIX ZRO THR EGT ZRO NIN FOR NIN THR FIV FOR SVN EGT SIX ONE FOR SVN THR NIN SVN ZRO FIV FOR FOR SIX FIV EGT FOR SVN EGT SVN FIV TWO ONE SVN SVN SIX NIN FOR NIN THR ONE ONE FOR NIN FIV FIV ZRO TWO THR NIN SIX NIN 
'''