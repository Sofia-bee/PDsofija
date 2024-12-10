def main():
    total_sum = 0  # Kopējā summa
    while True:
        try:
            # Ievadīt preces nosaukumu
            item_name = input("Ievadi preces nosaukumu: ")
            if item_name == '0':
                break  # Ja nosaukums ir "0", programma beidzas
            
            # Ievadīt cenu un validēt
            price = input("Ievadi cenu: ")
            if price == '0':  # Ja cena ir 0, programma beidzas
                break
            price = float(price)
            if price < 0:
                print("Kļūda! Cena nedrīkst būt negatīva.")
                continue
            
            # Ievadīt daudzumu un validēt
            quantity = input("Ievadi daudzumu: ")
            quantity = float(quantity)
            if quantity < 0:
                print("Kļūda! Daudzumam jābūt pozitīvam skaitlim.")
                continue
            
            # Aprēķināt preces kopējo summu
            item_total = price * quantity
            total_sum += item_total  # Uzkrāt summu

            # Parādīt preces kopsummu
            print(f"Preces '{item_name}' kopējā summa: {item_total:.2f} €")
        
        except ValueError:
            print("Kļūda! Lūdzu, ievadi derīgus skaitļus.")
    
    # Beigās parādīt galīgo kopsummu
    print(f"Kopsumma: {total_sum:.2f} €")

# Programmas izsaukšana
main()
