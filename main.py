# Search engine program.

from time import time
import parser_p as p
import trie as t
import graph as g
import os
import msort

number = 10

def find_path(word, address, graf, j):

    word = word.lower()

    ranking = {}
    sol = j.search(word)
    ranking, firstapp = calcrng(sol, ranking, graf)
    # print(graf.vertex_count())
    # print(graf.edge_count())
    # print("cao")
    # print(sol)
    if ranking:
        calc(ranking, firstapp)
    else:
        print("No results to show. ")


def op_and(wrd1, wrd2, address, graf, j):

    wrd1 = wrd1.lower()
    wrd2 = wrd2.lower()

    # print(graf.vertex_count())
    # print(graf.edge_count())
    # print("cao")
    ranking = {}
    ranking1 = {}
    sol = j.search(wrd1)
    sol2 = j.search(wrd2)

    ranking, firstapp = calcrng(sol, ranking, graf)

    # print("#"*300)
    # print("#" * 300)
    # print("#" * 300)

    ranking1, firstapp1 = calcrng(sol2, ranking1, graf)


    if ranking:
        if ranking1:
            temprang = {}
            for i in ranking:
                for j in ranking1:
                    if i == j:
                        temprang[i] = (ranking[i] + ranking1[j]) * 3
            calc(temprang, firstapp)
        else:
            calc(ranking, firstapp)
    else:
        if ranking1:
            calc(ranking1, firstapp1)
        else:
            print("No results to show. ")
            print(f"There is no file which contains both {wrd1} and {wrd2}")


def op_or(wrd1, wrd2, address, graf, j):

    wrd1 = wrd1.lower()
    wrd2 = wrd2.lower()

    # print("cao")
    ranking = {}
    ranking1 = {}
    sol = j.search(wrd1)
    sol2 = j.search(wrd2)

    ranking, firstapp = calcrng(sol, ranking, graf)

    # print("#" * 300)
    # print("#" * 300)
    # print("#" * 300)

    ranking1, firstapp1 = calcrng(sol2, ranking1, graf)

    temp_o = 0
    if ranking:
        if ranking1:
            temprang = {}
            for i in ranking:
                if i not in temprang:
                    temprang[i] = ranking[i]
                for j in ranking1:
                    if i == j:
                        temprang[i] = (ranking[i] + ranking1[j]) * 5
                    if j not in temprang:
                        temprang[j] = ranking1[j]
            calc(temprang, firstapp)
        else:
            temprang = ranking
            calc(ranking, firstapp)
    else:
        if ranking1:
            temprang = ranking1
            calc(ranking1, firstapp1)
        else:
            print("No results to show. ")
            print(f"There is no file which contains both {wrd1} and {wrd2}")
            temprang = {}

    return temprang, firstapp


def op_ortemp(wrd1, wrd2, address, graf, j):

    wrd1 = wrd1.lower()
    wrd2 = wrd2.lower()

    # print("cao")
    ranking = {}
    ranking1 = {}
    sol = j.search(wrd1)
    sol2 = j.search(wrd2)

    ranking, firstapp = calcrng(sol, ranking, graf)

    # print("#" * 300)
    # print("#" * 300)
    # print("#" * 300)

    ranking1, firstapp1 = calcrng(sol2, ranking1, graf)

    temp_o = 0
    if ranking:
        if ranking1:
            temprang = {}
            for i in ranking:
                if i not in temprang:
                    temprang[i] = ranking[i]
                for j in ranking1:
                    if i == j:
                        temprang[i] = (ranking[i] + ranking1[j]) * 5
                    if j not in temprang:
                        temprang[j] = ranking1[j]
            # calc(temprang, firstapp)
        else:
            temprang = ranking
            calc(ranking, firstapp)
    else:
        if ranking1:
            temprang = ranking1
            calc(ranking1, firstapp1)
        else:
            print("No results to show. ")
            print(f"There is no file which contains both {wrd1} and {wrd2}")
            temprang = {}

    return temprang, firstapp
def op_not(wrd1, wrd2, address, graf, j):

    wrd1 = wrd1.lower()
    wrd2 = wrd2.lower()
    # print("cao")
    ranking = {}
    ranking1 = {}
    sol = j.search(wrd1)
    sol2 = j.search(wrd2)

    ranking, firstapp = calcrng(sol, ranking, graf)
    ranking1, firstapp1 = calcrng(sol2, ranking1, graf)

    temp_o = 0
    if ranking:
        if ranking1:
            temprang = {}
            for i in ranking:
                temprang[i] = ranking[i]
                for j in ranking1:
                    if j in temprang:
                        del temprang[j]
            calc(temprang, firstapp)
        else:
            calc(ranking, firstapp)
    else:
        print("No results to show. ")
        print(f"There is no file which contains {wrd1} but not {wrd2}")


def look(address, graf, j):

    temp = 0
    for root, dirs, files in os.walk(address):
        for name in files:
            root = root.replace('\\', "/")
            temp_put = root + '/' + name
            temp_put = temp_put.replace('\\', "/")
            if os.path.isdir(temp_put):
                nesto = temp_put
                find_path(nesto)
            else:
                if not temp_put.startswith('.'):
                    if temp_put.endswith('.html'):
                        temp += 1
                        if not isinstance(temp_put, graf.Vertex):
                            a = graf.insert_vertex(temp_put)
                            pars = p.Parser()
                            pars.parse(temp_put)
                            cnt = 0
                            for i in pars.words:
                                j.insert(i.lower(), temp_put, cnt)
                                cnt += 1
                            for i in pars.links:
                                i = i.replace('\\', "/")
                                if not i.startswith('.'):
                                    if i.endswith('.html'):
                                        c = i
                                        if not isinstance(i, graf.Vertex):
                                            c = graf.insert_vertex(i)
                                        graf.insert_edge(a, c)
                        else:
                            continue

    if not temp:
        print("There is no .html files in this dict. ")
        print("Try again. ")

    return temp


def op_or1(wrd1, tempRec, j, graf):

    wrd1 = wrd1.lower()
    ranking = {}
    sol = j.search(wrd1)
    ranking, firstapp = calcrng(sol, ranking, graf)

    temp_o = 0
    if ranking:
        if tempRec:
            temprang = {}
            for i in ranking:
                if i not in temprang:
                    temprang[i] = ranking[i]
                for j in tempRec:
                    if i == j:
                        temprang[i] = (ranking[i] + tempRec[j]) * 5
                    if j not in temprang:
                        temprang[j] = tempRec[j]
        else:
            temprang = ranking
            calc(ranking, firstapp)
    else:
        if tempRec:
            temprang = tempRec
            calc(tempRec, firstapp)
        else:
            print("No results to show. ")
            temprang = {}

    return temprang, firstapp


def mult_or(arr, i, graf, j):

    sol, first = op_ortemp(arr[0], arr[1], i, graf, j)
    for i in range(len(arr) - 2):
        sol, first = op_or1(arr[i + 2], sol, j, graf)

    calc(sol, first)

def calcrng(sol, ranking, graf):

    firstapp = None
    if sol:
        for i, h in sol.items():
            if h:
                firstapp = h[0]
            else:
                firstapp = None
            ranking[i] = len(h) * 10
            cao = graf.get_incom_vert(i)
            if cao:
                for j in cao:
                    if i == j.element():
                        for k in graf._incoming[j]:
                            if k.element() in sol:
                                if k.element() in ranking:
                                    ranking[k.element()] += len(sol[k.element()]) * 5
                                else:
                                    ranking[k.element()] = len(sol[k.element()]) * 5

    if sol:
        for i in sol:
            cao = graf.vertices()
            if cao:
                for j in cao:
                    if i == j.element():
                        for k in graf._outgoing[j]:
                            if k.element() in sol:
                                if k.element() in ranking:
                                    ranking[k.element()] += len(sol[k.element()]) * 2
                                else:
                                    ranking[k.element()] = len(sol[k.element()]) * 2

    return ranking, firstapp


def calc(temprang, firstapp):

    global number
    sth = []
    if temprang:
        listkey = list(temprang.keys())
        listval = list(temprang.values())
        listval = msort.sort(listval)
        listval.reverse()
        print("-" * 100)
        tempic = 0
        for i in listval:
            if tempic > number - 1:
                break
            if temprang:
                for j in temprang:
                    if temprang[j] == i:
                        if j not in sth:
                            sth.append(j)
                            print(str(tempic + 1) + ". " +  j + ": " + str(temprang[j]))
                            if tempic == 0:
                                if firstapp:
                                    first_part(j, firstapp)
                            tempic += 1


def calcrngfrase(sol, ranking, graf):

    if sol:
        for i, h in sol.items():
            ranking[i] = h * 10
            cao = graf.get_incom_vert(i)
            if cao:
                for j in cao:
                    if i == j.element():
                        for k in graf._incoming[j]:
                            if k.element() in sol:
                                if k.element() in ranking:
                                    ranking[k.element()] += sol[k.element()] * 5
                                else:
                                    ranking[k.element()] = sol[k.element()] * 5

    if sol:
        for i in sol:
            cao = graf.vertices()
            if cao:
                for j in cao:
                    if i == j.element():
                        for k in graf._outgoing[j]:
                            if k.element() in sol:
                                if k.element() in ranking:
                                    ranking[k.element()] += sol[k.element()]  * 2
                                else:
                                    ranking[k.element()] = sol[k.element()]  * 2

    return ranking


def check_val(arr1, arr2):

    temp = []
    if arr1 and arr2:
        for i in arr1:
            for j in arr2:
                if j == i + 1:
                    temp.append(i)
                    temp.append(j)
        return temp
    else:
        return 0


def add_check(arr1, arr2):

    for i in arr1:
        for j in arr2:
            if i not in arr2:
                arr2.append(i)

    return arr2


def frase(listword, adr, graf, j):

    nesto = {}
    tempniz = {}
    rezniz = {}
    rez = {}
    for i in listword:
        i = i.lower()
        rez[i] = j.search(i)
    if rez:
        for q, i in rez.items():
            if i:
                for j, k in i.items():
                    if j not in nesto:
                        nesto[j] = 0
                    else:
                        pass
    if rez:
        for q,i in rez.items():
            if i:
                for j, k in i.items():
                    if j in tempniz:
                        sol = check_val(tempniz[j], k)
                        if sol:
                            if nesto[j] > 0:
                                tempniz[j] = add_check(sol, tempniz[j])
                                rezniz[j] = add_check(sol, tempniz[j])
                            else:
                                tempniz[j] = sol
                                rezniz[j] = sol
                            nesto[j] += 1
                    else:
                        tempniz[j] = k


    ranking = {}
    if rezniz:
        srez = {}
        for i in rezniz:
            if nesto[i] == len(listword) - 1:
                if rezniz[i]:
                    first = rezniz[i][0]
                srez[i] = len(rezniz[i]) // len(listword) * 10
        ranking = calcrngfrase(srez, ranking, graf)
    if ranking:
        calc(ranking, first)
    else:
        print("No results to show. ")


def first_part(address, inx):

    parss = p.Parser()
    parss.parse(address)
    if inx - 10 < 0:
        left = 0
    else:
        left = inx - 10
    if inx + 10 > len(parss.words):
        right = len(parss.words) - 1
    else:
        right = inx + 10
    print("-" * 100)
    for i in range(left, right):
        print(parss.words[i].upper(),end=' ')
    print('\n')
    print("-"*100)

def inp_sear(adr, graf, j):

    a = input("Insert word/words you want to search: ")
    a = a.lower()
    if len(a.split(' ')) == 1:
        find_path(a, adr, graf, j)
        return
    elif len(a.split(' ')) == 3 and a.split(' ')[1] == "and":
        op_and(a.split(' ')[0], a.split(' ')[2], adr, graf, j)
        return
    elif len(a.split(' ')) == 3 and a.split(' ')[1] == "or":
        op_or(a.split(' ')[0], a.split(' ')[2], adr, graf, j)
        return
    elif len(a.split(' ')) == 3 and a.split(' ')[1] == "not":
        op_not(a.split(' ')[0], a.split(' ')[2], adr, graf, j)
        return
    else:
        mult_or(a.split(' '), adr, graf, j)
        return


def inp_sear1(adr, graf, j):

    a = input("Insert frase you want to search: ")
    a = a.lower()
    frase(a.split(' '), adr, graf, j)
    return

def change_path():
    
    graf = g.Graph()
    j = t.Trie()
    while True:    
        inp = input("Input path: ")
        inp = inp.replace('\\', "/")
        if os.path.isdir(inp):
            a = time()
            if look(inp, graf, j):
                b = time()
                print("Elapsed time: ", b - a)
                break
            else:
                continue
        print("Unvalid path. ")

    return inp, graf, j


def inp_num():

    while True:

        a = input("Inser number of results you want: ")
        try:
            a = int(a)
            if a > 0:
                break
        except:
            print("Unvalid input. ")
            print("Try again. ")

    return a


def menu1(add, graf, j):

    global number
    poss = ['1', '2', '3', '4', 'x', 'X']
    while True:
        print("#"*30)
        print("Menu: ")
        print("#" * 30)
        print("1. Search. ")
        print("2. Change path. ")
        print("3. Frase search. ")
        print("4. Changing the number of results. ")
        print("x. Exit. ")
        print("#" * 30)
        option = input("Input your option: ")
        if option not in poss:
            print("Unvalid option. ")
            continue
        if option == '1':
            inp_sear(add, graf, j)
        if option == "2":
            add, graf, j = change_path()
        if option == '3':
            inp_sear1(add, graf, j)
        if option == "4":
            number = inp_num()
        if option == 'x' or option == "X":
            break

    print("End of search. ")
    quit()


def main():


    poss = ['1', 'x', 'X']
    while True:
        print("#" * 30)
        print("Menu: ")
        print("#" * 30)
        print("1. Insert path. ")
        print("x. Exit. ")
        print("#" * 30)
        option = input("Input your option: ")
        if option not in poss:
            print("Unvalid option. ")
            continue
        if option == '1':
            add, graf, j = change_path()
            menu1(add, graf, j)
        if option == 'x' or option == "X":
            break

    print("End of program. ")
    quit()
    

if __name__ == '__main__':
    main()

