import fortnite_api
from item_shop import ItemShop
from api_token import api_token
from wishlist import wishlist
from shown_types import shown_types


if __name__ == "__main__":
    api = fortnite_api.FortniteAPI(api_token)
    Shop_json = api.shop.fetch(combined=True)
    Shop = ItemShop(Shop_json.featured.entries, shown_types, wishlist)
    Shop.display_items()
