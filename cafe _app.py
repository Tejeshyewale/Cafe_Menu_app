#create an store app:
from tkinter import *
import pandas as pd

menu = {'coffee': 20, 'samosa': 25, 'vadapav': 15, 'tea': 15, 'biscuits': 10, 'pohas': 30}

def show_menu():
    a = pd.DataFrame({
        'Menulist': list(menu.keys()),
        'Price': list(menu.values())
    }, index=range(1, len(menu) + 1))
    return a
def main():
    def update_order():
        global order
        selected_items = order_var.get().split(',')
        order_total = 0
        items = []

        for item in selected_items:
            item = item.strip().lower()
            if item in menu:
                order_total += menu[item]
                items.append(item)
            else:
                result_label.config(text=f'Item "{item}" is not available.')
                return

        order_label.config(text=f'Your order list: {", ".join(items)}')
        total_label.config(text=f'Total bill: ${order_total}')

    root = Tk()
    root.title("Cafe Management System")
    root.geometry('600x400')
    root.config(bg='red')

    # Create and place widgets
    welcome_label = Label(root, text="Welcome to Our Restaurant!", font=("Times New Roman", 20), bg='gray')
    welcome_label.place(x=120, y=20, height=60, width=360)

    menu_df = show_menu()
    menu_text = menu_df.to_string(index=False)

    menu_label = Label(root, text="Menu", font=("Times New Roman", 20), bg='white')
    menu_label.place(x=20, y=100, height=30, width=100)

    menu_display = Text(root, height=10, width=50, wrap=WORD)
    menu_display.insert(END, menu_text)
    menu_display.place(x=20, y=140)

    order_var = StringVar()
    order_entry = Entry(root, textvariable=order_var, width=50)
    order_entry.place(x=20, y=320)

    order_button = Button(root, text="Submit Order", command=update_order, bg='lightblue')
    order_button.place(x=500, y=320, width=80, height=30)

    order_label = Label(root, text="", font=("Times New Roman", 14), bg='yellow')
    order_label.place(x=20, y=360, width=300)

    total_label = Label(root, text="", font=("Times New Roman", 14), bg='yellow')
    total_label.place(x=20, y=380, width=300)

    result_label = Label(root, text="", font=("Times New Roman", 12), bg='yellow', fg='red')
    result_label.place(x=20, y=340, width=300)

    root.mainloop()

if __name__ == "__main__":
    main()
