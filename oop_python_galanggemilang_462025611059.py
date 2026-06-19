# class rental_ps():
#     def __init__(self, name, balance ):
#         self.name =  name
#         self.balance = balance

#     def sewasejam(self, amount):
#         if amount > self.balance:
#             raise ValueError("duit lu kurang dek, have you any money?")
#             self.balance -= amount
#             return self.balance

#     def cek_dompet(self, amount):
#         if amount < 0:
#             raise NameError("klo maen duit harus ada ye")
#             self.balance += amount
#             return self.balance

# rental = rental_ps("bocil", 2500)
# try:
#     print(rental.sewasejam(4000))
# except ValueError as e:
#     print(e)
# try:
#     print(rental.cek_dompet(200))
# except NameError as e:
#     print(e)

# class BalanceNotEnoughError(Exception):
#     pass
# class NegativeisisaldoError(Exception):
#     pass
# class IncorrectIdpersonalError(Exception):
#     pass
# class IncorretIdnumberError(Exception):
#     pass

# class rental_ps():
#     def __init__(self, nama, balance, Id_personal, Id_Number):
#         self.nama = nama
#         self.balance = balance 
#         self.Id_personal = Id_personal
#         self.Id_Number = Id_Number


#     def sewa_ps(self, isisaldo, Id_personal, Id_Number):
#         if Id_personal != self.Id_personal:
#             raise IncorrectIdpersonalError("lupa Id personal? you can ask to owner rental")
#         if Id_Number != self.Id_Number:
#             raise IncorretIdnumberError("yee masa lupa id number, you must try to memorize it")
#         if isisaldo > self.balance:
#             raise BalanceNotEnoughError("duit lu abis cill , minta ortu noh")
#         self.balance -= isisaldo
#         print(f"sewa ps sukses. saldo lu sekarang  = {self.balance}")

#     def cek_dompet(self, isisaldo):
#         if isisaldo < 0:
#             raise NegativeisisaldoError("saldo harus ada isi")
#         self.balance += isisaldo
#         return self.balance

#     def cek_balance (self, Id_personal, Id_Number):
#         if Id_personal != self.Id_personal:
#             raise IncorrectIdpersonalError("you must try haard")
#         if Id_Number != self.Id_Number:
#             raise IncorretIdnumberError("you must try hard")
#         print(f"lumayan stabil {self.balance}")

#     def minta_uang(self, isisaldo, Id_personal, Id_Number):
#         if isisaldo < 0:
#             raise NegativeisisaldoError("harus ada duit")
#         if Id_personal != self.Id_personal:
#             raise IncorrectIdpersonalError("you must correct")
#         if Id_Number != self.Id_Number:
#             raise IncorretIdnumberError("memorize it")
#         self.balance += isisaldo
#         print(f"minta uang berhasill gass maen game")

# user = rental_ps("mas bahlil", 2000, "MBG", "1919")

# try:
#     rental_ps.sewa_ps(user, 3000, "MBG", "1919")
#     rental_ps.cek_balance(user, "MBG", "1919")
#     rental_ps.minta_uang(user, 1000, "MBG", "1919")
# except BalanceNotEnoughError as e:
#     print(e)
# except IncorrectIdpersonalError as e:
#     print(e)
# except IncorretIdnumberError as e:
#     print (e)

# try:
#     rental_ps.cek_balance(user, "MBG", "1919")
#     rental_ps.minta_uang(user, 1000, "MBG", "1919")
#     rental_ps.sewa_ps(user, 3000, "MBG", "1919")

# except BalanceNotEnoughError as e:
#     print(e)
# except IncorrectIdpersonalError as e:
#     print(e)
# except IncorretIdnumberError as e:
#     print (e)       



class BalanceNotEnoughError(Exception):
    pass
class NegativeisisaldoError(Exception):
    pass
class IncorrectIdpersonalError(Exception):
    pass
class IncorretIdnumberError(Exception):
    pass

    
class rental_ps():
    def __init__(self, nama, balance, Id_personal, Id_Number):
        self.nama = nama
        self.balance = balance 
        self.Id_personal = Id_personal
        self.Id_Number = Id_Number

    def ngecek_id(self, Id_personal, Id_Number):
        if Id_personal != self.Id_personal:
            raise IncorrectIdpersonalError("cek lagi coba")
        if Id_Number != self.Id_Number:
            raise IncorretIdnumberError("inget2 lagi")

    def sewa_ps(self, isisaldo, Id_personal, Id_Number):
        self.ngecek_id(Id_personal, Id_Number)
        if isisaldo > self.balance:
            raise BalanceNotEnoughError("minta uang sono cill")
        self.balance -= isisaldo
        print(f"nah berhasil lu minta uang, nah sisa nya {self.balance}")

    def cek_dompet(self, isisaldo):
        if isisaldo < 0:
            raise NegativeisisaldoError("duit harus ada cill")
        self.balance += isisaldo
        return self.balance

    def cek_balance(self, Id_personal, Id_Number):
        self.ngecek_id(Id_personal, Id_Number)
        print(f"duit lu sekarang {self.balance}")
    
    def minta_uang(self, isisaldo, Id_personal, Id_Number):
        self.ngecek_id(Id_personal, Id_Number)
        if isisaldo < 0:
            raise NegativeisisaldoError("duit harus ada")
        self.balance += isisaldo
        print(f"minta uang berhasil. sisa uang lu{self.balance}")

user = rental_ps("mas bahlil", 2000, "MBG", "1919")

try:
    rental_ps.sewa_ps(user, 3000, "MBG", "1919")
    rental_ps.cek_balance(user, "MBG", "1919")
    rental_ps.minta_uang(user, 1000, "MBG", "1919")
except BalanceNotEnoughError as e:
    print(e)
except IncorrectIdpersonalError as e:
    print(e)
except IncorretIdnumberError as e:
    print (e)

try:
    rental_ps.cek_balance(user, "MBG", "1919")
    rental_ps.minta_uang(user, 1000, "MBG", "1919")
    rental_ps.sewa_ps(user, 3000, "MBG", "1919")

except BalanceNotEnoughError as e:
    print(e)
except IncorrectIdpersonalError as e:
    print(e)
except IncorretIdnumberError as e:
    print (e)       

        
