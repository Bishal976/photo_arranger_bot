
import os


def extract(t):
    om = t.split("_")
    return om[1]


def photo_arranger(paath):
    os.chdir(paath)
    lst = os.listdir()
    places = []
    for i in lst:
        place = extract(i)
        if place not in places:
            places.append(place)
    for j in places:
        os.mkdir(j)
    for k in places:
        for l in lst:
            if extract(l) == k:
                os.rename(l, os.path.join(k, l))



                
#     print("i am bishal")
# if __name__ == "__main__":
#     photo_arranger(input("input the path:\n"))
# print("bishal")
print("TEST 1")

# if __name__ == '__main__':
#     print("TEST 2")
#
# if __name__ == 'photo_arranger':
#     print("TEST 3")