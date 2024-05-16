from item import Item


class Entry:
    def __init__(self, entry):
        self.__items = entry.items
        self.__main_item_type = entry.items[0].type.value
        self.__main_item_name = entry.items[0].name
        self.__main_item_price = entry.final_price
        self.__banner_value = entry.banner.value if entry.banner is not None else None
        self.__bundle = entry.bundle is not None

    def get_name(self):
        name = ""
        for item in self.__items:
            if item.type.value == self.__main_item_type:
                name += item.name + ", "
        name = name[:-2]  # Remove last comma and space
        return name

    def get_type(self):
        return self.__main_item_type

    def get_price(self):
        return self.__main_item_price

    def get_banner(self):
        return self.__banner_value

    def is_bundle(self):
        return self.__bundle

    def to_item(self):
        return Item(self.get_name(), self.get_type(), self.get_price(),
                    self.get_banner(), self.__items, self.is_bundle())
