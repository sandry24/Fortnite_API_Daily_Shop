from entry import Entry


class ItemShop:
    def __init__(self, entries, shown_types=None, wishlist=None):
        if wishlist is None:
            wishlist = []
        if shown_types is None:
            shown_types = ["outfit", "pickaxe", "glider", "backpack", "emote", "wrap", "music"]

        self.__shown_types = shown_types
        self.__wishlist = wishlist
        self.__items = []
        for entry in entries:
            entry = Entry(entry)
            self.__items.append(entry.to_item())

    def display_items(self):
        for shown_type in self.__shown_types:
            header = f"=={shown_type.upper()}S=="
            print(f"\n{header.center(65)}\n")
            type_items = []

            for item in self.__items:
                if item.get_type() == shown_type:
                    type_items.append(item)

            type_items.sort()
            for item in type_items:
                # print(item)
                item.display_in_columns()

        # Wishlist alert
        wishlisted_items = []
        for wishlisted_item in self.__wishlist:
            for item in self.__items:
                if item.contains(wishlisted_item):
                    wishlisted_items.append(item)
        if len(wishlisted_items) == 0:
            print("\nNo items from wishlist present")
        else:
            print("\n==WISHLISTED ITEMS==\n")
            for wishlisted_item in wishlisted_items:
                print(wishlisted_item)
