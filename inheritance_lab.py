#ini yang simpel 
# class Minuman:
    # def __init__(self, nama, jenis):
        # self.nama = nama
        # self.jenis = jenis

    # def info(self):
        # print(f"Nama muniman ini adalah {self.nama} dan dengan jenis {self.jenis}")

# class mineral(Minuman):
    # def kebanyakan_gula(self):
        # print(f"Minuman dengan nama {self.nama} tidak ada gula tapi ada manis-manis nya")

# class soda(Minuman):
    # def kebanyakan_gula(self):
        # print(f"Minuman dengan nama {self.nama} itu kebanyakan gula")

# soda1 = soda("Cocacola", "soda")
# soda1.info()
# soda1.kebanyakan_gula()

# mineral1 = mineral("Le minerale", "air putih")
# mineral1.info()
# mineral1.kebanyakan_gula()

# 
#ini yang penggunaan super()
# 
# class Minuman:
    # def __init__(self, nama, jenis):
        # self.nama = nama
        # self.jenis = jenis
# 
    # def info(self):
        # print(f"nama minuman ini adalah {self.nama} dan dengan jenis{self.jenis}")
# 
    # def kebanyakan_gula(self):
        # print(f"ini di print dari class minuman")
# 
# class mineral(Minuman):
    # def kebanyakan_gula(self):
        # print(f"ini di print dari class mineral")
# 
    # def dari_parent(self):
        # super().kebanyakan_gula()
        # 
# class soda(Minuman):
    # def kebanyakan_gula(self):
        # print(f"ini di print dari class soda")
# 
    # def dari_parent(self):
        # super().kebanyakan_gula()
# 
# soda1 = soda("cocacola", "soda")
# soda1.info()
# soda1.kebanyakan_gula()
# soda1.dari_parent()
# 
# mineral1 = mineral("Aqua", "air gunung")
# mineral1.info()
# mineral1.kebanyakan_gula()
# mineral1.dari_parent()
# 
# 
# ini penggunaan multilevel inhirate

# class Minuman:
    # def __init__(self, nama, jenis):
        # self.nama = nama
        # self.jenis = jenis
# 
    # def info(self):
        # print(f"nama minuman ini adalah {self.nama}dan jenis nya adalah{self.jenis}")
# 
# class Mineral(Minuman):
    # def Kebanyakan_gula(self):
        # print(f"nama Minuman ini adalah {self.nama}dan jenis nya adalah{self.jenis}")
#
# class soda(Minuman):
    # def Kebanyakan_gula(self):
        # print(f"nama Minuman ini adalah {self.nama} dan jenis nya adalah {self.jenis}")
# 
# class tebskeras(soda):
    # def info_soda(self):
        # print(f"minuman soda dengan  jenis nya {self.jenis}")
# 
# soda_keras1 = tebskeras("teh soda", "seger")
# soda_keras1.info()
# soda_keras1.Kebanyakan_gula()
# soda_keras1.info_soda()

class minuman:
    def __init__(self, nama, jenis):
        self.nama =  nama
        self.jenis = jenis

    def info(self):
        print(f"minuman ini namanya {self.nama}dan jenis nya itu {self.jenis}")

class seger(minuman):
    def bentuk_seger(self):
        print("ini adalah minuman seger")

    def cek_kelayakan_sehat(self):
        print("cek kelayakan sehat minuman seger")

class soda(minuman):
    def bentuk_soda(self):
        print("ini adalah minuman soda")

    def cek_kelayakan_sehat(self):
        print("cek kelayakan sehat minuman soda")

class sodaseger(seger, soda):
    def info_seger_soda(self):
        print("ini adalah soda yang seger")

seger_soda1 = sodaseger("miras", "minuman keras")
seger_soda1.info()
seger_soda1.bentuk_seger()
seger_soda1.bentuk_soda()
seger_soda1.cek_kelayakan_sehat()
