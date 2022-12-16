print("введите команду: ")
print("кондамы: add, del, view, DELindex, vs")
spisok = ["poko", "shelly", "leon", "el primo, red"]
com = input("команда: ")
if com == "add":
    a = input("наклацайте слово:")
    spisok.append(a)
    print(spisok)
elif com == "del":
    a = input("наклацайте удаляемое слово:")
    spisok.remove(a)
elif com == "DELindex":
    a = int(input("наклацайте индекс удаляемоего слова:"))
    del spisok[a]
    print(spisok)
elif com == "view":
    a = int(input("наклацайте индекс слова:"))
    print(spisok[a])
elif com == "vs":
    print(spisok)
elif com == "red":
    a = int(input("наклацайте индекс слова:"))
    spisok[a]=input("слово списка: ")
    print(spisok)