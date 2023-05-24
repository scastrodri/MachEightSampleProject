import itertools

def pairs(a_list, a_sum):

    pairs_list = list(itertools.combinations(a_list,2))
    for pair in pairs_list:
        try:
            if (int(pair[0]) + int(pair[1])) == a_sum:
                print(pair[0],pair[1])
        except:
            pass

a_list, a_sum = input("Please enter a list of numbers seprate by a ',' and a value sum desired separtae by space: \n").split()
pairs(a_list.split(','), int(a_sum))