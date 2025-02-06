class Restaurant:
    def __init__(self,menus,tables,orders):
        self.menus=menus
        self.tables=tables
        self.orders=orders
    def add_to_menus(self,item):
        self.menus.append(item)
    def book_tables(self,table_no):
        if(table_no not in self.tables):
            self.tables.append(table_no)
            return True
        return False
    def add_customer_order(self,order):
        self.orders.append(order)
    def print_menu(self):
        print("Menu: ",self.menus)
    def print_tables_reservation(self):
        print("Tables Already Booked: ",self.tables)
    def print_customer_order(self):
        print("Order: ",self.orders)