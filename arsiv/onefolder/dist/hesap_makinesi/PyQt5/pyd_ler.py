import glob

pydfiles = []
for file in glob.glob("*.pyd"):
    pydfiles.append(file)

pyd_list = open("pyd_ler.txt", "w", encoding="UTF-8")
for i in pydfiles:
    pyd_list.write(f"'{i}', ")
pyd_list.close()