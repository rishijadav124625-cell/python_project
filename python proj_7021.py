
import matplotlib.pyplot as plt

# Pharmacy data list
pharmacy = []

# Add medicine
def add_medicine():
    name = input("Enter medicine name: ")
    category = input("Enter category (Tablet/Syrup/etc): ")
    price = float(input("Enter price: "))
    stock = int(input("Enter stock quantity: "))
    
    medicine = {"name": name, "category": category, "price": price, "stock": stock}
    pharmacy.append(medicine)
    print("Medicine added successfully!\n")

# Insert medicine at position
def insert_medicine():
    pos = int(input("Enter position: "))
    
    name = input("Enter medicine name: ")
    category = input("Enter category: ")
    price = float(input("Enter price: "))
    stock = int(input("Enter stock: "))
    
    medicine = {"name": name, "category": category, "price": price, "stock": stock}
    
    if pos >= 0 and pos <= len(pharmacy):
        pharmacy.insert(pos, medicine)
        print("Medicine inserted successfully!\n")
    else:
        print("Invalid position!\n")

# Update medicine
def update_medicine():
    name = input("Enter medicine name to update: ")
    
    for med in pharmacy:
        if med["name"] == name:
            med["category"] = input("Enter new category: ")
            med["price"] = float(input("Enter new price: "))
            med["stock"] = int(input("Enter new stock: "))
            print("Medicine updated successfully!\n")
            return
    
    print("Medicine not found!\n")

# Delete medicine
def delete_medicine():
    name = input("Enter medicine name to delete: ")
    
    for med in pharmacy:
        if med["name"] == name:
            pharmacy.remove(med)
            print("Medicine deleted successfully!\n")
            return
    
    print("Medicine not found!\n")

# Display medicines
def display():
    if not pharmacy:
        print("No data available!\n")
        return
    
    print("\n--- Medicine List ---")
    for med in pharmacy:
        print(med)
    print()

# Bar chart (stock)
def bar_chart():
    if not pharmacy:
        print("No data for chart!\n")
        return
    
    names = [med["name"] for med in pharmacy]
    stocks = [med["stock"] for med in pharmacy]
    
    plt.bar(names, stocks)
    plt.title("Medicine Stock")
    plt.xlabel("Medicine")
    plt.ylabel("Stock")
    plt.show()

# Pie chart (category distribution)
def pie_chart():
    if not pharmacy:
        print("No data for chart!\n")
        return
    
    category_count = {}
    
    for med in pharmacy:
        cat = med["category"]
        category_count[cat] = category_count.get(cat, 0) + 1
    
    labels = list(category_count.keys())
    sizes = list(category_count.values())
    
    plt.pie(sizes, labels=labels, autopct='%1.1f%%')
    plt.title("Category Distribution")
    plt.show()

# Menu
while True:
    print("1. Add Medicine")
    print("2. Insert Medicine")
    print("3. Update Medicine")
    print("4. Delete Medicine")
    print("5. Display Medicines")
    print("6. Bar Chart")
    print("7. Pie Chart")
    print("8. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        add_medicine()
    elif choice == "2":
        insert_medicine()
    elif choice == "3":
        update_medicine()
    elif choice == "4":
        delete_medicine()
    elif choice == "5":
        display()
    elif choice == "6":
        bar_chart()
    elif choice == "7":
        pie_chart()
    elif choice == "8":
        print("Exiting program...")
        break
    else:
        print("Invalid choice!\n")
