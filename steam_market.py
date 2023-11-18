import requests


class SteamItem:
    @staticmethod
    def get_steam_item(name_hash = None,game_id=570, currency_id=1):
        """
        Retrieves information about the price of an item on the Steam Market.

        game_id: Game identifier (AppID). Default is 570 (Dota 2).
        currency_id: Currency identifier. Default is 1 (USD).
        name_hash: Market hash name of the item on Steam.
        return: JSON data with information about the item price.
        """
        if name_hash is None:
            raise ValueError("The 'name_hash' parameter is required.")
        
        ENDPOINT_STEAM= f"https://steamcommunity.com/market/priceoverview/?appid={game_id}&currency={currency_id}&market_hash_name={name_hash}"  
        return requests.get(ENDPOINT_STEAM).json()
    
    
    @staticmethod
    def get_steam_item_price(name_hash = None,game_id=570, currency_id=1):
        """
        Retrieves ONLY LOWEST price of an item on the Steam Market.

        game_id: Game identifier (AppID). Default is 570 (Dota 2).
        currency_id: Currency identifier. Default is 1 (USD).
        name_hash: Market hash name of the item on Steam.
        return: Information about the item price.
        """
        if name_hash is None:
            raise ValueError("The 'name_hash' parameter is required.")
        
        ENDPOINT_STEAM= f"https://steamcommunity.com/market/priceoverview/?appid={game_id}&currency={currency_id}&market_hash_name={name_hash}"  
        return requests.get(ENDPOINT_STEAM).json()["lowest_price"]