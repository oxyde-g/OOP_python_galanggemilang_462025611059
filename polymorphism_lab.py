# # tidak pakai polymorphism

# class Pemainbola:
#     def __init__(self, nama: str):
#         self.nama = nama

# class coach:
#     def __init__(self,nama: str):
#         self.nama = nama

# class official:
#     def __init__(self, nama: str):
#         self.nama = nama


# def contoh_tanpa_poly(pemainbola):

#     if isinstance(pemainbola, coach):
#         print(f"coach {pemainbola.nama} lagi melatih pemain bola")
#     elif isinstance(pemainbola, official):
#         print(f"official {pemainbola.nama} sedang mengatur strategy bersama coach")
#     elif isinstance(pemainbola, Pemainbola):
#         print(f"pemain {pemainbola.nama} sedang berlatih main bola ")
#     else:
#         print("ini NPC sok asik")

# pemain_elgocek = Pemainbola("neymar")
# abang_coach = coach("bang pep")
# si_official = official("si dodo")

# print(" --simulasikan main bola (tanpa polymorphism) --")
# contoh_tanpa_poly(pemain_elgocek)
# contoh_tanpa_poly(abang_coach)
# contoh_tanpa_poly(si_official)

# contoh yang pake polymorpishm

class pemainbola:
    def __init__(self, nama: str):
        self.nama = nama

    def maenbola(self):
        print(f"{self.nama} sedang mengotak atik lapangan hijau")

class coach(pemainbola):
    def maenbola(self):
        print(f"{self.nama} lagi teriak2 buat ngarahin si pemain yang ngotak atik")

class official(pemainbola):
    def maenbola(self):
        print(f"{self.nama} lagi bantuin teriak2 si pelatih tadi, kandesa ngk pake dolar")

def otakatik_lapangan(pemainbola):
    pemainbola.maenbola()


pemain_elgocek = pemainbola("neymar")
abang_coach = coach("bang pep guardiola")
si_official = official("si pranowo")


print (" ---- kita nonton maennya si wowo -----")
otakatik_lapangan(pemain_elgocek)
otakatik_lapangan(abang_coach)
otakatik_lapangan(si_official)


