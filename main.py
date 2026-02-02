


def main():
    with open("version.txt","r") as f:
        ver = f.readline()
    with open("version.txt","w") as f:
        print(ver)
        if len(ver) == 0:
            new_ver = input("Add meg a jelenlegi verziót amit le szeretnél tölteni\n: ")
            f.writelines(new_ver)
        else:
            update_text(ver=ver)
    
def update_text(ver):
    with open("version.txt", "w") as f:
        inp1 = input(f"A verziószám a következőre módosul: {ver[:-3]}{int(ver[4:])+1}\nElfogadod: I/n: ").upper()
        if inp1 == "N":
            full_new_ver = input("Add meg a teljes verziót: 0.0.122: ")
            f.write(full_new_ver)
        elif inp1 == "I" or inp1 == "":
            f.write(f"{ver[:-3]}{int(ver[4:])+1}")
            print("A módosítás sikeres!")

        print(inp1)
if __name__ == "__main__":
    main()