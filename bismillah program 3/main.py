class Shirt:
    def __init__(self, name, size, price):
        self.name = name
        self.size = size
        self.price = price

    def __str__(self):
        return f"{self.name} | {self.size} | {self.price:.2f}"

class ShirtManager:
    def __init__(self):
        self.shirts = []

    def add_shirt(self, shirt):
        self.shirts.append(shirt)

    def get_shirts(self):
        return self.shirts

class ShirtView:
    def display_menu(self):
        print("\n=== Toko Baju ===")
        print("1. Tambah Baju")
        print("2. Tampilkan Semua Baju")
        print("3. Keluar")

    def get_user_input(self):
        while True:
            try:
                choice = int(input("Pilih menu (1-3): "))
                if choice not in [1, 2, 3]:
                    raise ValueError("Pilihan tidak valid.")
                return choice
            except ValueError as e:
                print(f"Error: {e}. Silakan coba lagi.")

    def get_shirt_details(self):
        name = input("Masukkan nama baju: ")
        size = input("Masukkan ukuran baju (S/M/L/XL): ").upper()
        
        while True:
            try:
                price = float(input("Masukkan harga baju: "))
                if price < 0:
                    raise ValueError("Harga tidak boleh negatif.")
                break
            except ValueError as e:
                print(f"Error: {e}. Silakan coba lagi.")

        return Shirt(name, size, price)

    def display_shirts(self, shirts):
        print("\n=== Daftar Baju ===")
        print("Nama | Ukuran | Harga")
        for shirt in shirts:
            print(shirt)
        print("====================\n")

def main():
    manager = ShirtManager()
    view = ShirtView()

    while True:
        view.display_menu()
        choice = view.get_user_input()

        if choice == 1:
            shirt = view.get_shirt_details()
            manager.add_shirt(shirt)
            print("Baju berhasil ditambahkan!")
        
        elif choice == 2:
            shirts = manager.get_shirts()
            view.display_shirts(shirts)
        
        elif choice == 3:
            print("Terima kasih! Sampai jumpa!")
            break

if __name__ == "__main__":
    main()
1