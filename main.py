import fortnite_api
from item_shop import ItemShop

api_token = ""  # Get API key at https://dash.fortnite-api.com/account
api = fortnite_api.FortniteAPI(api_token)
shown_types = ["outfit", "emote", "pickaxe", "wrap", "glider"]  # empty will show all items
wishlist = ["Kratos", "Leviathan Axe", "Social Climber", "Starlit"]

if __name__ == "__main__":
    Shop_json = api.shop.fetch(combined=True)
    Shop = ItemShop(Shop_json.featured.entries, shown_types, wishlist)
    Shop.display_items()
