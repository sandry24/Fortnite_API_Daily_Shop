class Item:
    def __init__(self, item_name, item_type, item_price, banner, items, bundle):
        self.__item_name = item_name
        self.__item_type = item_type
        self.__item_price = item_price
        self.__banner = banner
        self.__contains = items
        self.__bundle = bundle

    def get_name(self):
        return self.__item_name

    def get_type(self):
        return self.__item_type

    def get_price(self):
        return self.__item_price

    def get_banner(self):
        return self.__banner

    def is_bundle(self):
        return self.__bundle

    def contains(self, item_name):
        for item in self.__contains:
            if item.name == item_name:
                return True
        return False

    def __str__(self):
        string = f"{self.__item_name}"
        if self.__bundle:
            string += " (bundle)"
        string += f", {self.__item_price} vbucks"
        if self.__banner is not None:
            string += f" ({self.__banner.upper()})"
        return string

    def display_in_columns(self):
        string = ""
        name_col = f"{self.__item_name}"
        if self.__bundle:
            name_col += " (bundle)"
        if len(name_col) > 46:
            name_col = name_col[:43] + "..."
        price_col = f"{self.__item_price} vbucks"
        banner_col = f"{self.__banner.upper()}" if self.__banner is not None else ""
        string = name_col.ljust(50) + price_col.ljust(15) + banner_col
        print(string)

    def __lt__(self, other):
        return (self.__item_name, self.__item_price) < (other.__item_name, other.__item_price)
