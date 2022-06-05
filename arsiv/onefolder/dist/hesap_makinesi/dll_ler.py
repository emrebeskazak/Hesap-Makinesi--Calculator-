import glob

dllfiles = []
for file in glob.glob("*.dll"):
    dllfiles.append(file)

dll_list = open("dll_ler.txt", "w", encoding="UTF-8")
for i in dllfiles:
    dll_list.write(f"'{i}', ")
dll_list.close()