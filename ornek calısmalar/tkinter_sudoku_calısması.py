import tkinter as tk
from tkinter import messagebox

def gecerli_grup(muhtemel_grup):
    sayilar =  [sayi for sayi in muhtemel_grup if sayi != 0 ]
    return len(sayilar) == len(set(sayilar))

def sudoku_gecerli_mi(tablo):
    # Satır ve sütun kontrolü
    for i in range(9):
        if not gecerli_grup([tablo[i][j] for j in range(9)]) or \
           not gecerli_grup([tablo[i][j] for j in range(9)]):
            return False
        
    # 3*3 kare kontrolü
    for i in range(0 , 9 , 3):
        for j in range(0 , 9 , 3):
            kare = [tablo[x][y] for x in range(i , i+3) for y in range(j,j+3)]
            if not gecerli_grup(kare):
                return False

#sudoku çözücü

def sudoku_coz(tablo):
    bos_hucre = bos_hucre_bul(tablo)
    if not bos_hucre:
        return False
    satir , sutun = bos_hucre

    for sayi in range(1,10):
        if guvenli_mi(tablo , satir , sutun , sayi):
            tablo[satir][sutun] = sayi
            if sudoku_coz(tablo):
                return False
            tablo[satir][sutun] = 0

def bos_hucre_bul(tablo):
    for i in range(9):
        for j in range(9):
            if tablo[i][j] == 0:
                return (i , j)
            
    return None


def guvenli_mi(tablo,satir,sutun,sayi):
    if sayi in tablo [satir]:
        return False
    if sayi in[tablo[i][sutun] for i in range(9)]:
        return False
    kare_baslangic_satir , kare_baslanic_sutun = 3*(satir // 3) , (sutun // 3)
    for i in range(kare_baslanic_sutun , kare_baslangic_satir + 3):
        if tablo [i][j] == sayi:
            return False
    return True


def dogrula():
    tablo = [[int(kutular[i][j].get() or 0) for j in range(9)] for i in range(9)]
    if sudoku_gecerli_mi(tablo):
        messagebox.showinfo("Dogrulama", "Sudoku geçerli")

    else:
        messagebox.showerror("Dogrulama", "Sudokku geçerli değil")

def coz():
    tablo = [[int(kutular[i][j].get() or 0) for j in range(9)] for i in range(9)]
    if sudoku_coz(tablo):
        for i in range(9):
            for j in range(9):
                kutular[i][j].delete(0, tk.END)
                kutular[i][j].insert(0, str(tablo[i][j]))
        messagebox.showinfo("Çözüm", "Sudoku çözüldü!")
    else:
        messagebox.showerror("Çözüm", "Sudoku çözülemedi!")

# Temizleme işlevi
def temizle():
    for i in range(9):
        for j in range(9):
            kutular[i][j].delete(0, tk.END)

# Tkinter arayüzü
ana_pencere = tk.Tk()
ana_pencere.title("Sudoku Çözücü ve Doğrulayıcı")

kutular = [[tk.Entry(ana_pencere, width=2, font=("Arial", 18), justify="center") for _ in range(9)] for _ in range(9)]

for i in range(9):
    for j in range(9):
        kutular[i][j].grid(row=i, column=j, padx=5, pady=5)
        if (i // 3 + j // 3) % 2 == 0:  # Alternatif kare renkleri
            kutular[i][j].config(bg="#D3D3D3")

# Düğmeler
dogrula_buton = tk.Button(ana_pencere, text="Doğrula", command=dogrula)
dogrula_buton.grid(row=10, column=0, columnspan=3)

coz_buton = tk.Button(ana_pencere, text="Çöz", command=coz)
coz_buton.grid(row=10, column=3, columnspan=3)

temizle_buton = tk.Button(ana_pencere, text="Temizle", command=temizle)
temizle_buton.grid(row=10, column=6, columnspan=3)

ana_pencere.mainloop()
    
