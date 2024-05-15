from datetime import datetime 

class Collection():
    def __init__(self, name):
        self.name = name
        self.nfts = []

    def total_spent(self):
        total_spent_tokens = 0
        total_spent_aud = 0
        for nft in self.nfts:
            total_spent_tokens += nft.pprice_tokens
            total_spent_aud += nft.pprice_aud
        return total_spent_tokens, total_spent_aud
    
class Nft():
    def __init__(self, id, collection, pprice_tokens, pprice_aud, purchase_date):
        self.id = id
        self.collection = collection
        self.pprice_tokens = pprice_tokens
        self.pprice_aud = pprice_aud
        self.purchase_date = purchase_date

    def calc_collection_ratio(self):
        total_spent_tokens, total_spent_aud = self.collection.total_spent()
        ratio_tokens = round(self.pprice_tokens/total_spent_tokens, 3)
        ratio_aud = round(self.pprice_aud/total_spent_aud, 3)
        return ratio_tokens, ratio_aud

# Initial NFT Data (No backend yet)

first_fed = Collection('Stargazers - First Federation')

first_fed.nfts = [
    Nft(2757, first_fed, 655, 10.82, datetime(2023, 9, 3)),
    Nft(3735, first_fed, 497, 8.22, datetime(2023, 9, 3)),
    Nft(3108, first_fed, 600, 8.96, datetime(2023, 9, 17))
    ]

after_the_filter = Collection("After the Filter")
after_the_filter.nfts = [
    Nft(1474, after_the_filter, 3000, 49.63, datetime(2023, 9, 3)),
    Nft(7794, after_the_filter, 4440, 73.45, datetime(2023, 9, 3)),
    Nft(1064, after_the_filter, 9000, 148.89, datetime(2023, 9, 3))
]

collections = [first_fed, after_the_filter]